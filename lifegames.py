import time, os
import asyncio
import sys, re
import random
from time import sleep
from random import randint
from datetime import datetime
from telethon import TelegramClient, events, utils, Button
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

api_id = 18850178 
api_hash = '34d2d64d0bb5827789bc7bf7c0d34b69'
sesi_file = 'Judi'

cmd = 'Bbet 5+37'
grup = -1001944528171

bet = (
'1',
'3+40',
'2+40',
'69',
'4646'
)

user_id = 5199147926

async def bentar(w):
    await asyncio.sleep(w)
    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message(grup , cmd))
    
    @client.on(events.NewMessage(chats=grup))
    async def handler(event):
        pesan = event.raw_text
        from_ = await event.client.get_entity(event.from_id)
                
        if "🚓 Finns sepertinya kamu mencoba melanggar hukum.." in pesan:
            print(time.asctime(), pesan)
            await bentar(600)
            await client.send_message(grup, cmd)
            return
        
        if "🎰 Finns telah bertaruh" in pesan:
            print(time.asctime(), pesan)
            await bentar(2)
            await client.send_message(grup, "Bbet "+str(random.choice(bet)))
            return

        elif not from_.bot and not from_.user_id and 'send' in pesan:
            print(time.asctime(), pesan)
            await bentar(2)
            await event.reply('Ppay *')
            return
        
                
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	