from os import environ
import aiohttp
from pyrogram import Client, filters

API_ID = environ.get('API_ID', '4546803')
API_HASH = environ.get('API_HASH', '08ad181fba3b05e1141db96175cab60e')
BOT_TOKEN = environ.get('BOT_TOKEN', '6027500067:AAG-veKTUgl3nSIT2rpiK_FMAWv_60vPDqg')
PDISK_KEY = "99xz8zhn3shdv021ws"

bot = Client('gplink bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "I'm GPlink bot. Just send me link and get short link")

# Upload a file from local storage
responses = await pdisk.upload_file("/path/to/file")
for response in responses:
    print(response)

# Upload a remote file


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        responses = pdisk.upload_remote_file(link)
        print(response)
        await message.reply(f'Here is your https://pdisk.pro/{responses}', quote=True)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'https://pdisk.pro/api/upload/url'
    params = {'key': PDISK_KEY, 'url': url, 'fld_id': 0}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data['result']['file_code']

bot.run()
