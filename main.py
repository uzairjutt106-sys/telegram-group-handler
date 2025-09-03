from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler,MessageHandler, filters, ContextTypes 
import os

BOT_TOKEN = "8027538894:AAHM68ckyxHN7QPKCPOLrscn_BTM5j6avCI"

async def check_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    user = update.message.from_user.first_name  
    await update.message.reply_text("Hello! I am alive 🚀")
    if "http://" in message or "https://" in message or "www." in message:
        # Delete the message
        await update.message.delete()
        print(f"Deleted a link message from {user}")

async def send_reminder(context:ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.chat_id
    await context.bot.send_message(chat_id=chat_id, text="Hello! I am alive 🚀")

async def start_reminder(update: Update, context:ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    complext.job_queue.run_repeating(send_reminder, interval=1800, first=10, chat_id=chat_id)
    await update.message.reply_text("url not allowed")
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register /start command
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_message))
    app.add_handler(CommandHandler("start", start_reminder))

    # Run bot
    print("bot is runing")
    app.run_polling()

if __name__ == "__main__":
    main()
