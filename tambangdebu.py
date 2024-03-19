import time
import asyncio
from telethon import TelegramClient, events

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'

sesi_file = input("Akun: ")

print("\ncontoh: Angka = 2")
print("Pilih bot yang digunakan:")
mpm = input("\tKetik 1 untuk Bot Alpha\n\tKetik 2 untuk Bot X\n\tKetik 3 untuk Bot X4\nAngka = ")
if mpm == '1':
    bot_id = 'KampungMaifamBot'
elif mpm == '2':
    bot_id = 'KampungMaifamXBot'
elif mpm == '3':
    bot_id = 'KampungMaifamX4Bot'

cmd = ['/safebox_meedios_x_50', '/donasiGuild_meedios_50']

async def send_messages():
    async with TelegramClient(sesi_file, api_id, api_hash) as client:
        for command in cmd:
            await client.send_message(bot_id, command)
            await asyncio.sleep(2)

        @client.on(events.NewMessage(incoming=True, from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text
            print("Pesan yang diterima dari bot:", pesan)

        print(time.asctime(), '-', 'Mulai')
        await client.run_until_disconnected()
        print(time.asctime(), '-', 'Berhenti')

asyncio.run(send_messages())