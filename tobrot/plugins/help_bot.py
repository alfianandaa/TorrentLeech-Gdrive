#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

help_string = f'''
/mirror: Start mirroring the link to google drive

/mirrorup: Start mirroring the link to Telegram

/tmirror unzip | unrar | untar: Reply to any File on Telegram Start mirroring and if downloaded file is any archive , extracts it to google drive

/mirror unzip | unrar | untar: starts mirroring and if downloaded file is any archive , extracts it to google drive

/mirror archive: start mirroring and upload the archived (.tar) version of the download

/ytdl: Reply To message Link To Mirror through youtube-dl and Upload to Telegram

/cancel (GID): Reply to the message by which the download was initiated and that download will be cancelled

/status: Shows a status of all the downloads

/stats: Show Stats of the machine the bot is hosted on

/ping: Test Ping 
'''

async def help_bot_message(client, message):
    await message.reply_text(help_string)


