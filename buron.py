import asyncio
import sys
import re
import time
from telethon import TelegramClient, events

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_fil = input('Siapa: ')

cabang = "/mg24_game_Mencuri_46"
jenis = "_curibarang"
hapus = "/mg2024_hapusBuronan"
rumah = "/mg2024_RumahWarga"
i = 0
#bot = 'catlovy'
bot = 'KampungMaifamBot'
alamat = []  
beli = "/mg2024_shop_5000"

async def main():
    async with TelegramClient(sesi_fil, api_id, api_hash) as clien:
        await clien.send_message(bot, cabang)
        
        @clien.on(events.NewMessage(from_users=bot))
        async def handler(event):
            global i, alamat
            pesan = event.raw_text
            
            if "bisa saja polisi menangkap dan memenjarakanmu" in pesan:
                alamat.clear() 
                i = 0
                print('=' * 30)
                print('Kondisi Muncul alamat')
                print('=' * 30)
                baris = pesan.split('\n')
                for baris_teks in baris:
                    if '/mg2024_x_' in baris_teks:
                        alamat.append(baris_teks.strip()) 
                print(alamat) 
                await asyncio.sleep(1.5)
                if alamat:
                    
                    await asyncio.sleep(1.5)
                    await event.respond((alamat[i].replace('🏘', '')) + str(jenis))
                return

            if "Berhasil mencuri" in pesan:
                print('=' * 30)
                print('Kondisi Berhasil Mencuri')
                print('=' * 30)
                i += 1
                if 1 <= i <= 2:
                    await asyncio.sleep(1.5)
                    await event.respond(hapus)
                elif 3 <= i <= 5:
                    await asyncio.sleep(1.5)
                    await event.respond(hapus)
                return
              
            if "Apa kamu yakin ingin menghapus" in pesan:
                print('=' * 30)
                print('Konfirmasi Penghapusan Buron')
                await asyncio.sleep(1.5)
                await event.click(text="Confirm")
                return
            
            if "Harga buronan dihapus" in pesan or "Saat ini kamu bersih" in pesan or "Kamu tidak memiliki uang" in pesan:
                print('=' * 30)
                print('Kondisi Buron di hapus / Tidak ada buron')
                print('=' * 30)
                #if i >= 5:
                    #await asyncio.sleep(1.5)
                    #await event.respond(beli)
                if i >= 5:
                    await asyncio.sleep(1.5)
                    await event.respond(rumah)
                elif alamat and i < len(alamat):
                    await asyncio.sleep(1.5)
                    await event.respond((alamat[i].replace('🏘', '')) + str(jenis))
                return
            
            #if "Berhasil membeli 5000 KemampuanMencuri" in pesan:
                #await asyncio.sleep(1.5)
                #await event.respond(beli)
                #return
            
            #if "Uang tidak mencukupi" in pesan:
                #await asyncio.sleep(1.5)
                #await event.respond(rumah)
                #return
                
            if "Kumpulkan poin sebanyak-banyaknya" in pesan or "Permainan dimulai" in pesan:
                print('=' * 30)
                print('Kumpulkan poin sebanyak-banyaknya / Permainan dimulai')
                print('=' * 30)
                await asyncio.sleep(1.5)
                await event.respond(rumah)
                return
              
            if "Polisi menemukanmu" in pesan:
                print('=' * 30)
                print('Kondisi Di Tangkap Polisi')
                print('=' * 30)
                
                words = pesan.split()
                
                index = words.index('menit')
                
                captured_value = words[index - 1]
                
                if captured_value:
                    durasi_penjara = int(captured_value)
                    print("Durasi penjara:", durasi_penjara, "menit")
                    
                    detik = durasi_penjara * 60
                    print("Durasi penjara dalam detik:", detik)
                    
                    await asyncio.sleep(detik)
                    
                    if alamat and i < len(alamat):
                        print('=' * 30)
                        print('Lanjut Mencuri')
                        print('=' * 30)
                        
                        await asyncio.sleep(1.5)
                        await event.respond((alamat[i].replace('🏘', '')) + str(jenis))
                return
                        
        print(time.asctime(), '-', 'Mulai')
        await clien.run_until_disconnected()
        print(time.asctime(), '-', 'Berhenti')

asyncio.run(main())