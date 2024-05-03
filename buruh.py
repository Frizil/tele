import time, asyncio, sys, random, re
import logging
from telethon import TelegramClient, events, utils, Button

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input("Akun : ")

#bot
print("\ncontoh: Angka = 2")
print("Pilih bot yng digunakan")
mpm = input("\tKetik 1 untuk Bot Alpha\n\tKetik 2 untuk Bot X\n\tKetik 3 untuk Bot X4\n   Angka = ")
if mpm == '1':
    bot_id = 'KampungMaifamBot'
elif mpm == '2':
    bot_id = 'KampungMaifamXBot'
elif mpm == '3':
    bot_id = 'KampungMaifamX4Bot'
    
#bot_id = 1396547380

total_pabrik = int(input("Masukkan jumlah total pabrik : "))
daftar_pabrik = []

for i in range(total_pabrik):
    daftar_id = int(input(f"Masukkan ID pabrik ke-{i+1} : "))
    daftar_pabrik.append(daftar_id)

skill_min = int(input("Masukkan batas minimum skill : "))
uang_max = int(input("Masukkan batas maksimum uang : "))


i = 0

id_pabrik = daftar_pabrik[i]
#cmd = f"/md2024_rekrut_{str(id_pabrik)}"
cmd = f"/md2024_pabrik_{id_pabrik}"

data_rekrut = []
data_perpanjang = []
md = "/md2024"

logging.basicConfig(level=logging.ERROR)

boleh = False

lanjut = 0

