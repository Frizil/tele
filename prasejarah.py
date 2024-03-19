import time
import asyncio
import sys
import threading
import re
from telethon import TelegramClient, events, utils
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_fil = input('Siapa: ')

count = 0

def fani():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with TelegramClient(sesi_fil, api_id, api_hash, loop=loop) as clien:
        clien.loop.run_until_complete(clien.send_message("kampungmaifambot", '/mg2024_game_Tambang_22'))

        @clien.on(events.NewMessage(from_users="kampungmaifambot"))
        async def handler(event):
            global idMer
            global count
            global angka
            print(event.raw_text)
            print(count)
            
            if "Energi: 72%" in event.raw_text:
                time.sleep(1)
                await event.respond('/mg2024_buff_Energi')
                return
            
            if 'Tunggu 20' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(17.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(17.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(19.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return  
            
            if 'Tunggu 19' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(16.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(16.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(18.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return  
            
            if 'Tunggu 18' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(15.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(15.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(17.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return  
            
            if 'Tunggu 17' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(14.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(14.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(16.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return  
            
            if 'Tunggu 16' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(13.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(13.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(15.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return  
        
            if 'Tunggu 15' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(12.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(12.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(14.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return  
        
            if 'Tunggu 14' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(11.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(11.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(13.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return  
        
            if 'Tunggu 13' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(10.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(10.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(12.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return  
        
            if 'Tunggu 12' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(9.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(9.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(11.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return  
                
            if 'Tunggu 11' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(8.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(8.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(10.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return  
        
            if 'Tunggu 10' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(7.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(7.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(9.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return  
        
            if 'Tunggu 9' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(6.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(6.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(8.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return  
        
            if 'Tunggu 8' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(5.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(5.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(7.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return  
            
            if 'Tunggu 7' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(3.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(3.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(6.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return  
            
            if 'Tunggu 6' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(2.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(2.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(5.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return   
            
            if 'Tunggu 5' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(1.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(1.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(4.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return   

            if 'Tunggu 4' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(1.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(1.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(3.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return        

            if 'Tunggu 3' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(1.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(1.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(2.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return                     

            if 'Tunggu 2' in event.raw_text:
                o = re.findall('\d+', event.raw_text)
                angka = int(o[1])
                count += angka
                if "Energi: 82%" in event.raw_text:
                    time.sleep(1.5)
                    await event.respond('/mg2024_buff_Energi') 
                    return
                elif count >= 1000:
                    time.sleep(1.5)
                    await event.respond('/mg2024_buff_DoublePoint') 
                    return
                else:
                     time.sleep(1.5)
                     msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                     await msg.click(0)
                     return  
                return 

            if 'Kamu memerlukan' in event.raw_text:
                time.sleep(1.5)
                msg = await clien.get_messages(await event.get_sender(),ids = idMer)
                await msg.click(0)
                return                   
                
            if "dari menambang fosil" in event.raw_text:
                time.sleep(1.5)
                await event.click(text='START')
                return
                
            if "Apa kamu yakin ingin" in event.raw_text:
                time.sleep(1)
                await event.click(text='Confirm')
                return
                
            if "Energi dipulihkan menjadi 100%!!" in event.raw_text:
                count -= 150
                time.sleep(1.5)
                await event.respond('/mg2024_buff_Kemampuan')
                return
                
            if "5000 Kemampuan Tambang ditambahkan!!" in event.raw_text:
                count -= 100
                time.sleep(1.5)
                await event.respond('/mg2024_GuaTambang')
                return
                
            if "Buff dibeli!!" in event.raw_text:
                count -= 1000
                time.sleep(1.5)
                await event.respond('/mg2024_GuaTambang')
                return
                
            if "Permainan dimulai" in event.raw_text:
                time.sleep(1)
                await event.respond('/mg2024_GuaTambang')
                return
                
            if 'Tingkatkan kemampuanmu' in event.raw_text:
                idMer = event.id
                time.sleep(1)
                await clien(GetBotCallbackAnswerRequest(
                    peer=await event.get_sender(),
                    msg_id=event.message.id,
                    data=event.message.reply_markup.rows[0].buttons[0].data
                    ))
        

        clien.run_until_disconnected()
        print(time.asctime(), '-', 'Stop')

threading.Thread(target=fani).start()
print(time.asctime(), '-', 'Cha Alay')

#if abis == 2 :
#    client.disconnect()
#    clien.disconnect()
