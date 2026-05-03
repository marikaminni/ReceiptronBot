from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters, CommandHandler
from config import BOT_TOKEN, IMAGES_DIR
from app.services.ai_parser import parse_receipt
from app.db.db import init_db, save_receipt
from app.bot.utils import format_message_receipt
import uuid
import os
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hi, send me an image of a receipt")

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    photo= update.message.photo[-1]

    #set unique id and image path
    file_id = str(uuid.uuid4())
    image_path= os.path.join(IMAGES_DIR, f"{file_id}.jpg")

    #download and save temporary image
    file= await context.bot.get_file(photo.file_id)
    await file.download_to_drive(image_path)

    #send to ai_parser
    parsed_data= parse_receipt(image_path)
    #save to db parsered data
    receipt_id=save_receipt(parsed_data)
    #delete image
    os.remove(image_path)

    #bot answer
    await update.message.reply_text(format_message_receipt(parsed_data, receipt_id))

def main():
    init_db()
    # Create the Application and pass it your bot's token.
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO,handle_image))

    app.run_polling()
if __name__ == "__main__":
    main()