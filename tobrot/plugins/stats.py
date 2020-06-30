# (c) Alfiananda84 

import shutil, psutil
import time
import pyrogram

from tobrot import botStartTime
from tobrot.helper_funcs.helper_stats import get_readable_time, get_readable_file_size

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

