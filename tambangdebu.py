import time, os
import asyncio
import sys, re
import random
import datetime
from time import sleep
from random import randint
from datetime import datetime
from telethon import TelegramClient, events, utils, Button
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input("Akun : ")

print("\ncontoh: Angka = 2")
print("Pilih bot yng digunakan")
mpm = input("\tKetik 1 untuk Bot Alpha\n\tKetik 2 untuk Bot X\n\tKetik 3 untuk Bot X4\n   Angka = ")
if mpm == '1':
    bot_id = 'KampungMaifamBot'
elif mpm == '2':
    bot_id = 'KampungMaifamXBot'
elif mpm == '3':
    bot_id = 'KampungMaifamX4Bot'


with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, cmd))
    @client.on(events.NewMessage(incoming=True, from_users=bot_id))
    async def handler(event):
        pesan = event.raw_text
        
        cmd = ['/safebox_meedios_x_50', '/donasiGuild_meedios_50']
        for command in cmd:
            time.sleep(2)
            await client.send_message(command)
                
     
    client.start()
    print(time.asctime(), '-', 'Mulai')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Berhanti')