from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters, CallbackContext, CommandHandler
from config import BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hi, send me an image of a receipt")

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    photo= update.message.photo[-1]
    file_id = photo.file_id
    file= await update.message.reply_text(f"🧾 Image received: the id is {file_id}")

def main():
    # Create the Application and pass it your bot's token.
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO,handle_image))

    app.run_polling()
if __name__ == "__main__":
    main()