from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
from logger import LOGGER

bot = Client(
    "uploader_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("✅ Uploader Bot Running Successfully 🚀")

LOGGER.info("Bot Started Successfully")

bot.run()
