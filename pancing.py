import time
import asyncio
import sys, re
from telethon import TelegramClient, events, utils
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input("Akun : ")
loop = asyncio.new_event_loop()

#bot
print("\nPilih bot yng digunakan")
print("Contoh: Angka = 2")
mpm = input("\tKetik 1 untuk Bot Alpha\n\tKetik 2 untuk Bot X\n\tKetik 3 untuk Bot X4\n   Angka = ")
if mpm == '1':
    bot_id = 'KampungMaifamBot'
elif mpm == '2':
    bot_id = 'KampungMaifamXBot'
elif mpm == '3':
    bot_id = 'KampungMaifamX4Bot'
    
#tempat mancing
print("\nPilih tempat mancing")
pilih = input('\tKetik 1 untuk 💦 Lala\n\tKetik 2 untuk 💦 Mimi\n\tKetik 3 untuk 💦 Badabu\n\tKetik 4 untuk 🏝 Soprano\n\tKetik 5 untuk 💧 Bulari\n\tKetik 6 untuk 🌊 Narrow/Sempit\n\tKetik 7 untuk 🌊 Gabagaba\n\tKetik 8 untuk 🌊 Ancient/Purba\n\tKetik 9 untuk 🌊 Haunted/Berhantu\n\tKetik 10 untuk 🌊 All\n\tKetik 11 untuk 💦 Danau Penjara\n   Angka =  ')
if pilih == '1': 
    tempat = 'Lala River' 
elif pilih == '2': 
    tempat = 'Mimi River' 
elif pilih == '3': 
    tempat = 'Badabu River' 
elif pilih == '4': 
    tempat = 'Soprano Lake' 
elif pilih == '5': 
    tempat = 'Bay of Bulari' 
elif pilih == '6': 
    tempat = 'Narrow Sea'
elif pilih == '7': 
    tempat = 'Gabagaba Ocean' 
elif pilih == '8': 
    tempat = 'Ancient Sea' 
elif pilih == '9': 
    tempat = 'Haunted Sea'
elif pilih == '10': 
    tempat = 'All Sea'
elif pilih == '11': 
    tempat = 'Danau Penjara'
    
#alat pancing
print("\nPilih jenis alat")
pilih = input('\tKetik 1 untuk 🎣 Pancing\n\tKetik 2 untuk 🎣 Rod\n\tKetik 3 untuk 🕸 Jala\n\tKetik 4 untuk 🕸 Net\n   Angka = ')
if pilih == '1': 
    alat = 'Tarik Alat Pancing' 
elif pilih == '2': 
    alat = 'Pull The Fishing Rod' 
elif pilih == '3': 
    alat = 'Tarik Jala' 
elif pilih == '4': 
    alat = 'Pull The Net' 
    
#narasi di bot
narasi = {
    "Doesn't look like",
    "Sungai dangkal",
    "Legend said a man",
    "Legenda mengatakan",
    "Only big fish",
    "Hanya ikan besar",
    "Rare fish lived",
    "Ikan langka",
    "Well, some little",
    "Terletak di bagian",
    "People claimed that",
    "Orang-orang mengklaim",
    "Many years ago",
    "Bertahun-tahun yang",
    "A dangerous strange",
    "Laut aneh berbahaya",
    "A cursed sea",
    "Laut terkutuk",
    "Here you can",
    "Bagian kecil",
    "The Government",
    "Pemerintah Maikantri",
}
        
tunggu = 1.5
       
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, tempat))
    @client.on(events.NewMessage(from_users=bot_id))
    async def handler(event):
        pesan = event.raw_text
                   
        if any(nar in pesan for nar in narasi):
            ditz = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(tunggu)
            await ditz.click(text=alat)
            return

        if "You've got" in pesan or "Kamu mendapatkan" in pesan:
            time.sleep(tunggu)
            await event.respond(tempat)
            return
        
        if "You've caught" in pesan or "berhasil menangkap" in pesan:
            time.sleep(tunggu)
            await event.respond(tempat)
            return
        
        if "not fishing" in pesan or "tidak sedang memancing" in pesan:
            time.sleep(tunggu)
            await event.respond(tempat)
            return
        
        #if "Your energy is" in pesan or 'Kamu tidak memiliki' in pesan:
            #time.sleep(tunggu)
            #await event.respond("/restore")
            #return
        
        if "Energy Successfully" in pesan or 'Energi berhasil' in pesan:
            time.sleep(tunggu)
            await event.respond(tempat)
            return
        
        if "you can't eat more" in pesan:
            sl = re.findall('\d+', pesan)
            nn = int(sl[0])
            #print(time.asctime(), f'Tunggu {3600-nn*60} detik')
            time.sleep(int(3600-nn*60))
            await event.respond("/eat_rotibelanda")
            return
        
        if "Yummy mummy" in pesan:
            time.sleep(tunggu)
            await event.respond(tempat)
            return
        
client.start()
print()
print(time.asctime(), '-', 'Lesgoo mancing 🎣')
client.run_until_disconnected()
print(time.asctime(), '-', 'Lelah ges')