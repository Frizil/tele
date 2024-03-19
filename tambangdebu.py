import time
import asyncio
import sys
import threading
import re
from telethon import TelegramClient, events, utils
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_fil = input('Akun : ')

def fani():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with TelegramClient(sesi_fil, api_id, api_hash, loop=loop) as clien:
        clien.loop.run_until_complete(clien.send_message("kampungmaifambot", '/mg2024_game_Tambang_20'))

        @clien.on(events.NewMessage(from_users="kampungmaifambot"))
        async def handler(event):
            print(event.raw_text)
            
            if 'Tunggu 20' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(15)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return
            
            if 'Tunggu 19' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(14)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return
            
            if 'Tunggu 18' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(13)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return
            
            if 'Tunggu 17' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(12)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return
            
            if 'Tunggu 16' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(11)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return
        
            if 'Tunggu 15' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(10)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return
        
            if 'Tunggu 14' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(9)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return
        
            if 'Tunggu 13' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(8)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return 
        
            if 'Tunggu 12' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(7)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return 
        
            if 'Tunggu 11' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(6)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return 
        
            if 'Tunggu 10' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(5)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return 
        
            if 'Tunggu 9' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(4)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return 
        
            if 'Tunggu 8' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(3)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return 
            
            if 'Tunggu 7' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(2)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return  
            
            if 'Tunggu 6' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(1)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return  
            
            if 'Tunggu 5' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(1)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return    

            if 'Tunggu 4' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(1)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return             

            if 'Tunggu 3' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(1)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return            

            if 'Tunggu 2' in event.raw_text:
                pesan = event.text
                a = pesan.split('\n\n')
                for x in a:
                    if 'Kemampuan' in x:
                        time.sleep(1)
                        o = re.findall('\d+', x)
                        angka2 = str(o[0])
                        await event.respond("/mg24_kurangiSkill_"+angka2) 
                        return
                return
                
            if "900 dikurangi dari kemampuan tambang" in event.raw_text:
                time.sleep(1.5)
                await event.respond('/mg2024_GuaTambang')
                return
                
            if "dikurangi dari kemampuan tambang" in event.raw_text:
                time.sleep(1.5)
                await event.respond('/mg2024_buff_Energi')
                return
                
            if "Tiap peserta akan" in event.raw_text:
                time.sleep(1.5)
                await event.click(text='START')
                return
                
            if "Apa kamu yakin ingin" in event.raw_text:
                time.sleep(1)
                await event.click(text='Confirm')
                return
                
            if "Energi dipulihkan menjadi 100%!!" in event.raw_text:
                time.sleep(1.5)
                await event.respond('/mg2024_GuaTambang')
                return
                
            if "Permainan dimulai" in event.raw_text:
                time.sleep(1)
                await event.respond('/mg24_kurangiSkill_900')
                return
                
            if "Kamu memerlukan" in event.raw_text:
                time.sleep(1.5)
                await event.respond('/mg2024_GuaTambang')
                return
                
            if 'Tingkatkan kemampuan' in event.raw_text:
                time.sleep(1)
                await event.click(text='⛏')
                return
        

        clien.run_until_disconnected()
        print(time.asctime(), '-', 'Stop')

threading.Thread(target=fani).start()
print(time.asctime(), '-', 'Cha Alay')

#if abis == 2 :
#    client.disconnect()
#    clien.disconnect()
