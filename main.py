import asyncio
import os
from dotenv import load_dotenv
from telegram_bot import TelegramBot
from discord_bot import DiscordBot

# .env 파일에서 환경 변수 로드
load_dotenv()

async def main():
    TELEGRAM_BOT_API_TOKEN = os.getenv("TELEGRAM_BOT_API_TOKEN")
    DISCORD_BOT_API_TOKEN = os.getenv("DISCORD_BOT_API_TOKEN")

    discord_bot = DiscordBot(DISCORD_BOT_API_TOKEN)
    telegram_bot = TelegramBot(TELEGRAM_BOT_API_TOKEN, discord_bot)
    discord_bot.telegram_bot = telegram_bot
    
    discord_bot.target_channel_id = os.getenv("YOUR_DISCORD_CHAT_ID")
    telegram_bot.target_chat_id = os.getenv('YOUR_TELEGRAM_CHAT_ID')

    try:
        await asyncio.gather(
            telegram_bot.start(),
            discord_bot.start_bot()
        )
    finally:
        await telegram_bot.stop()
        await discord_bot.stop_bot()

if __name__ == "__main__":
    asyncio.run(main())
