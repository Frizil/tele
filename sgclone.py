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

mergeList = [
'Mentimun',
'Anggur',
'Apel',
'Avokad',
'BungaMatahari',
'Cabai',
'Jagung',
'Jeruk',
'Kentang',
'Lily',
'Mawar',
'Melon',
'Mentimun',
'Nanas',
'Pisang',
'Sakura',
'Semangka',
'Strawberry',
'Tomat',
'Wortel',
'BuahNaga',
'Jambu',
'KacangTanah',
'Kelapa',
'Mangga',
'Nangka',
'Pepaya',
'Persik',
'Pir',
'Rambutan',
'Terung',
'Tulip',
'Ubi',
'AnggurKeramat',
'BerryKeramat',
'LabuKeramat',
'ManggaKeramat',
'NanasKeramat',
'PisangKeramat',
'TerungKeramat',
'TomatKeramat',
'WortelKeramat',
'Last',
]

Grade = [
'',
'E',
'D',
'C',
'B',
'A',
'Last',
]

bot = ['danaudalamhutan', 'KampungMaifamXBot', 'KampungMaifamX4Bot', 'KampungMaifamBot']
hasil = "/casino_hasil"
judi = "/casino_UltraLuck_"
ternak = "/ambilHasil"
makan = "/beriMakan"
mese = '/sg_harvest'
sghc = '/sg_hc'
panen = '/sg_panen'
#logs = 'fincasino'
turu = 4
mer = 0
gradenum = 0


q = []


async def bentar(w):
    await asyncio.sleep(w)

async def mancingddh(client,w):
    while True:
        await client.send_message(bot[0], "/fish")
        await bentar(w)

with TelegramClient(sesi_fil, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot[1], panen))
    @client.on(events.NewMessage(incoming=True, from_users=bot[1]))
    async def handler(event):
        pesan = event.raw_text
        global mer
        global idMer
        global gradenum
        
        if "di keranjang buah" in pesan:
            mer += 1
            time.sleep(2)
            await event.respond('/sg_merge_'+mergeList[mer]+Grade[gradenum])
            return

        if "tidak memiliki cukup energi" in pesan:
            time.sleep(2)
            await event.respond('/restore_max_confirm')
            print(time.asctime(), 'Isi energi')
            return

        if "Kamu tidak memiliki" in pesan:
            mer +=1
            
            if mer %15 == 0 :
                await client.send_message(bot[3], hasil)
                await bentar(turu)
                await client.send_message(bot[3], judi+str(random.randint(1,50))+"_5e12")
                await bentar(turu)
                await client.send_message(bot[3], ternak)
                await bentar(turu)
                await client.send_message(bot[3], makan)
                await bentar(turu)
                await client.send_message(bot[3], "/sg_panen")
                await bentar(10)
                
            await bentar(turu)
            await event.respond('/sg_merge_'+mergeList[mer]+Grade[gradenum])
            return
        
        #if "1500x menjadi" in pesan:

            #time.sleep(2)
            #await event.respond('/sg_merge_'+mergeList[mer]+Grade[gradenum])
            #return
        
        if 'Berhasil menggabungkan' in pesan:
            await bentar(0.9)
            msg = await client.get_messages(bot[1],ids = idMer)
            await msg.click(0,2)
            return
          
                
        if 'Energi berhasil' in pesan:
            time.sleep(2)
            await event.respond(panen)
            print(time.asctime(), 'Yuk sekarang masak lagi')
            return
        
        if 'Keranjang buah tidak mencukupi' in pesan:
            time.sleep(2)
            await event.respond('/sg_merge_'+mergeList[mer]+Grade[gradenum])
            return
            
        if 'Berhasil memanen' in pesan or 'Tidak ada yang bisa dipanen' in pesan:
            time.sleep(2)
            await event.respond('/sg_merge_'+mergeList[mer]+Grade[gradenum])
            return

              
        if mergeList[mer] == mergeList[-1]:
            gradenum +=1
            mer = 0
            print('Yosh Naik Grade!!')
            time.sleep(2)
            await event.respond('/sg_merge_'+mergeList[mer]+Grade[gradenum])
            return
        
        if Grade[gradenum] == Grade[-1]:
            gradenum = 0
            mer = 0
            time.sleep(2)
            print('Yosh ulang!!')
            await client.send_message(bot[1], panen)
            return
        
        elif "dimiliki:" in pesan:
            idMer = event.id
            msg = await client.get_messages(bot[1],ids = idMer)
            time.sleep(1.5)
            a = pesan.split()
            b = int(a.index('dimiliki:'))
            total = int(a[b+1])
            if total < 500:
                await msg.click(text="Gabung 5")
                return
            #elif total >= 500 and total < 1000:
                #await msg.click(text="Gabung 5")
                #return
            #elif total >= 1000 and total < 1500:
                #await msg.click(text="Gabung 5")
                #return
            #elif total >= 1500:
                #await msg.click(text="Gabung 5")
            return
          
            
    @client.on(events.NewMessage(from_users=bot[3]))
    async def handle_chat(event):
        message = event.raw_text
        
        if "Kamu tidak memiliki cukup energi" in message:
            print(time.asctime(), 'Capek aseli')
            await bentar(2)
            await client.send_message(bot[3], "/makan_RotiBelanda")
            
        if "Tidak tidak" in message:
            print(time.asctime(), 'Kenyang WOI!!!')
            await bentar(2)
            await client.send_message(bot[3], "/restore_max_confirm")
            
        #if "Kamu Memenangkan Permainan!!" in message:
            #await bentar(2)
            #await client.forward_messages(logs, event.message)
            #return


    client.start()
    print(time.asctime(), '-', 'Start')
    client.loop.create_task(mancingddh(client,245))
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stop')