with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, cmd))

    @client.on(events.NewMessage(from_users=bot_id))
    async def handler(event):
        global data_rekrut, id_pabrik, cmd, data_perpanjang, md, i, daftar_pabrik, boleh
        pesan = event.raw_text
        
        if "Rekrut buruh pekerja untuk Pabrik" in pesan:
            data_rekrut.clear() 
            id_pabrik = daftar_pabrik[i]
            narasi = pesan
            pola = r'👷‍♂️ (\w+) - (\d+) SKILL\n➕ (\/md2024_rekrut_\d+_\d+) - (\d+(?:,\d+)?)💰'
            matches = re.findall(pola, pesan)
            if matches:
                for match in matches:
                    nama = match[0]
                    skill = int(match[1])
                    rekrut = match[2]
                    uang = int(match[3].replace(',', ''))
                    if skill >= skill_min and uang <= uang_max:
                        data_rekrut.append((nama, skill, rekrut, uang))
                    else:
                        data_rekrut.append((0,0,0,0))
                        
                #mengurutkan data berdasarkan skill tertinggi
                data_sorted = sorted(data_rekrut, key=lambda x: x[1], reverse=True)
                
                #kalau mau ganti bisa mengurutkan data berdasarkan uang terendah
                #data_sorted = sorted(data, key=lambda x: x[3], reverse=False)
                ambil = data_sorted[0]
                if ambil[1] != 0:
                    time.sleep(1.5)
                    await client.send_message(bot_id, ambil[2])
                    #print(ambil)
                if ambil[1] == 0:
                    data_rekrut.clear()
                    cmd = f"/md2024_rekrut_{str(id_pabrik)}"
                    time.sleep(2.5)
                    await client.send_message(bot_id, cmd)
            return
          
        if "Apa kamu yakin ingin merekrut" in pesan:
            print(time.asctime(), 'Rekrut')
            klik = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(0.5)
            await klik.click(text='Confirm')
            return
          
        if "Berhasil merekrut" in pesan or "Kamu hanya bisa merekrut" in pesan:
            print(time.asctime(), 'Jeda')
            data_rekrut.clear() 
            time.sleep(58)
            await client.send_message(bot_id, cmd)
            return
          
        if "Pekerja dengan ID" in pesan or "Kamu tidak bisa merekrut buruh" in pesan:
            print(time.asctime(), 'Pekerja Tidak Ditemukan')
            data_rekrut.clear()
            time.sleep(2.5)
            await client.send_message(bot_id, cmd)
            return
             

        if "Kamu memerlukan" in pesan:
            i = 0
            id_pabrik = daftar_pabrik[i]
            print(time.asctime(), 'Habis Duit')
            cmd = f"/md2024_pabrik_{id_pabrik}"
            time.sleep(2.5)
            await client.send_message(bot_id, cmd)
            return
          
        if "Tingkatkan Level Pabrik untuk" in pesan:
            data_perpanjang.clear() 
            id_pabrik = daftar_pabrik[i]
            pola_perpanjang = r'/md2024_(\w+)_(\w+) \((\w+ \w+)\)'
            matches = re.findall(pola_perpanjang, pesan)
            
            pola_hasil = r"Kapasitas Pekerja: \((\d+)/(\d+)\)\nKapasitas Produksi: \((\d+)/(\d+)\)"
            match_hasil = re.search(pola_hasil, pesan)
            
            if matches:
                for match in matches:
                    jenis = match[0].replace('b', 'perpanjang')
                    nama = match[1]
                    kontrak = match[2]
                    if kontrak == "kontrak berakhir":
                        data_perpanjang.append((jenis, nama, kontrak))
                    
                if "kontrak berakhir" in kontrak: 
                    perpanjang = data_perpanjang[0]
                    time.sleep(2.5)
                    await client.send_message(bot_id, f"/md2024_{perpanjang[0]}_{perpanjang[1]}_1")
                    
                if "kontrak berakhir" not in kontrak: 
                    print(time.asctime(), 'Ambil Hasil')
                    klik = await client.get_messages(bot_id, ids=event.message.id)
                    time.sleep(2.5)
                    await klik.click(text='AmbilHasil')
                    
                        
            if match_hasil and not matches:
                total_pekerja = int(match_hasil.group(1))
                total_produksi = int(match_hasil.group(3))
                
                if total_pekerja == 0 and total_produksi == 0:
                    id_pabrik = daftar_pabrik[i]
                    cmd = f"/md2024_rekrut_{str(id_pabrik)}"
                    print(time.asctime(), 'Rekrut')
                    time.sleep(2.5)
                    await client.send_message(bot_id, cmd)
                
                else:
                    if boleh == True:
                        id_pabrik = daftar_pabrik[i]
                        cmd = f"/md2024_rekrut_{str(id_pabrik)}"
                        print(time.asctime(), 'Rekrut')
                        time.sleep(2.5)
                        await client.send_message(bot_id, cmd)
                    if boleh == False:
                        print(time.asctime(), 'Ambil Hasil')
                        klik = await client.get_messages(bot_id, ids=event.message.id)
                        time.sleep(2.5)
                        await klik.click(text='AmbilHasil')
                    
            return
        
        if "Apa kamu yakin ingin memperpanjang" in pesan:
            print(time.asctime(), 'perpanjang')
            klik = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(1)
            await klik.click(text='Confirm')
            return
          
        if "diperpanjang dan akan berakhir" in pesan:
            print(time.asctime(), 'Berhasil Memperpanjang')
            id_pabrik = daftar_pabrik[i]
            data_perpanjang.clear()
            cmd = f"/md2024_pabrik_{id_pabrik}"
            time.sleep(2.5)
            await client.send_message(bot_id, cmd)
            return
            
        if "Berhasil mengambil Hasil Produksi" in pesan:
            print(time.asctime(), 'Berhasil Ambil Hasil')
            cmd = f"/md2024_HasilProduksi"
            time.sleep(2.5)
            await client.send_message(bot_id, cmd)
            return
            
        if "Hasil produksi dari semua" in pesan:
            print(time.asctime(), 'Jual Hasil')
            klik = await client.get_messages(bot_id, ids=event.message.id)
            time.sleep(1)
            await klik.click(text='Confirm')
            return
          
        
        if "Berhasil menjual semua hasil" in pesan:
            boleh = True
            id_pabrik = daftar_pabrik[i]
            cmd = f"/md2024_pabrik_{str(id_pabrik)}"
            print(time.asctime(), 'Berhasil Jual Hasil')
            time.sleep(2.5)
            await client.send_message(bot_id, cmd)
            return
        
        if "Kapasitas pabrik sudah penuh" in pesan:
            i += 1
            boleh = False
            if i < len(daftar_pabrik):
                id_pabrik = daftar_pabrik[i]
                cmd = f"/md2024_pabrik_{id_pabrik}"
                print(time.asctime(), 'Pabrik Penuh, beralih ke pabrik selanjutnya')
                time.sleep(2.5)
                await client.send_message(bot_id, cmd)
            else:
                i = 0
                boleh = False
                print(time.asctime(), 'Semua pabrik penuh, tidak dapat melanjutkan operasi')
                time.sleep(58)
                await client.send_message(bot_id, cmd)
            return
          
                      
    client.start()
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Berhenti')