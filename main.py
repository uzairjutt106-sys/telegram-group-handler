from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
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








def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register /start command
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_message))

    # Run bot
    print("bot is runing")
    app.run_polling()

if __name__ == "__main__":
    main()
