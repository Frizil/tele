import time
import asyncio
import sys
import random

from telethon import TelegramClient, events, utils, Button

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input('Akun : ')

mese = '/gbk'
restore = '/restore_max_confirm'
bot_id = "kampungmaifamxbot"
gbkt = '/gbk_Task'
krj = '/gbk_keranjang'

lokasi = {
#G
    "Tempat ini dipenuhi tupai",
    "Dulu sekali seorang petani tinggal",
    "Keberadaan tumbuhan-tumbuhan beracun",
    "Di sini tidak benar-benar ada kelinci",
    "Gua kecil di bagian dasar Gunung",
    "Berlokasi di tepi gunung yang cukup curam",
    "terdapat berbagai macam burung",
    "Taman bunga matahari di kaki Gunung",
    "Area hutan kecil di dasar gunung",
#F
    "Gua ini menyimpan permata-permata",
    "Tempat hidup para monyet",
    "Taman mawar yang dipenuhi mawar",
    "Area subur yang dipenuhi buah-buahan"
}

narasi = {
    "Mendaki gunung memang melelahkan",
    "Gunung ini terlihat tenang",
    "perjalanan panjang pasti akan membuahkan hasil",
    "Saat ini kamu masih berada",
    "Hal-hal ajaib yang ada di hutan",
    "Sudah mulai lelah? Jangan patah semangat",
    "Ada banyak lokasi-lokasi misterius",
    "Kamu mendaki gunung dan menemukan sebuah",
    "Seorang bajak laut terkenal",
    "Tempat-tempat langka",
    "Gunung ini menyimpan kekuatan sihir",
    "Hal paling misterius dari gunung",
    "Meskipun gunung ini sangat tinggi",
    "Sudah merasa berjalan cukup jauh"
}

with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, mese))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text
            
            if any(loc in pesan for loc in lokasi):
                #print(time.asctime(), 'Ketemu Area')
                #time.sleep(2)
                #await event.click(0,0)
                return
            
            if any(nar in pesan for nar in narasi):
                time.sleep(2)
                await event.click(text="Lanjut Mendaki")
                return
      
            
            if "Gunung dipenuhi dengan berbagai" in pesan:
                if pesan.startswith('Keranjang: '):
                    pesan_split = pesan.split(': ')[1].split('/')
                    if len(pesan_split) == 2:
                        try:
                            angka_terisi = int(pesan_split[0])
                            angka_total = int(pesan_split[1])
                
                            # Memeriksa apakah angka terisi sama dengan angka total
                            if angka_terisi == angka_total:
                                time.sleep(2)
                                await event.respond(krj)
                
                        except ValueError:
                            print("Format angka tidak valid")
                    else:
                        print("Format pesan tidak sesuai")
                
                else:
                  time.sleep(2)
                  await event.click(text="Mulai Mendaki")
                return
              

            if "Kamu tidak memiliki cukup energi" in pesan:
                time.sleep(2)
                await event.respond(restore)
                return
            
            if "Energi berhasil" in pesan:
                time.sleep(2)
                await event.respond(mese)
                return
              
            if "Keranjang kamu sudah penuh!!" in pesan:
                print(time.asctime(), pesan)
                time.sleep(2)
                await event.respond(krj)
                return
              
            if "🧺 Keranjang - GunungBelakangKebun" in pesan:
                if "Silakan turun gunung terlebih dahulu" in pesan:
                    time.sleep(2)
                    await event.respond(mese)
                    
                if "Berhasil mengirim ke barang:" in pesan:
                    time.sleep(2)
                    await event.respond(mese)
                    
                else:
                    time.sleep(2)
                    await event.click(0,0)
                
            
            elif "dan berhasil mendapat" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
              
            elif "tidak ada permata berharga" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
              
            elif "Gua kecil di bagian dasar Gunung" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
            
            elif "Tunggu pancing dengan seksama" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
              
            elif "Kamu menarik alat pancing namun sayang" in pesan:
                time.sleep(10)
                await event.click(0,0)
                return
              
            elif "Kamu melempar kembali alat pancingmu" in pesan:
                time.sleep(10)
                await event.click(0,0)
                return
              
            elif "hanya bisa mendaki sampai ketinggian" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
              
            elif "namun sayang sekali belum menemukan apa-apa" in pesan:
                time.sleep(2)
                await event.click(0,0)
                return
              
            elif "apa kamu ingin turun gunung?" in pesan:
                time.sleep(2)
                await event.click(text="Turun")
                return


client.start()
print(time.asctime(), '-', 'Started')
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')
