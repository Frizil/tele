from telethon import TelegramClient, events, utils, Button
import time, os, asyncio, sys, re, random, logging
from time import strftime
logging.basicConfig(level=logging.ERROR)

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input('Mau sesi mana = ')

gbk = '/gbk_jelajah'
restore = '/restore_max_confirm'
bot_id = "KampungMaifamBot"
#bot_id = 5199147926
#bot_id = "heliavan"
#grup = "heliavan"
krj = '/gbk_keranjang'
tsk = '/gbk_Task'
tskg = '/gbk_task_G'

narasi_gbk = {
    "memang melelahkan",
    "Gunung ini terlihat tenang",
    "Semangat, perjalanan panjang",
    "Saat ini kamu masih berada",
    "Hal-hal ajaib yang ada",
    "Sudah mulai lelah?",
    "Ada banyak lokasi-lokasi",
    "menemukan sebuah"
}

narasi_1 = "Tempat ini dipenuhi tupai" #area_Tupai
narasi_2 = "Dulu sekali seorang" #kebun_terbengkalai
narasi_3 = "tidak benar-benar ada kelinci" #lubang_kelinci_raksasa
narasi_4 = "tumbuhan-tumbuhan beracun" #gua_beracun
narasi_5 = "Ikan-ikan kecil hidup" #kolam_kecil
narasi_6 = "Gua kecil di bagian dasar" #gua_gibi
narasi_7 = "Taman bunga matahari" #taman_matahari
narasi_8 = "mayoritas berwarna merah" #kebun_merah
narasi_9 = "terdapat berbagai macam burung" #surga_burung

area_tupai = {
    "BerryBiasa[A]", "BerryBiasa[B]", "BerryBiasa[C]", "BerryBiasa[D]", "BerryLiar[B]", "BerryLiar[C]", "KacangOak", "KacangOak[A]", "KacangOak[B]", "KacangOak[C]", "KacangOak[D]", "KacangOak[E]", "Pisang", "Pisang[A]", "Pisang[B]", "Pisang[C]", "Pisang[D]", "Pisang[E]"
}

kebun_terbengkalai = {
    "Apel[A]", "Apel[B]", "Apel[C]", "Apel[D]", "Apel[E]", "BerryBiasa", "BerryBiasa[E]", "BerryLiar", "BerryLiar[D]", "BerryLiar[E]", "JamurBiasa", "JamurBiasa[C]", "JamurBiasa[D]", "JamurBiasa[E]", "Tomat", "Tomat[A]", "Tomat[B]", "Tomat[C]", "Tomat[D]", "Tomat[E]", "Tomat[S]"
}

lubang_kelinci_raksasa = {
    "KacangTanah", "KacangTanah[A]", "KacangTanah[B]", "KacangTanah[C]", "KacangTanah[D]", "KacangTanah[E]", "KacangTanah[S]", "Kentang", "Kentang[A]", "Kentang[B]", "Kentang[C]", "Kentang[D]", "Kentang[E]", "Kentang[S]", "Mentimun", "Mentimun[A]", "Mentimun[B]", "Mentimun[C]", "Mentimun[D]", "Mentimun[E]", "Mentimun[S]", "Wortel", "Wortel[A]", "Wortel[B]", "Wortel[C]", "Wortel[D]", "Wortel[E]", "Wortel[S]"
}

gua_beracun = {
    "JamurBeracun", "JamurBeracun[C]", "JamurBeracun[D]", "JamurBeracun[E]"
}

kolam_kecil = {
    "GuramiKecil", "GuramiKecil[C]", "GuramiKecil[D]", "GuramiKecil[E]", "KoiKecil", "MujairKecil", "MujairKecil[C]", "MujairKecil[D]", "MujairKecil[E]"
}

gua_gibi = {
    "Batu", "BatuBara", "BatuBara[D]", "BatuBara[E]", "Batu[D]", "Batu[E]", "BatuKerikil", "BatuKerikil[D]", "BatuKerikil[E]", "Nikel", "Nikel[D]", "Nikel[E]"
}

