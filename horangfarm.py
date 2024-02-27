import time
import asyncio
import logging
from telethon import TelegramClient, events

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Horang'

restore = '/restore_max_confirm'
siram = '/siram'
panen = '/ambilPanen'
farm = '/kebun'
bot = ['danaudalamhutan', 'KampungMaifamXBot', 'KampungMaifamX4Bot', 'KampungMaifamBot']
ambil = '/ambilHasil'
beri = '/beriMakan'
jhasil = 0
jtanam = 0

logging.basicConfig(level=logging.ERROR)

async def bentar(w):
    await asyncio.sleep(w)

async def cmd_tanam(client, bot):
    tanam = ['/tanam_Tomat_655', '/tanam_Cabai_655']
    for command in tanam:
        await asyncio.sleep(3)
        await client.send_message(bot, command)
        if len(tanam) <= 1:
            await asyncio.sleep(3)
            await client.send_message(bot, command)
        elif len(tanam) >= 2:
            await asyncio.sleep(3)
            await client.send_message(bot, siram)
        

async def mancingddh(client, w):
    while True:
        await client.send_message(bot[0], "/fish")
        await bentar(w)

with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot[1], siram)) 
    
    @client.on(events.NewMessage(from_users=bot[1]))
    async def handler(event):
        global jtanam, jhasil
        pesan = event.raw_text
        
        if "Berhasil menyiram tanaman" in pesan:
            print(time.asctime(), 'Siram')
            time.sleep(2)
            await event.respond(beri)
        
        elif "Kamu berhasil memanen" in pesan:
            print(time.asctime(), pesan)
            jhasil = 0
            jtanam = 0
            time.sleep(2)
            await cmd_tanam(client, bot[1]) 
            return
        
        elif "Kamu berhasil menanam" in pesan:
            print(pesan)
            #jtanam += 1
            #if jtanam:
                #if jtanam >= 2:
                    #time.sleep(2)
                    #await event.respond(siram)
            return

        elif "Kamu memperoleh:" in pesan:
            jhasil += 1
            print(time.asctime(), f'Hasil ternak = {jhasil}')
            if jhasil:
                if jhasil >= 10:
                    time.sleep(2)
                    await event.respond(panen)
                else:
                    time.sleep(2)
                    await event.respond(beri)
            return
            
        elif "Tak ada yang bisa dipanen" in pesan or "Tak ada ternak untuk" in pesan:
            time.sleep(2)
            await event.respond(ambil)
            return
          
        elif "Berhasil memberi makan ternak" in pesan or "Tak ada tanaman untuk disiram" in pesan:
            time.sleep(2)
            await event.respond(ambil)
          
        elif "Lahan tersisa di kebun kamu tidak mencukupi" in pesan:
            time.sleep(2)
            await event.respond(farm)
         
        elif 'Kamu tidak memiliki cukup energi' in pesan:
            print(time.asctime(), pesan)
            time.sleep(2)
            await event.respond(restore)
            
        elif 'Energi berhasil dipulihkan' in pesan:
            print(time.asctime(), pesan)
            time.sleep(2)
            await event.respond(siram)
        
        elif '🌲 Kebun' in pesan:
            if 'siap panen!!' in pesan:
                time.sleep(2)
                await event.respond(panen)
            elif 'siram' in pesan:
                time.sleep(2)
                await event.respond(siram)
            elif 'Kebun kamu kosong' in pesan:
                time.sleep(2)
                await cmd_tanam(client, bot[1])
            else:
                time.sleep(2)
                await event.respond(ambil)

    client.start() 
    print(time.asctime(), '-', 'start')
    client.loop.create_task(mancingddh(client, 245))
    print(time.asctime(), '-', 'ddh')
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')