import time
import asyncio
from telethon.sync import TelegramClient, events, utils, Button

# Ganti dengan informasi akun Telegram Anda
api_id = 18850178
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Zifri'

group_list = [
    'BIO_RPP_30',
    'bio_lpm_rpps',
    'BIORPP55',
    'BIORPP4_S2',
    'LPMBANG',
]

message = """
**BANG BANG LPM BANG BARU BUKA NIH
BANG BANG JOIN DONG BANG GAS KAN
JOIN BIAR RAME BANG SILAHKAN
UDAH JOIN BOLEH SEBARIN JUGA**

@LPMBANG @LPMBANG @LPMBANG
@LPMBANG @LPMBANG @LPMBANG
@LPMBANG @LPMBANG @LPMBANG

**BOLEH JUALAN, CARI CP, TEMAN DAN LAINNYA YAH!!!**

__— Jaseb by @coffeeseduh —__
"""

async def send_message_to_groups():
    async with TelegramClient(sesi_file, api_id, api_hash) as client:
        print(time.asctime(), "- Userbot Started")
        while True:
            for group_username in group_list:
                try:
                    await client.send_message(group_username, message, link_preview=False)
                    print(f"Pesan berhasil dikirim ke {group_username}")
                except Exception as e:
                    print(f"Terjadi kesalahan saat mengirim pesan ke {group_username}: {e}")
                await asyncio.sleep(2)
            await asyncio.sleep(10)

asyncio.run(send_message_to_groups())