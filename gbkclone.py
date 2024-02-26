from telethon import TelegramClient, events, utils, Button
import time, os, asyncio, sys, re, random, logging
logging.basicConfig(level=logging.ERROR)

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input('Mau sesi mana = ')

gbk = '/gbk_jelajah'
restore = '/restore_max_confirm'
bot_id = "KampungMaifamBot"
#bot_id = 5199147926
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

emoji_list = ['🌻','🍄','🍌','🌰','🥜','🍎','🍓', '🍅','▪️'] 

jumlah = 0
misi = []
narasi = []
tugas = []
klem = []
jenis_tugas = []

async def handle_task_progress(pesan, jenis_tugas_awal, jumlah_awal):
    # Pola pencarian untuk menemukan jenis item yang berhasil didapat
    pola_item = r"berhasil mendapat ([\w\s\[\]]+)"
    
    # Mencocokkan pola dengan pesan
    match = re.search(pola_item, pesan)
    
    # Jika ditemukan, ekstrak informasi item dan cetak progresnya
    if match:
        item = match.group(1)
        print(f"Progres {item} = 1")
    
    # Memeriksa apakah item yang berhasil didapat sama dengan tugas awal
    if jenis_tugas_awal == item:
        jumlah += 1
        print(f'Progres {jenis_tugas_awal} = {jumlah}')
        if jumlah % jumlah_awal == 0:
            time.sleep(1.5)
            await event.respond('/gbk_task')
            jumlah = 0
            print('Misi selesai. Yuk cari misi lagi!')
        else:
            time.sleep(1.5)
            await event.click(0, 0)
    else:
        time.sleep(1.5)
        await event.click(0, 0)


with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, tskg))
    @client.on(events.NewMessage(from_users=bot_id))
    async def handler(event):
        pesan = event.raw_text
        global misi, jumlah, jenis_tugas, jenis_tugas_awal, jumlah_awal, narasi_awal, progres_awal
        
        if "Selesaikan tugas-tugas" in pesan:
            if "Tidak ada tugas" in pesan:
                print("Tidak ada tugas yang sedang diambil. Menanggapi dengan tugas baru.")
                time.sleep(2.0)
                await event.respond(tskg)
            if "Ongoing Task" in pesan:
                print("Kondisi Ongoing Task terpenuhi.")
                # Pola regex untuk mengekstrak informasi tugas
                pola_tugas = r'([A-Za-z]+)\[([A-Z])\] \((\d+)/(\d+)\)\n⏱ (.+?)\n'

                # Mencocokkan pola regex dengan pesan untuk mengekstrak informasi tugas
                tasks = re.findall(pola_tugas, pesan)
                
                # Mengurutkan tugas berdasarkan waktu
                tasks_sorted = sorted(tasks, key=lambda x: x[4])
                
                narasi = None  # Variabel narasi didefinisikan di luar loop
                
                # Menampilkan informasi tugas
                for task in tasks_sorted:
                    jenis_tugas = f"{task[0]}[{task[1]}]"
                    total = task[3]
                    progress = task[2]
                
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
                            print("Jenis item tidak ditemukan di dalam area")
                            break
                
                    print('-' * 30)
                    print("Tersedia tugas")
                    print(f"jenis_tugas = {jenis_tugas}")
                    print(f"jumlah = {total}x")
                    print(f"progres = {progress}")
                    print(f"narasi = {narasi}")
                    print("Selamat menyelesaikan tugas!!")
                    print('-' * 30)
                
                # Memulai mengerjakan tugas yang paling awal
                
                narasi_awal = None

                # Mencari tugas pertama yang sedang dikerjakan
                first_task = tasks_sorted[0]
                
                # Mengatur narasi dengan narasi dari tugas pertama
                if first_task[0] in area_tupai:
                    narasi_awal = narasi_1
                elif first_task[0] in kebun_terbengkalai:
                    narasi_awal = narasi_2
                elif first_task[0] in lubang_kelinci_raksasa:
                    narasi_awal = narasi_3
                elif first_task[0] in gua_beracun:
                    narasi_awal = narasi_4
                elif first_task[0] in kolam_kecil:
                    narasi_awal = narasi_5
                elif first_task[0] in gua_gibi:
                    narasi_awal = narasi_6
                elif first_task[0] in taman_matahari:
                    narasi_awal = narasi_7
                elif first_task[0] in kebun_merah:
                    narasi_awal = narasi_8
                elif first_task[0] in surga_burung:
                    narasi_awal = narasi_9
                else:
                    print("Jenis item tidak ditemukan di dalam area")

                print("\nMulai mengerjakan tugas\n")
                jenis_tugas_awal = f"{tasks_sorted[0][0]}[{tasks_sorted[0][1]}]"
                jumlah_awal = tasks_sorted[0][3]
                progres_awal = tasks_sorted[0][2]
                if jenis_tugas_awal:
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
                        print("Jenis item tidak ditemukan di dalam area")
                        
                          
                print(f"jenis_tugas = {jenis_tugas_awal}")
                print(f"jumlah = {jumlah_awal}x")
                print(f"progres = {progres_awal}")
                print(f"narasi = {narasi_awal}")
                
                time.sleep(2)
                await client.send_message(bot_id, gbk)
                
                  
        
        if "Berikut adalah daftar Tugas" in pesan:
            misi = []
            print()
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
    
        
        if "Kamu masih memiliki 3 tugas aktif untuk dikerjakan" in pesan:
            time.sleep(2)
            await event.respond(tsk)
            return
          
        if "Berhasil mengambil tugas dengan ID" in pesan:
            print(pesan)
            time.sleep(2)
            await event.respond(tskg)
            return
        
        if "Tugas tidak ditemukan" in pesan or "Kamu tidak bisa mengambil" in pesan:
            time.sleep(1.5)
            await event.respond(tskg)
            return
        
        if "Berhasil menyelesaikan tugas" in pesan:
            print('-'*30+f"\nTugas sudah di selesaikan\n"+'-'*30)
            time.sleep(2)
            await client.forward_messages(ch, event.message)
            time.sleep(2)
            await event.respond(tskg)
            return
        
        elif any(loc in pesan for loc in jalan):
            time.sleep(1.5)
            await event.click(0,0)
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
        
        
        elif "berhasil mendapat" in pesan:
            handle_task_progress(pesan, jenis_tugas_awal, jumlah_awal)
            return
      
        
        elif "belum menemukan apa-apa" in pesan:
            time.sleep(1.5)
            await event.click(0,0)
            return
        
        
        elif '- GBK ⛰' in pesan:
            narasi = narasi_awal
            if narasi in pesan:
                print('-' * 30)
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
            print('-'*30+f"\nNaik Level Dik\n"+'-'*30)
            time.sleep(1.5)
            await client.forward_messages(ch, event.message)
            time.sleep(1.5)
            await event.respond(tskg)
            return
        
    client.start()
    print(time.asctime(), '-', 'Mulai')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Berhenti')
    