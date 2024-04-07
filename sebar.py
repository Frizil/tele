import asyncio
import time
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest, GetHistoryRequest, ForwardMessagesRequest, SendMessageRequest
from telethon.tl.types import InputPeerEmpty

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Zifri'

client = TelegramClient(sesi_file, api_id, api_hash)

keywords = [' ']

async def main():
    async with client:
        dialogs = await client(GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=100,
            hash=0
        ))
        
        # Replace 'destination_group_id' and 'source_group_id' with the actual group IDs
        destination_group_id = -1002067531778  # Example destination group ID
        source_group_id = -1001332967453  # Example source group ID
        
        destination_entity = await client.get_input_entity(destination_group_id)
        source_entity = await client.get_input_entity(source_group_id)
        
        if source_entity is not None:
            messages = await client(GetHistoryRequest(
                peer=source_entity,
                limit=100,
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0
            ))
            
            for message in messages.messages:
                sender = await client.get_entity(message.sender_id)
                sender_username = sender.username if sender.username else "No username"
                sender_user_id = sender.id
                if len(message.message.split()) < 25 and any(keyword in message.message.lower() for keyword in keywords):
                    await asyncio.sleep(15)
                    forwarded_message = await client(ForwardMessagesRequest(
                        from_peer=source_entity,
                        to_peer=destination_entity,
                        id=[message.id]
                    ))
                    reply_message = f"Pesan dari {sender_username} dengan ID: {sender_user_id}"
                    await asyncio.sleep(2)
                    await client(SendMessageRequest(forwarded_message.to_id, reply_message))  # Reply to the forwarded message with the sender's information
                    print(reply_message)

print(time.asctime(), '-', 'Mulai')
client.loop.run_until_complete(main())