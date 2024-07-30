import discord
from discord.ext import commands
from utils import log

class DiscordBot(commands.Bot):
    def __init__(self, token, command_prefix="!", intents=None):
        intents = intents or discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.token = token
        self.telegram_bot = None
        self.target_channel_id = None

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        await log(message.content)
        if self.telegram_bot and self.telegram_bot.application:
            await self.telegram_bot.application.bot.send_message(chat_id=self.telegram_bot.target_chat_id, text=message.content)

    async def start_bot(self):
        await self.start(self.token)

    async def stop_bot(self):
        await self.close()
