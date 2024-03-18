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

narasi = {
    "Sungai dangkal, kelihatannya di sini",
    "Legenda mengatakan kalau seseorang",
    "Hanya ikan besar yang tinggal di sini",
    "Ikan langka tinggal di sini",
    "Terletak di bagian timur Kampung Maifam",
    "Orang-orang mengklaim kalau mereka",
    "Bertahun-tahun yang lalu",
    "Laut aneh berbahaya",
    "Laut terkutuk yang dipenuhi hantu",
    "berhasil mendapatkan"
}

area = [
  "LautGabagaba",
  "LautPurba",
  "LautBerhantu"
]

mg = "/mg24_"
waktu = 18.5
i = 0

with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, mg+str(area[i])))
    @client.on(events.NewMessage(incoming=True, from_users=bot_id))
    async def handler(event):
        pesan = event.raw_text
        global waktu,i
      
        if any(nar in pesan for nar in narasi):
            time.sleep(waktu)
            await event.click(0,0)
            return
         
        if "silakan memancing di tempat lain" in pesan:
            while "silakan memancing di tempat lain" in pesan:
                waktu = 18.5
                i = (i + 1) % len(area) 
                time.sleep(2)
                await client.send_message(bot_id, mg+str(area[i]))
                break
            return
        
        if "sayang sekali belum ada ikan" in pesan:
            waktu += 1
            time.sleep(waktu)
            await event.click(0,0)
            return
        
    client.start()
    print(time.asctime(), '-', 'Mulai')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Berhanti')