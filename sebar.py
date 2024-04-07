import asyncio
import time
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest, GetHistoryRequest, ForwardMessagesRequest
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
                if len(message.message.split()) < 100 and any(keyword in message.message.lower() for keyword in keywords):
                    await asyncio.sleep(10)
                    await client(ForwardMessagesRequest(
                        from_peer=source_entity,
                        to_peer=destination_entity,
                        id=[message.id]
                    ))
                    print(f"Pesan diterima dari grup dengan ID: {source_group_id}, dan diteruskan ke grup dengan ID: {destination_group_id}")

client.loop.run_until_complete(main())
print(time.asctime(), '-', 'Mulai')