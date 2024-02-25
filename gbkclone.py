import time, asyncio, sys, random, re

from telethon import TelegramClient, events, utils, Button

import time, os, asyncio, sys, re, random, logging
logging.basicConfig(level=logging.ERROR)

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = input('Akun : ')

gbk = '/gbk_jelajah'
restore = '/restore_max_confirm'
bot_id = "KampungMaifamBot"
#bot_id = 5199147926
krj = '/gbk_keranjang'
tsk = '/gbk_Task'
tskg = '/gbk_task_G'
cmd = '/gbk'

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


area_tupai = {
    "BerryBiasa[A]", "BerryBiasa[B]", "BerryBiasa[C]", "BerryBiasa[D]", "BerryLiar[B]", "BerryLiar[C]", "KacangOak", "KacangOak[A]", "KacangOak[B]", "KacangOak[C]", "KacangOak[D]", "KacangOak[E]", "Pisang", "Pisang[C]", "Pisang[D]", "Pisang[E]"
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

kebun_merah = {
    "Apel", "Apel[B]", "Apel[C]", "Apel[D]", "Apel[E]", "Strawberry", "Strawberry[B]", "Strawberry[C]", "Strawberry[D]", "Strawberry[E]", "Tomat", "Tomat[B]", "Tomat[C]", "Tomat[D]", "Tomat[E]"
}

kolam_kecil = {
    "GuramiKecil", "GuramiKecil[C]", "GuramiKecil[D]", "GuramiKecil[E]", "KoiKecil", "MujairKecil", "MujairKecil[C]", "MujairKecil[D]", "MujairKecil[E]"
}

gua_gibi = {
    "Batu", "BatuBara", "BatuBara[D]", "BatuBara[E]", "Batu[D]", "Batu[E]", "BatuKerikil", "BatuKerikil[D]", "BatuKerikil[E]", "Nikel", "Nikel[D]", "Nikel[E]"
}

surga_burung = {
    "Apel[A]", "Apel[B]", "Apel[S]", "Avokad[A]", "Avokad[B]", "Avokad[S]", "Pisang[A]", "Pisang[B]", "Pisang[S]", "TelurBurungHantu", "TelurBurungUnta", "TelurElang", "TelurGagak", "TelurKakakTua", "TelurMerak", "TelurPhoenix", "TelurPuyuh"
}

taman_matahari = {
    "BungaMatahari", "BungaMatahari[A]", "BungaMatahari[B]", "BungaMatahari[C]", "BungaMatahari[D]", "BungaMatahari[E]", "BungaMatahari[S]", "BungaMatahari[SS]", "BungaMatahari[SSS]"
}

jalan = narasi_gbk


emoji_list = ['🍎','🍓', '🌰', '🍅', '🥜', '🍌', '🍄','🌻','▪️']

jumlah = 0
misi = []
narasi = []
tugas = []
klem = []
jenis_tugas = []
ch = -1001522767385

areas = [area_tupai, kebun_terbengkalai, lubang_kelinci_raksasa, gua_beracun, kebun_merah, kolam_kecil, gua_gibi, surga_burung, taman_matahari]


area_tugas = [
    area_tupai, kebun_terbengkalai, lubang_kelinci_raksasa,
    gua_beracun, kolam_kecil, gua_gibi, taman_matahari,
    kebun_merah, surga_burung
]

def tentukan_narasi(jenis_tugas):
    if jenis_tugas in area_tupai:
        return "Tempat ini dipenuhi tupai"
    elif jenis_tugas in kebun_terbengkalai:
        return "Dulu sekali seorang petani tinggal"
    elif jenis_tugas in lubang_kelinci_raksasa:
        return "Di sini tidak benar-benar ada kelinci"
    elif jenis_tugas in gua_beracun:
        return "Keberadaan tumbuhan-tumbuhan beracun di gua ini"
    elif jenis_tugas in kolam_kecil:
        return "Ikan-ikan kecil hidup di sini"
    elif jenis_tugas in gua_gibi:
        return "Gua kecil di bagian dasar Gunung"
    elif jenis_tugas in taman_matahari:
        return "Taman bunga matahari di kaki Gunung"
    elif jenis_tugas in kebun_merah:
        return "di sini mayoritas berwarna merah"
    elif jenis_tugas in surga_burung:
        return "di sini terdapat berbagai macam burung"
    else:
        return "Jenis tugas tidak dikenali."

with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(bot_id, tskg))
    @client.on(events.NewMessage(from_users=bot_id))
    async def handler(event):
        pesan = event.raw_text
        global misi, jumlah, tugas, klem, narasi, jenis_tugas, item
        if "Selesaikan tugas-tugas" in pesan:
            if "Tidak ada tugas" in pesan:
                print("Tidak ada tugas yang sedang diambil")
                time.sleep(2)
                await event.respond(cmd)
            if "Ongoing Task" in pesan:
                tasks = []
                lines = pesan.split("\n")
                for line in lines:
                    if "(" in line and ")" in line:
                        task_info = line.split("(")[0].strip()
                        task_progress = line.split("(")[1].split(")")[0].strip()
                        tasks.append((task_info, task_progress))
                if tasks:
                    print("Tugas-tugas yang sedang berlangsung:")
                    for task, progress in tasks:
                        task_name = task.split()[1]  # Mengambil nama tugas
                        task_amount = progress.split("/")[0]  # Mengambil jumlah yang sudah dikerjakan
                        task_total = progress.split("/")[1]  # Mengambil total jumlah tugas
                        print(f"- {task_name}: {task_amount}/{task_total}")
                        jenis_tugas = task_name
                    
                        if jenis_tugas:
                            time.sleep(2)
                            await event.respond(gbk)
                            narasi = tentukan_narasi(jenis_tugas)
                            tugas = jenis_tugas
                            print('-'*30+f"\nTersedia tugas\njenis_tugas = {tugas}\njumlah = {klem}x\nprogres = {jumlah}\nnarasi = {narasi}\nSelamat menyelesaikan tugas!!\n"+'-'*30)
                            break  # Memastikan 'break' berada di dalam loop
                  
        
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
                            pass 
                
                exp_list = None
                exp_split = [i for i in x.split("\n") if "🎁 EXP:" in i]
                if exp_split:
                    exp = exp_split[0].split()
                    if len(exp) >= 3:
                        try:
                            exp_list = int(exp[2].replace("❇️", ""))
                        except ValueError:
                            pass 
                
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
            misi.sort(key=get_exp, reverse=False)
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
        
        if 'berhasil mendapat' in pesan:
            item = pesan.splitlines()[4].split('berhasil mendapat ')[1]
            if tugas == item:
                jumlah+=1
                print(f'Progres {tugas} = {jumlah}')
                if jumlah %klem == 0:
                    time.sleep(1.5)
                    await event.respond('/gbk_task')
                    jumlah = 0
                    print('Misi selesai. Yuk cari misi lagi!')
                else:
                    time.sleep(1.5)
                    await event.click(0,0)
            else:
                time.sleep(1.5)
                await event.click(0,0)
            return
        
        elif "belum menemukan apa-apa" in pesan:
            time.sleep(1.5)
            await event.click(0,0)
            return
        
        elif "Tugas tidak ditemukan" in pesan:
            time.sleep(1.5)
            await event.respond(tskg)
            return
        
        elif '- GBK ⛰' in pesan:
            if narasi in pesan:
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