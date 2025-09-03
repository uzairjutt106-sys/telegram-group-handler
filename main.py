from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler,MessageHandler, filters, ContextTypes 
import os

BOT_TOKEN = "8027538894:AAHM68ckyxHN7QPKCPOLrscn_BTM5j6avCI"

async def check_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    print(f"📌 Chat ID: {chat_id}")  
    message = update.message.text
    user = update.message.from_user.first_name  
    await update.message.reply_text("Hello! I am alive 🚀")
    if "http://" in message or "https://" in message or "www." in message:
        # Delete the message
        await update.message.delete()
        print(f"Deleted a link message from {user}")

async def send_reminder(context:ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.chat_id
    await context.bot.send_message(chat_id=chat_id, text="link messages not allowed")

def main():
    
    # Regdef main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # ✅ Initialize job queue
    job_queue = app.job_queue

    # Handle normal messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_message))
    chat_id = -1002980571408
    app.job_queue.run_repeating(send_reminder, interval=1800, first=10, chat_id=chat_id)

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
