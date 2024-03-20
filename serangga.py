import time
import asyncio
import threading
import re
from telethon import TelegramClient, events

api_id = 224069
api_hash = 'f2ddfd53867f28a3b6b98e80fa010e9d'
sesi_fil = input('Siapa: ')

skill = 1000
bot = 'kampungmaifambot'

async def handle_event(event, clien):
    global skill
    if 'kemampuan saat ini: 7,000' in event.raw_text:
        skill = 7000
        await asyncio.sleep(1.5)
        await event.respond('/mg2024_buff_Energi')
    elif 'menjadi target buruan kamu' in event.raw_text:
        pesan = event.text
        angka = re.findall('\d+', event.raw_text)
        angka1 = int(angka[0])
        skill += angka1
        a = skill - 7000
        if skill > 7000:
            await asyncio.sleep(1.5)
            await event.respond("/mg24_kurangiSkill_" + str(a))
        elif skill < 7000:
            await asyncio.sleep(1.5)
            await event.respond('/mg2024_buff_Energi')
    elif 'Tunggu' in event.raw_text:
        time_to_sleep = int(re.findall(r'Tunggu (\d+)', event.raw_text)[0]) - 3
        await asyncio.sleep(time_to_sleep)
        tangkap = re.findall(r'/mg2024_tangkap_\w+', event.raw_text)
        if tangkap:
            await event.respond(tangkap[0])
        else:
            maling2 = event.raw_text.split()
            maling = [i for i in maling2 if '/mg2024_tangkap' in i]
            await clien.send_message(bot, maling[0])
    elif "dikurangi dari kemampuan berburu" in event.raw_text:
        skill -= int(re.findall('\d+', event.raw_text)[0])
        await asyncio.sleep(1.5)
        await event.respond('/mg2024_buff_Energi')
    elif "Pelan-pelan, amati sekitar" in event.raw_text:
        await asyncio.sleep(1.5)
        await event.click(text="Cari Hewan")
    elif "Kamu memerlukan " in event.raw_text:
        await asyncio.sleep(1.5)
        await event.respond('/mg2024_Hutan4')
    elif "Energi dipulihkan menjadi 100%!!" in event.raw_text:
        await asyncio.sleep(1.5)
        await event.respond('/mg2024_Hutan4')
    elif "Kumpulkan poin sebanyak-banyaknya" in event.raw_text:
        await asyncio.sleep(1.5)
        await event.click(text="START")
    elif "Apa kamu yakin" in event.raw_text:
        await asyncio.sleep(0.5)
        await event.click(text="Confirm")
    elif "Permainan dimulai" in event.raw_text:
        await asyncio.sleep(0.5)
        await event.respond('/mg2024_Hutan4')

async def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    async with TelegramClient(sesi_fil, api_id, api_hash, loop=loop) as clien:
        clien.loop.create_task(clien.send_message("kampungmaifambot", '/mg2024_game_Berburu_30'))
        clien.add_event_handler(handle_event, events.NewMessage(from_users="kampungmaifambot"))
        await clien.run_until_disconnected()

threading.Thread(target=lambda: asyncio.run(main())).start()
print(time.asctime(), '-', 'Cha Alay')