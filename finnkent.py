import time, os, asyncio, sys, re, random, datetime
from time import sleep
from random import randint
from datetime import datetime
from telethon import TelegramClient, events, utils, Button
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = "Finnkent"

bot_id = [-1001944528171, 'KampungMaifamXBot', 'KampungMaifamX4Bot', 'KampungMaifamBot']

restore = '/restore_max_confirm'

#jenis hewan 
hewan = input("Nama hewan = ")
#jumlah 
jmlh = input("berapa jumlahnya = ")
ternak = f"/pelihara_{hewan}_{jmlh}"

bet = (
'1',
'1+42',
'5+41',
'69',
'4646'
)

judi = "Bbet "+str(random.choice(bet))

tnk = 0

async def bentar(w):
    await asyncio.sleep(w)

async def lifegames(client,w):
    while True:
        await client.send_message(bot[0], judi)
        await bentar(w)

with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id[2], ternak))

    @client.on(events.NewMessage(from_users=bot_id[2]))
    async def handler(event):
        pesan = event.raw_text
        global tnk
        
        if "Berhasil menambahkan" in pesan or "Kandang ternak khusus penuh" in pesan:
            time.sleep(1.5)
            await event.respond('/ambilHewan')
            return
        
        if "Kamu berhasil mendapat" in pesan:
            print(time.asctime(), 'Ke -',tnk)
            tnk += 1
            if tnk == 15 :
                await bentar(turu)
                await client.send_message(bot[3], "/pfs_AreaClassE_ambilpanen")
                await bentar(turu)
                await client.send_message(bot[3], "/pfs_AreaClassD_ambilpanen")
                await bentar(turu)
                await client.send_message(bot[3], "/pfs_AreaClassC_ambilpanen")
                await bentar(turu)
                await client.send_message(bot[3], "/pfs_AreaClassS_ambilpanen")
                await bentar(turu)
                tnk =- 15
            time.sleep(1.5)
            await event.respond(ternak)
            return
          
        if "Kamu tidak memiliki cukup energi" in pesan:
            time.sleep(1.5)
            await event.respond(restore)
            return
                
        if "Energi berhasil" in pesan:
            print(time.asctime(), 'Energi pulih')
            time.sleep(1.5)
            await event.respond(ternak) 
            return
          
        elif "Tidak ada yang bisa diambil" in pesan:
            print(time.asctime(), pesan)
            time.sleep(1.5)
            await event.respond(ternak)
            return
        
    client.start() 
    print(time.asctime(), '-', 'mulai')
    client.loop.create_task(lifegames(client,5))
    print(time.asctime(), '-', 'ddh')
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	