import asyncio
import time
import random
from telethon import TelegramClient, events, Button

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
session_file = input('Akun :')

cmd = 'Bbet 1+45'
group_id = -1001944528171

bet = (
    '1+45',
    '5+45',
    '69',
)

user_id = 1396547380

async def wait_for(seconds):
    await asyncio.sleep(seconds)

async def main():
    async with TelegramClient(session_file, api_id, api_hash) as client:
        await client.send_message(group_id, cmd)

        @client.on(events.NewMessage(chats=group_id))
        async def handler(event):
            message = event.raw_text
            sender = await event.client.get_entity(event.sender_id)

            if "🚓 Zifri sepertinya kamu mencoba melanggar hukum.." in message:
                print(time.asctime(), message)
                await wait_for(600)
                await client.send_message(group_id, cmd)

            elif "🎰 Zifri telah bertaruh" in message:
                print(time.asctime(), message)
                await wait_for(5)
                await client.send_message(group_id, "Bbet " + str(random.choice(bet)))

            elif not sender.bot and not sender.user_id and 'send' in message:
                print(time.asctime(), message)
                await wait_for(5)
                await event.reply('Ppay *')

        await client.run_until_disconnected()

asyncio.run(main())
print(time.asctime(), '-', 'berhenti')