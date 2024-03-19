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


area = "GuaTambang"
mg = "/mg24_"
jeda = 4
cmd = mg+str(area)
skill = 0 
koin = 0
buffe = "/mg2024_buff_Energi"
buffk = "/mg2024_buff_DoublePoint"
kurangi = "/mg2024_kurangiskill_400"

with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, cmd))
    @client.on(events.NewMessage(incoming=True, from_users=bot_id))
    async def handler(event):
        pesan = event.raw_text
        global jeda, skill, koin
        
      
        if "Tingkatkan kemampuanmu dan bawa pulang" in pesan:
            time.sleep(jeda)
            await event.click(0,0)
            return
          
        if "Kamu mendapat" in pesan:
            narasi = event.raw_text
            pola = r"Tunggu (\d+) detik sampai kamu bisa menambang lagi\.\.\."
            pola_kemampuan = r"Kemampuan Menambang \+(\d+)"
            pola_koin = r"Koin Tambang \+(\d+)"
            pola_energi = r"Energi: (\d+)%"
            
            hasil_kemampuan = re.search(pola_kemampuan, narasi)
            hasil_koin = re.search(pola_koin, narasi)
            hasil_pencarian = re.search(pola, pesan)
            hasil_energi = re.search(pola_energi, pesan)
            persentase_energi = int(hasil_energi.group(1))
            kemampuan = int(hasil_kemampuan.group(1))
            koin_tambang = int(hasil_koin.group(1))
            jeda = int(hasil_pencarian.group(1))
           
            if hasil_kemampuan and hasil_koin:
                os.system("clear")
                skill+=kemampuan
                koin+=koin_tambang
                print("Skill =", skill)
                print("Koin =", koin)
                
            if koin:
                if koin >= 1500:
                    time.sleep(2)
                    await event.respond(buffk)
            if skill:
                if skill >= 500:
                    time.sleep(2)
                    await event.respond(kurangi)

            if persentase_energi > 50:
                time.sleep(jeda)
                await event.click(text="⛏⛏⛏⛏")
                
            if persentase_energi < 50:
                time.sleep(jeda)
                await event.respond(buffe) 
            return
          
        if "Pelan-pelan, kamu masih terlalu lelah" in pesan:
            time.sleep(jeda)
            await event.click(text="⛏⛏⛏⛏")
            return
          
        if "Energi dipulihkan menjadi" in pesan:
            jeda = 4
            koin -= 150
            time.sleep(2)
            await event.respond(cmd)
            return
          
        if "dikurangi dari kemampuan tambang" in pesan:
            skill -= 400
            return
          
        if "yang kamu dapat akan dilipatgandakan" in pesan:
            koin -= 1000
            return
          
        if "Permainan selesai!!" in pesan:
            print("Game Berakhir")
            return
        
    client.start()
    print(time.asctime(), '-', 'Mulai')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Berhanti')