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
sesi_fil = input("Akun : ")

bot = 'KampungMaifamXBot'
cmd = "/mg24_game_Tambahan_74"
jeda = 4.5

with TelegramClient(sesi_fil, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot, cmd))
    @client.on(events.NewMessage(incoming=True, from_users=bot))
    async def handler(event):
        pesan = event.raw_text
        
        
        if "Poin didapat dari memainkan" in pesan:
            time.sleep(jeda)
            await event.click(text="Play")
            return
          
        if "Kamu memutar SlotMachine" in pesan or "Tunggu 5 detik sebelum" in pesan:
            time.sleep(jeda)
            await event.click(text="Play")
            return


    client.start()
    print(time.asctime(), '-', 'Start')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stop')