taman_matahari = {
    "BungaMatahari", "BungaMatahari[A]", "BungaMatahari[B]", "BungaMatahari[C]", "BungaMatahari[D]", "BungaMatahari[E]", "BungaMatahari[S]", "BungaMatahari[SS]", "BungaMatahari[SSS]"
}

kebun_merah = { 
    "Apel", "Apel[B]", "Apel[C]", "Apel[D]", "Apel[E]", "Strawberry", "Strawberry[B]", "Strawberry[C]", "Strawberry[D]", "Strawberry[E]", "Tomat", "Tomat[B]", "Tomat[C]", "Tomat[D]", "Tomat[E]" 
}

surga_burung = {
    "Apel[A]", "Apel[B]", "Apel[S]", "Avokad[A]", "Avokad[B]", "Avokad[S]", "Pisang[A]", "Pisang[B]", "Pisang[S]", "TelurBurungHantu", "TelurBurungUnta", "TelurElang", "TelurGagak", "TelurKakakTua", "TelurMerak", "TelurPhoenix", "TelurPuyuh"
}

jalan = narasi_gbk

ch = -1001522767385
#ch = "heliavan"

emoji_list = ['🌻','🍄','🍌','🌰','🥜','🍎','🍓', '🍅','▪️'] 
full_emoji = ['🌻', '🍄', '🍌', '🌰', '🥜', '🍎', '🍓', '🍅', '▪️', '🥒', '🥕', '🥔', '🐟', '🥚']
jumlah = 0
misi = []
narasi = []
tugas = []
klem = []
jenis_tugas = []
tasks = []


