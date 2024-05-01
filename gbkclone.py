#created by @itz, @hawk ini wm ya dick
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
krj = '/gbk_keranjang'
tsk = '/gbk_Task'
tskf = '/gbk_task_G'


narasi_gbk = {
    "memang melelahkan",
    "Gunung ini terlihat tenang",
    "Semangat, perjalanan panjang",
    "Saat ini kamu masih berada",
    "Hal-hal ajaib yang ada",
    "Sudah mulai lelah?",
    "Ada banyak lokasi-lokasi",
    "menemukan sebuah",
    "Seorang bajak laut terkenal",
    "Tempat-tempat langka",
    "Gunung ini menyimpan kekuatan sihir",
    "Hal paling misterius dari gunung",
    "Meskipun gunung ini sangat tinggi",
    "Sudah merasa berjalan cukup jauh",
    
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
narasi_10 = "Tempat hidup para monyet" #hutan monyet
narasi_11 = "Taman mawar yang dipenuhi mawar" #rumah mawar
narasi_12 = "Gua ini menyimpan permata" #GOA L
narasi_13 = "Area subur yang dipenuhi buah-buahan" #kebun emas

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

hutan_monyet = {
    "Mentimun", "Mentimun[A]" ,"Mentimun[B]", "Mentimun[C]", "Mentimun[D]", "Mentimun[E]", "Mentimun[S]", "PisangKeramat", "PisangKeramat[C]", "PisangKeramat[D]", "PisangKeramat[E]"
}

rumah_mawar = {
    "MawarHitam", "MawarMerah", "MawarMerahJambu", "MawarPutih", "MawarUngu"
}

goal = {
    "Amethyst", "GreenJade", "LemonQuartz", "Moonstone", "RoseQuartz"
}

kebun_emas = {
    "AnggurEmas", "ApelEmas", "ManggaEmas" , "PepayaEmas", "PisangEmas"
}

jalan = narasi_gbk

ch = -1001522767385

emoji_list = ['🌻', '🍄', '🍌', '🌰', '🥜', '🍎', '🍓', '🍅', '▪️', '🥕', '🥔', '🐟', '🥚', '🥑', '◻️', '🍐', '🥭', '🍇','🥀', '🥒']
full_emoji = ['🌻', '🍄', '🍌', '🌰', '🥜', '🍎', '🍓', '🍅', '▪️', '🥕', '🥔', '🐟', '🥚', '🥑', '◻️', '🍐', '🥭', '🍇','🥀', '🥒']
jumlah = 0
misi = []
narasi = []
tugas = []
klem = []
jenis_tugas = []
tasks = []

masak = "/masak_MiniBacon_220"
makan = "/makan_steaksapipremium"

with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, tskf))
    @client.on(events.NewMessage(from_users=bot_id))
    async def handler(event):
        pesan = event.raw_text
        global misi, jumlah, jenis_tugas, run_task, run_total, run_narasi, run_progress, tasks, task_nongrade, task_grade,tugas_awal
        
        if "Selesaikan tugas-tugas" in pesan:
            if "Tidak ada tugas" in pesan:
                print('-' * 30)
                print("Tidak ada tugas yang sedang diambil. Menanggapi dengan tugas baru.")
                print('-' * 30)
                time.sleep(2.0)
                await event.respond(tskf)
            if "Ongoing Task" in pesan:
                time.sleep(2)
                print('-' * 30)
                print("Kondisi Ongoing Task terpenuhi")
                print('-' * 30)
                # Pola regex untuk mengekstrak informasi tugas dengan grade
                pola_grade = r'([A-Za-z]+)\[([A-Z]+)\] \((\d+)/(\d+)\)\n⏱ (.+?)\n'
                # Pola regex untuk mengekstrak informasi tugas tanpa grade
                pola_nongrade = r'([A-Za-z]+) \((\d+)/(\d+)\)\n⏱ (.+?)\n'
                # Mencocokkan pola regex dengan pesan untuk mengekstrak informasi tugas dengan grade
                tasks_grade = re.findall(pola_grade, pesan)
                # Mencocokkan pola regex dengan pesan untuk mengekstrak informasi tugas tanpa grade
                tasks_nongrade = re.findall(pola_nongrade, pesan)
            
                if tasks_grade:
                    print('-' * 30)
                    print("Tersedia tugas dengan grade:")
                    print('-' * 30)
                    for task in tasks_grade:
                        tasks.append(task)
                        jenis_tugas = f"{task[0]}[{task[1]}]"
                        total = task[3]
                        progress = task[2]
                        print(f"Jenis tugas: {jenis_tugas}")
                        print(f"Total: {total}x")
                        print(f"Progress: {progress}")
                        print('-' * 30)
                
                if tasks_nongrade:
                    print('-' * 30)
                    print("Tersedia tugas tanpa grade:")
                    print('-' * 30)
                    for task in tasks_nongrade:
                        jenis_tugas = task[0]
                        total = task[2]
                        progress = task[1]
                        tasks.append((jenis_tugas, "", progress, total, ""))
                        print(f"Jenis tugas: {jenis_tugas}")
                        print(f"Total: {total}x")
                        print(f"Progress: {progress}")
                        print('-' * 30)
                
                
                tasks_sorted = sorted(tasks, key=lambda x: x[3])
                tugas = tasks_sorted
                tugas1 = tugas[0]
                tugas2 = tugas[1]
                tugas3 = tugas[2]
                print(tasks_sorted)
                urutan = f"""
Urutan Tugas Berdasarkan Total :
Task 1 =  {tugas1[0]}  total {tugas1[3]}
Task 2 =  {tugas2[0]}  total {tugas2[3]}
Task 3 =  {tugas3[0]}  total {tugas3[3]}
"""
                print(urutan)
                
                narasi = None
                run_narasi = None
                task_nongrade = None
                task_grade = None
                tugas_awal = None
                
                tugas_pertama = tugas1
                print(tugas_pertama)
                
                if tugas_pertama[1] == '':
                    task_nongrade = f"{tugas_pertama[0]}"
                    tugas_awal=task_nongrade
                
                else: 
                    task_grade = f"{tugas_pertama[0]}[{tugas_pertama[1]}]"
                    tugas_awal=task_grade
                
                
                if tugas_awal == task_nongrade:
                    run_task = task_nongrade
                    run_total = tugas_pertama[3]
                    run_progress = tugas_pertama[2]
                elif tugas_awal == task_grade:
                    run_task = task_grade
                    run_total = tugas_pertama[3]
                    run_progress = tugas_pertama[2]
                
                
                print(run_task)
                
                if run_task in area_tupai:
                    run_narasi = narasi_1
                elif run_task in kebun_terbengkalai:
                    run_narasi = narasi_2
                elif run_task in lubang_kelinci_raksasa:
                    run_narasi = narasi_3
                elif run_task in gua_beracun:
                    run_narasi = narasi_4
                elif run_task in kolam_kecil:
                    run_narasi = narasi_5
                elif run_task in gua_gibi:
                    run_narasi = narasi_6
                elif run_task in taman_matahari:
                    run_narasi = narasi_7
                elif run_task in kebun_merah:
                    run_narasi = narasi_8
                elif run_task in surga_burung:
                    run_narasi = narasi_9
                elif run_task in hutan_monyet:
                    run_narasi = narasi_10
                elif run_task in rumah_mawar:
                    run_narasi = narasi_11
                elif run_task in goal:
                    run_narasi = narasi_12
                elif run_task in kebun_emas:
                    run_narasi = narasi_13
                else:
                    print("\nJenis item tidak ditemukan di dalam area")
                    run_narasi = '⛰ Gunung Belakang Kebun ⛰'

                tugas_satu = f"""
Mulai mengerjakan tugas
jenis_tugas = {run_task}
jumlah = {run_total}x
progres = {run_progress}
narasi = {run_narasi}
Selamat menyelesaikan tugas!!
"""
                time.sleep(2)
                print(tugas_satu)
                time.sleep(2)
                await client.send_message(bot_id, gbk)
                return
                
                
                
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
            def get_koin(misi):
                return misi.get("koin_list")
            misi.sort(key=get_koin, reverse=True)
            
            #KALAU MAU CARI EXP TERBANYAK
            #def get_exp(misi):
                #return misi.get("exp_list")
            #misi.sort(key=get_exp, reverse=True)
            time.sleep(1.5)
            await event.respond(misi[0].get("misi_list"))
            return
        
        if "Berhasil menyelesaikan tugas" in pesan:
            print('\n'+'-'*30+f"\nTugas sudah di selesaikan\n"+'-'*30)
            tasks.clear()
            time.sleep(2)
            await client.forward_messages(ch, event.message)
            time.sleep(2)
            await event.respond(tskf)
            return
        
        elif any(loc in pesan for loc in jalan):
            time.sleep(1.5)
            await event.click(0,0)
            return
        
        elif "Tugas tidak ditemukan" in pesan or "silakan pilih tugas lain" in pesan:
            time.sleep(1.5)
            await event.respond(tskf)
            return
        
        elif "Gunung dipenuhi" in pesan:
            time.sleep(1.5)
            await event.respond(krj)
            return
          
        elif "Kamu tidak memiliki cukup energi" in pesan:
            time.sleep(1.5)
            await event.respond(makan)
            return
          
        elif "kamu tidak bisa makan" in pesan:
            time.sleep(1.5)
            await event.respond(restore)
            return
        
        elif "Energi berhasil" in pesan or "Uuuh rasanya enak sekali" in pesan:
            time.sleep(1.5)
            await event.respond(masak)
            return
          
        elif "Berhasil memasak" in pesan:
            time.sleep(1.5)
            await event.respond(masak)
            return
          
        elif "Kamu tidak bisa memasak" in pesan:
            time.sleep(1.5)
            await event.respond(tskf)
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
                await event.respond(tskf)
            if "kamu kosong" in pesan:
                time.sleep(1.5)
                await event.respond(tskf)
            else:
                time.sleep(1.5)
                await event.click(text='Kirim ke Barang')
            return
        
        elif "Kamu masih memiliki 3 tugas aktif untuk dikerjakan" in pesan:
            time.sleep(2)
            await event.respond(tsk)
            return
          
        elif "Berhasil mengambil tugas dengan ID" in pesan:
            time.sleep(2)
            await event.respond(tskf)
            return
        
        if "berhasil mendapat" in pesan:
            pola_item = pesan.splitlines()[4].split('berhasil mendapat')[1]
            pola_item = None
            for emoji in full_emoji:
                if emoji in pesan:
                    hasil_item = pesan.split(emoji,1)[1].split()[0]
            if hasil_item == run_task: 
                jumlah+=1
                print(f"\n{time.strftime('%X')} - Progres {run_task} = {jumlah}")
                if jumlah >= int(run_total):
                    print('\nMisi selesai. Yuk cari misi lagi!')
                    time.sleep(2.0)
                    await event.respond('/gbk_task')
                    jumlah = 0
                else:
                    time.sleep(1.5)
                    await event.click(0, 0)
            if hasil_item != run_task:
                time.sleep(1.5)
                await event.click(0, 0)
            return
        
        elif "belum menemukan apa-apa" in pesan:
            time.sleep(1.5)
            await event.click(0,0)
            return
        
        elif '- GBK ⛰' in pesan:
            narasi = run_narasi
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
          
        
        elif 'EXP terpenuhi!! Level pendaki meningkat!!' in pesan or 'Level maksimal tercapai' in pesan:
            print('\n'+'-'*30+f"\nNaik Level Dik\n"+'-'*30)
            time.sleep(1.5)
            await client.forward_messages(ch, event.message)
            time.sleep(1.5)
            await event.respond(tskf)
            return
        
    client.start()
    print(time.asctime(), '-', 'Mulai')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Berhenti')