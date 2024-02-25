import time, asyncio, sys, random
import logging
from telethon import TelegramClient, events, utils

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
jpanen = 0
jtanam = 0
jhasil = 0

logging.basicConfig(level=logging.ERROR)
    
async def bentar(w):
    await asyncio.sleep(w)

async def mancingddh(client,w):
    while True:
        await client.send_message(bot[0], "/fish")
        await bentar(w)
        
tanam = ['/tanam_Tomat_655', '/tanam_Cabai_655']

with TelegramClient(sesi_file, api_id, api_hash) as client:
    for command in tanam:
        client.loop.run_until_complete(client.send_message(bot[1], command))
        @client.on(events.NewMessage(from_users=bot[1]))
        async def handler(event):
            global jtanam, jpanen, jhasil
            pesan = event.raw_text
            
            
            if "Berhasil menyiram tanaman" in pesan:
                jtanam = 0
                print(time.asctime(), 'Siram')
                time.sleep(2)
                await event.respond(ambil)
                return
    
            if "Kamu berhasil memanen" in pesan:
                print(time.asctime(), pesan)
                jhasil = 0
                time.sleep(2)
                for cmd in tanam:
                    time.sleep(2)
                    client.send_message(bot[1], cmd)
                    break
                return
            
            if "Kamu berhasil menanam" in pesan:
                jtanam += 1
                if jtanam:
                   if jtanam >= 2:
                      time.sleep(2)
                      await event.respond(siram)
                      break
                return
                
    
            if "Kamu memperoleh:" in pesan:
                jhasil += 1
                print(time.asctime(), 'Hasil ternak')
                time.sleep(2)
                await event.respond(beri)
                if jhasil:
                    if jhasil >= 10:
                        time.sleep(2)
                        await event.respond(panen)
                    else:
                        time.sleep(2)
                        await event.respond(ambil)
                        break
                return
                 
                
            if "Tak ada yang bisa dipanen" in pesan:
                print(time.asctime(), pesan)
                time.sleep(2)
                await event.respond(ambil)
                return
              
            if "Berhasil memberi makan ternak" in pesan:
                print(time.asctime(), pesan)
                time.sleep(2)
                await event.respond(ambil)
              
            if "Tak ada ternak untuk" in pesan:
                print(time.asctime(), pesan)
                time.sleep(2)
                await event.respond(ambil)
                return
               
            if "Lahan tersisa di kebun kamu tidak mencukupi" in pesan:
                time.sleep(2)
                await event.respond(farm)
                return
             
            if 'Kamu tidak memiliki cukup energi' in pesan:
                print('Energi habis')
                time.sleep(2)
                await event.respond(restore)
                return
                
            if 'Energi berhasil dipulihkan' in pesan:
                time.sleep(2)
                await event.respond(siram)
                return
            
            if 'Tak ada tanaman untuk disiram' in pesan:
                time.sleep(2)
                await event.respond(farm)
                return
              
            if '🌲 Kebun' in pesan:
                if 'siap panen!!' in pesan:
                    time.sleep(2)
                    await event.respond(panen)
                elif 'siram' in pesan:,
                    time.sleep(2)
                    await event.respond(siram)
                else:
                    time.sleep(2)
                    await event.respond(ambil)
                return
              
           
            
        client.start() 
        print(time.asctime(), '-', 'start')
        client.loop.create_task(mancingddh(client,245))
        print(time.asctime(), '-', 'ddh')
        client.run_until_disconnected() 
        print(time.asctime(), '-', 'berhenti')