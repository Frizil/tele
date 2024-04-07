import asyncio
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ForwardMessagesRequest

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'

sesi_file = 'Zifri'

client = TelegramClient(sesi_file, api_id, api_hash)

keywords = ['nd', 'need', 'temenan', 'sini']

async def main():
    async with client:
        dialogs = await client(GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=100,  # Set limit to the maximum allowed value
            hash=0
        ))
        
        for dialog in dialogs.dialogs:
            if dialog.title == 'LPMBANG':
                destination_entity = dialog.entity
                break
        
        source_entity = None
        for dialog in dialogs.dialogs:
            if dialog.title == 'BIO_RPP_30':
                source_entity = dialog.entity
                break
        
        if source_entity is not None:
            messages = await client(GetHistoryRequest(
                peer=source_entity,
                limit=100,  # Set limit to the maximum allowed value
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0
            ))
            
            for message in messages.messages:
                if any(keyword in message.message.lower() for keyword in keywords):
                    await asyncio.sleep(5)
                    await client(ForwardMessagesRequest(
                        from_peer=source_entity,
                        to_peer=destination_entity,
                        id=[message.id]
                    ))

client.loop.run_until_complete(main())