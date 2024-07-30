from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from utils import log

class TelegramBot:
    def __init__(self, token, discord_bot):
        self.token = token
        self.application = None
        self.discord_bot = discord_bot
        self.target_chat_id = None
        print("telegram bot ready")

    async def echo(self, update: Update, context: CallbackContext) -> None:
        if update.message is not None:
            received_message_text = update.message.text
            await log(received_message_text)
            channel = self.discord_bot.get_channel(int(self.discord_bot.target_channel_id))
            if channel:
                await channel.send(received_message_text)

    async def start(self):
        self.application = Application.builder().token(self.token).build()
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.echo))
        await self.application.initialize()
        await self.application.start()
        await self.application.updater.start_polling()

    async def stop(self):
        await self.application.updater.stop()
        await self.application.stop()
        await self.application.shutdown()
