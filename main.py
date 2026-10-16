import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN = "8852941397:AAGQr-kq2zU2_q8gc8k7H8oRgeyYusdaOZw"
CHANNEL = "@hellen_signals"
logging.basicConfig(level=logging.INFO)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am Hellen Bot!")
async def handle_signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = update.message.text
    fmt = f"HELLEN SIGNAL\n\n{txt}\n\nBy Hellen"
    try:
        await context.bot.send_message(chat_id=CHANNEL, text=fmt)
        await update.message.reply_text("Sent to channel!")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_signal))
    app.run_polling()
if __name__ == "__main__":
    main()
