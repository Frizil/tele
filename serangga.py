import asyncio
import sys
import re, time
from telethon import TelegramClient, events

api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_fil = input('Siapa: ')

area = "/mg2024_Hutan4"
skill = 1000
tmp = 0
skillasli = []
bot = 'kampungmaifambot'

async def main():
    async with TelegramClient(sesi_fil, api_id, api_hash) as clien:
        await clien.send_message("kampungmaifambot", '/mg2024_game_Berburu_31')

        @clien.on(events.NewMessage(from_users="kampungmaifambot"))
        async def handler(event):
            global skill
            global coin
            global tmp
            global maling2
            pesan = event.raw_text
            print(skill)
           
            
            if 'kemampuan saat ini: 7,000' in pesan:
                skill = 7000
                await asyncio.sleep(1.5)
                await event.respond('/mg2024_buff_Energi')
                return
            
            if 'menjadi target buruan kamu' in pesan:
                pesan = event.text
                a = pesan.split('\n\n')
                o = re.findall('\d+', pesan)
                angka1 = int(o[0])
                skill += angka1  
                a = skill - 7000 
                skillasli.append(a)
                if skill > 7000:
                   await asyncio.sleep(1.5)
                   await event.respond("/mg24_kurangiSkill_"+str(a))
                   return
                elif skill < 7000:
                   await asyncio.sleep(1.5)
                   await event.respond('/mg2024_buff_Energi')
                   return
                return
            
            if 'Silakan pilih hewan mana' in pesan:
                pattern = r'\bTunggu\s+(\d+)\s+(?:detik\b)?'
                match = re.search(pattern, pesan)
                if match:
                    angka = match.group(1)
                    detik = int(angka)
                    if detik >= 8:
                        
                        jeda = detik - 5.5
                        print(jeda)
                        if '/mg2024_tangkap_Tupai' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Tupai')
                            return
                        if '/mg2024_tangkap_Monyet' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Monyet')
                            return
                        if '/mg2024_tangkap_Babihutan' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Babihutan')
                            return
                        if '/mg2024_tangkap_Babi' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Babi')
                            return
                        if '/mg2024_tangkap_Gorila' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Gorila')
                            return
                        if '/mg2024_tangkap_Rusa' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Rusa')
                            return
                        if '/mg2024_tangkap_Badak' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Badak')
                            return
                        if '/mg2024_tangkap_Gajah' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Gajah')
                            return
                        if '/mg2024_tangkap_Mammoth' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Mammoth')
                            return
                        if '/mg2024_tangkap_Harimau' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Harimau')
                            return
                        if '/mg2024_tangkap_Puma' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Puma')
                            return
                        if '/mg2024_tangkap_Citah' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Citah')
                            return
                        if '/mg2024_tangkap_Jaguar' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Jaguar')
                            return
                        if '/mg2024_tangkap_Panther' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Panther')
                            return
                        if '/mg2024_tangkap_GorilaAlbino' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_GorilaAlbino')
                            return
                        if '/mg2024_tangkap_BayiUnicorn' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_BayiUnicorn')
                            return
                        if '/mg2024_tangkap_Unicorn' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Unicorn')
                            return
                        if '/mg2024_tangkap_Kelelawar' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Kelelawar')
                            return
                        if "Babi tidak ditemukan" in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_BabiHutan')
                            return
                        else:
                            tmp = 0
                            maling2 = pesan.split()
                            maling = [i for i in maling2 if '/mg2024_tangkap' in i]
                            await asyncio.sleep(jeda)
                            await clien.send_message(bot, maling[tmp])
                        
                    elif detik <= 6:
                        jeda = detik - int(detik - 1)
                        print(jeda)
                        if '/mg2024_tangkap_Tupai' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Tupai')
                            return
                        if '/mg2024_tangkap_Monyet' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Monyet')
                            return
                        if '/mg2024_tangkap_Babihutan' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Babihutan')
                            return
                        if '/mg2024_tangkap_Babi' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Babi')
                            return
                        if '/mg2024_tangkap_Gorila' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Gorila')
                            return
                        if '/mg2024_tangkap_Rusa' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Rusa')
                            return
                        if '/mg2024_tangkap_Badak' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Badak')
                            return
                        if '/mg2024_tangkap_Gajah' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Gajah')
                            return
                        if '/mg2024_tangkap_Mammoth' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Mammoth')
                            return
                        if '/mg2024_tangkap_Harimau' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Harimau')
                            return
                        if '/mg2024_tangkap_Puma' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Puma')
                            return
                        if '/mg2024_tangkap_Citah' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Citah')
                            return
                        if '/mg2024_tangkap_Jaguar' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Jaguar')
                            return
                        if '/mg2024_tangkap_Panther' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Panther')
                            return
                        if '/mg2024_tangkap_GorilaAlbino' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_GorilaAlbino')
                            return
                        if '/mg2024_tangkap_BayiUnicorn' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_BayiUnicorn')
                            return
                        if '/mg2024_tangkap_Unicorn' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Unicorn')
                            return
                        if '/mg2024_tangkap_Kelelawar' in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_Kelelawar')
                            return
                        if "Babi tidak ditemukan" in pesan:
                            await asyncio.sleep(jeda)
                            await event.respond('/mg2024_tangkap_BabiHutan')
                            return
                        else:
                            tmp = 0
                            maling2 = pesan.split()
                            maling = [i for i in maling2 if '/mg2024_tangkap_' in i]
                            await asyncio.sleep(jeda)
                            await clien.send_message(bot, maling[tmp])
                    else:
                        print("Waktu jeda sudah habis atau tidak ada")
                else:
                    print("Angka tidak ditemukan dalam pesan.")
            
            if "dikurangi dari kemampuan berburu" in pesan:
                skill -= skillasli[0]
                skillasli.clear()
                await asyncio.sleep(1.5)
                await event.respond('/mg2024_buff_Energi')
                return
                
            if "Pelan-pelan, amati sekitar" in pesan:
                await asyncio.sleep(1.5)
                await event.click(text="Cari Hewan")
                return
                
            if "Kamu memerlukan " in pesan:
                await asyncio.sleep(1.5)
                await event.respond(area)
                return
                
            if "Energi dipulihkan menjadi 100%!!" in pesan:
                await asyncio.sleep(1.5)
                await event.respond(area)
                return
                
            if "Kumpulkan poin sebanyak-banyaknya" in pesan:
                await asyncio.sleep(1.5)
                await event.click(text="START")
                return
                
            if "Apa kamu yakin" in pesan:
                await asyncio.sleep(0.5)
                await event.click(text="Confirm")
                return
                
            if "Permainan dimulai" in pesan:
                await asyncio.sleep(0.5)
                await event.respond(area)
                return
              
            if "area berburu bisa dikunjungi" in pesan:
                await asyncio.sleep(0.5)
                await event.respond(area)
                return
            
        print(time.asctime(), '-', 'Mulai')
        await clien.run_until_disconnected()
        print(time.asctime(), '-', 'Berhenti')
            

asyncio.run(main())
print('Cha Alay')