# © ported from izzy12 by alfiananda84

import shutil, psutil
import time
import pyrogram
import subprocess
import os
import asyncio

from tobrot import botStartTime
from tobrot.helper_funcs.helper_stats import get_readable_time, get_readable_file_size
from tobrot import (
    DESTINATION_FOLDER,
    RCLONE_CONFIG
)

async def stats_bot_g(client, message):
    currentTime = get_readable_time((time.time() - botStartTime))
    total, used, free = shutil.disk_usage('.')
    total = get_readable_file_size(total)
    used = get_readable_file_size(used)
    free = get_readable_file_size(free)
    cpuUsage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    stats = f'Bot Uptime: {currentTime}\n' \
            f'Total disk space: {total}\n' \
            f'Used: {used}\n' \
            f'Free: {free}\n' \
            f'CPU: {cpuUsage}%\n' \
            f'RAM: {memory}%\n'
    await message.reply_text(stats)

async def ping_bot_g(client, message):
    start_time = int(round(time.time() * 1000))
    i_m_sefg = await message.reply_text(f'ping')
    end_time = int(round(time.time() * 1000))
    await i_m_sefg.edit_text(f"""pong! \n{end_time - start_time} ms""")

async def check_size_g(client, message):
    #await asyncio.sleep(5)
    del_it = await message.reply_text("Checking size...")
    subprocess.Popen(('touch', 'rclone.conf'), stdout = subprocess.PIPE)
    with open('rclone.conf', 'a', newline="\n") as fole:
        fole.write("[DRIVE]\n")
        fole.write(f"{RCLONE_CONFIG}")
    destination = f'{DESTINATION_FOLDER}'
    process1 = subprocess.Popen(['rclone', 'size', '--config=rclone.conf', 'DRIVE:'f'{destination}'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    popi, popp = process1.communicate()
    print(popi)
    print(popp)
    print(popp.decode("utf-8"))
    p = popi.decode("utf-8")
    print(p)
    await asyncio.sleep(5)
    await del_it.edit_text(f"Folder {DESTINATION_FOLDER} Info:\n\n{p}")