with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, tskg))
    @client.on(events.NewMessage(from_users=bot_id))
    async def handler(event):
        pesan = event.raw_text
        global misi, jumlah, jenis_tugas, jenis_tugas_awal, jumlah_awal, narasi_awal, progres_awal, tasks
        
        if "Selesaikan tugas-tugas" in pesan:
            if "Tidak ada tugas" in pesan:
                print('-' * 30)
                print("Tidak ada tugas yang sedang diambil. Menanggapi dengan tugas baru.")
                print('-' * 30)
                time.sleep(2.0)
                await event.respond(tskg)
            if "Ongoing Task" in pesan:
                time.sleep(2)
                print('-' * 30)
                print("Kondisi Ongoing Task terpenuhi")
                print('-' * 30)
                # Pola regex untuk mengekstrak informasi tugas dengan grade
                pola_tugas_grade = r'([A-Za-z]+)\[([A-Z]+)\] \((\d+)/(\d+)\)\n⏱ (.+?)\n'
                # Pola regex untuk mengekstrak informasi tugas tanpa grade
                pola_tugas_tanpa_grade = r'([A-Za-z]+) \((\d+)/(\d+)\)\n⏱ (.+?)\n'
                # Mencocokkan pola regex dengan pesan untuk mengekstrak informasi tugas dengan grade
                tasks_with_grade = re.findall(pola_tugas_grade, pesan)
                # Mencocokkan pola regex dengan pesan untuk mengekstrak informasi tugas tanpa grade
                tasks_without_grade = re.findall(pola_tugas_tanpa_grade, pesan)
            
                # Menampilkan informasi tugas dengan grade
                if tasks_with_grade:
                    print('-' * 30)
                    print("Tersedia tugas dengan grade:")
                    print('-' * 30)
                    for task in tasks_with_grade:
                        tasks.append(task)
                        #print("Menambahkan tugas dengan grade:", task)  # Tampilkan nilai yang di-append
                        jenis_tugas = f"{task[0]}[{task[1]}]"
                        total = task[3]
                        progress = task[2]
                        print(f"Jenis tugas: {jenis_tugas}")
                        print(f"Total: {total}x")
                        print(f"Progress: {progress}")
                        print('-' * 30)
                
                # Menampilkan informasi tugas tanpa grade
                if tasks_without_grade:
                    print('-' * 30)
                    print("Tersedia tugas tanpa grade:")
                    print('-' * 30)
                    for task in tasks_without_grade:
                        jenis_tugas = task[0]
                        total = task[2]
                        progress = task[1]
                        tasks.append((jenis_tugas, "", progress, total, ""))  # Menambahkan dengan format yang sesuai
                        #print("Menambahkan tugas tanpa grade:", task)  # Tampilkan nilai yang di-append
                        print(f"Jenis tugas: {jenis_tugas}")
                        print(f"Total: {total}x")
                        print(f"Progress: {progress}")
                        print('-' * 30)
                
                # Pastikan setiap tuple dalam tasks memiliki panjang yang sama
                tasks_with_grade = [(task[0], task[1], task[2], task[3], task[4]) for task in tasks_with_grade]
                tasks_without_grade = [(task[0], task[1], task[2], task[3], "") for task in tasks_without_grade]
                
                # Mengurutkan tugas berdasarkan waktu
                tasks_sorted = sorted(tasks, key=lambda x: x[4])
                
                narasi = None  # Variabel narasi didefinisikan di luar loop
                
                #Menampilkan informasi tugas
                for task in tasks_sorted:
                    jenis_tugas = task[0]
                    total = task[3]
                    progress = task[2]
                    
                    # Menentukan narasi berdasarkan jenis tugas
                    if jenis_tugas in area_tupai:
                        narasi = narasi_1
                    elif jenis_tugas in kebun_terbengkalai:
                        narasi = narasi_2
                    elif jenis_tugas in lubang_kelinci_raksasa:
                        narasi = narasi_3
                    elif jenis_tugas in gua_beracun:
                        narasi = narasi_4
                    elif jenis_tugas in kolam_kecil:
                        narasi = narasi_5
                    elif jenis_tugas in gua_gibi:
                        narasi = narasi_6
                    elif jenis_tugas in taman_matahari:
                        narasi = narasi_7
                    elif jenis_tugas in kebun_merah:
                        narasi = narasi_8
                    elif jenis_tugas in surga_burung:
                        narasi = narasi_9
                    else:
                        narasi = '⛰ Gunung Belakang Kebun ⛰'
                    
      
                # Menentukan narasi_awal, jenis_tugas_awal, jumlah_awal, dan progres_awal
                narasi_awal = narasi
                jumlah_awal = total
                progres_awal = progress
                
                # Memulai mengerjakan tugas yang paling awal
                #print("Isi list tasks setelah semua operasi append:")
                #print(tasks)
                narasi_awal = None
                
                first_task = tasks_sorted[0]
    
                # Menentukan nilai jenis_tugas_awal, jumlah_awal, dan progres_awal
                if first_task[1] == '':
                    #mengecek index ke 1 dalam list append tasks
                    jenis_tugas_awal = f"{first_task[0]}"
                    jumlah_awal = first_task[3]
                    progres_awal = first_task[2]
                    
                else:
                    jenis_tugas_awal = f"{first_task[0]}[{first_task[1]}]"
                    jumlah_awal = first_task[3]
                    progres_awal = first_task[2]
                    
                # Mengatur narasi dengan narasi dari tugas pertama
                if jenis_tugas_awal in area_tupai:
                    narasi_awal = narasi_1
                elif jenis_tugas_awal in kebun_terbengkalai:
                    narasi_awal = narasi_2
                elif jenis_tugas_awal in lubang_kelinci_raksasa:
                    narasi_awal = narasi_3
                elif jenis_tugas_awal in gua_beracun:
                    narasi_awal = narasi_4
                elif jenis_tugas_awal in kolam_kecil:
                    narasi_awal = narasi_5
                elif jenis_tugas_awal in gua_gibi:
                    narasi_awal = narasi_6
                elif jenis_tugas_awal in taman_matahari:
                    narasi_awal = narasi_7
                elif jenis_tugas_awal in kebun_merah:
                    narasi_awal = narasi_8
                elif jenis_tugas_awal in surga_burung:
                    narasi_awal = narasi_9
                else:
                    print("\nJenis item tidak ditemukan di dalam area")
                    narasi_awal = '⛰ Gunung Belakang Kebun ⛰'
      
                tugas_awal = f"""
__{time.strftime('%x - %X %Z')}__
----- ○ ----- ○ ----- ○ ----- ○ ----- ○ -----
Mulai mengerjakan tugas
➱ jenis_tugas = {jenis_tugas_awal}
➱ jumlah = {jumlah_awal}x
➱ progres = {progres_awal}
➱ narasi = {narasi_awal}
Selamat menyelesaikan tugas!!
----- ○ ----- ○ ----- ○ ----- ○ ----- ○ -----"""
                time.sleep(2)
                print(tugas_awal)
                time.sleep(2)
                await client.send_message(bot_id, gbk)
                
        if "Berikut adalah daftar Tugas" in pesan:
            misi = []
            #print()
            z = [i for i in pesan.split("\n\n") if any(loc in i for loc in emoji_list)]
            for x in z:
                koin_list = None
                koin_split = [i for i in x.split("\n") if "🎁 Koin:" in i]
                if koin_split:
                    koin = koin_split[0].split()
                    if len(koin) >= 3:
                        try:
                            koin_list = int(koin[2].replace("🪙", ""))
                        except ValueError:
                            pass  # Menangani jika koin tidak bisa dikonversi ke integer
                
                exp_list = None
                exp_split = [i for i in x.split("\n") if "🎁 EXP:" in i]
                if exp_split:
                    exp = exp_split[0].split()
                    if len(exp) >= 3:
                        try:
                            exp_list = int(exp[2].replace("❇️", ""))
                        except ValueError:
                            pass  # Menangani jika exp tidak bisa dikonversi ke integer
                
                misi_split = [i for i in x.split("\n") if "🗒" in i]
                if misi_split:
                    misi_list = misi_split[0].split()[1]
                    misi.append({"koin_list": koin_list, "exp_list": exp_list, "misi_list": misi_list})
            
            #KALAU MAU CARI KOIN TERBANYAK
            #def get_koin(misi):
                #return misi.get("koin_list")
            #misi.sort(key=get_koin, reverse=True)
            
            #KALAU MAU CARI EXP TERBANYAK
            def get_exp(misi):
                return misi.get("exp_list")
            misi.sort(key=get_exp, reverse=True)
            time.sleep(1.5)
            await event.respond(misi[0].get("misi_list"))
            return
        
        if "Berhasil menyelesaikan tugas" in pesan:
            print('\n'+'-'*30+f"\nTugas sudah di selesaikan\n"+'-'*30)
            tasks.clear()
            time.sleep(2)
            await client.forward_messages(ch, event.message)
            time.sleep(2)
            await event.respond(tskg)
            return
        
        elif any(loc in pesan for loc in jalan):
            time.sleep(1.5)
            await event.click(0,0)
            return
        
        elif "Tugas tidak ditemukan" in pesan or "silakan pilih tugas lain" in pesan:
            time.sleep(1.5)
            await event.respond(tskg)
            return
        
        elif "Gunung dipenuhi" in pesan:
            time.sleep(1.5)
            await event.respond(krj)
            return
          
        elif "Kamu tidak memiliki cukup energi" in pesan:
            time.sleep(1.5)
            await event.respond(restore)
            return
        
        elif "Energi berhasil" in pesan:
            time.sleep(1.5)
            await event.respond(tsk)
            return
        
        elif 'ingin turun gunung' in pesan or "tidak bisa mengambil tugas" in pesan or "hanya bisa mendaki" in pesan:
            time.sleep(1.5)
            await event.click(text='Turun')
            return
          
        elif "Keranjang kamu sudah penuh!!" in pesan:
            time.sleep(1.5)
            await event.respond('/gbk')
            return
        
        elif "🧺 Keranjang - GunungBelakangKebun" in pesan:
            if "Silakan turun gunung terlebih dahulu" in pesan:
                time.sleep(1.5)
                await event.respond('/gbk')
            if "Berhasil mengirim ke barang:" in pesan:
                time.sleep(1.5)
                await event.respond(tskg)
            if "kamu kosong" in pesan:
                time.sleep(1.5)
                await event.respond(tskg)
            else:
                time.sleep(1.5)
                await event.click(text='Kirim ke Barang')
            return
        
        elif "Kamu masih memiliki 3 tugas aktif untuk dikerjakan" in pesan:
            time.sleep(2)
            await event.respond(tsk)
            return
          
        elif "Berhasil mengambil tugas dengan ID" in pesan:
            jenis_tugas = None
            for emoji in emoji_list:
                if emoji in pesan:
                    jenis_tugas = pesan.split(emoji,1)[1].split()[0]
                    break
            tugass = re.findall(r'dapatkan (\D+) sebanyak', pesan)
            klems = re.findall(r'sebanyak (\d+) kali', pesan)
            for tugas in tugass:
                tugas=str(tugass[0])
            for klem in klems:
                klem=int(klems[0])
            if jenis_tugas:
                if jenis_tugas in area_tupai:
                    narasi = narasi_1
                elif jenis_tugas in kebun_terbengkalai:
                    narasi = narasi_2
                elif jenis_tugas in lubang_kelinci_raksasa:
                    narasi = narasi_3
                elif jenis_tugas in gua_beracun:
                    narasi = narasi_4
                elif jenis_tugas in kolam_kecil:
                    narasi = narasi_5
                elif jenis_tugas in gua_gibi:
                    narasi = narasi_6
                elif jenis_tugas in taman_matahari:
                    narasi = narasi_7
                elif jenis_tugas in kebun_merah:
                    narasi = narasi_8
                elif jenis_tugas in surga_burung:
                    narasi = narasi_9
                else:
                    narasi = '⛰ Gunung Belakang Kebun ⛰'
            ambil_tugas = f"""
__{time.strftime('%x - %X %Z')}__
----- ○ ----- ○ ----- ○ ----- ○ ----- ○ -----
+Berhasil mengambil tugas 
➱ jenis_tugas = {tugas}
➱ jumlah = {klem}x 
➱ koin pendaki = {misi[0].get("koin_list")}🪙
➱ exp pendaki = {misi[0].get("exp_list")}❇️
➱ 🗒 {misi[0].get("misi_list")}
➱ narasi = {narasi}
----- ○ ----- ○ ----- ○ ----- ○ ----- ○ -----"""
            time.sleep(2)
            print(ambil_tugas)
            #print('\n'+pesan)
            time.sleep(2)
            await event.respond(tskg)
            return
        
          
        if "berhasil mendapat" in pesan:
            pola_item = pesan.splitlines()[4].split('berhasil mendapat')[1]
            pola_item = None
            for emoji in full_emoji:
                if emoji in pesan:
                    hasil_item = pesan.split(emoji,1)[1].split()[0]
            if hasil_item == jenis_tugas_awal: 
                jumlah+=1
                print(f"\n{time.strftime('%X')} - Progres {jenis_tugas_awal} = {jumlah}")
                if jumlah >= int(jumlah_awal):
                    time.sleep(2.0)
                    await event.respond('/gbk_task')
                    jumlah = 0
                    print('\nMisi selesai. Yuk cari misi lagi!')
                else:
                    time.sleep(1.5)
                    await event.click(0, 0)
            if hasil_item != jenis_tugas_awal:
                time.sleep(1.5)
                await event.click(0, 0)
            return
        
        elif "belum menemukan apa-apa" in pesan:
            time.sleep(1.5)
            await event.click(0,0)
            return
        
        elif '- GBK ⛰' in pesan:
            narasi = narasi_awal
            if narasi in pesan:
                print('\n'+'-'*30)
                print(f"narasi {narasi} di temukan")
                print('-' * 30)
                time.sleep(1.5)
                await event.click(0,0)
                return
            else:
                time.sleep(1.5)
                await event.click(1,0)
                return
            return
          
        
        elif 'EXP terpenuhi!! Level pendaki meningkat!!' in pesan:
            print('\n'+'-'*30+f"\nNaik Level Dik\n"+'-'*30)
            time.sleep(1.5)
            await client.forward_messages(ch, event.message)
            time.sleep(1.5)
            await event.respond(tskg)
            return
        
    client.start()
    print(time.asctime(), '-', 'Mulai')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Berhenti')