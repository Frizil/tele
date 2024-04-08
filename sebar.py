import asyncio
import time
from telethon.sync import TelegramClient

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Zifri'

async def forward_messages():
    async with TelegramClient(sesi_file, api_id, api_hash) as client:
        source_group_id = -1001332967453  # Example source group ID
        destination_group_id = -1002067531778  # Example destination group ID
        
        source_entity = await client.get_entity(source_group_id)
        destination_entity = await client.get_entity(destination_group_id)
        
        async for message in client.iter_messages(source_entity):
            if len(message.text.split()) < 50:
                await client.forward_messages(destination_entity, message)

async def main():
    print(time.asctime(), '-', 'Mulai')
    task = asyncio.create_task(forward_messages())
    await task
    print(time.asctime(), '-', 'Selesai')

asyncio.run(main())