from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from config import BOT_TOKEN, IMAGES_DIR
from app.services.ai_parser import parse_receipt
from app.db.db import init_db
from app.db.query import save_receipt, filter_period
from app.bot.utils import format_message_receipt, format_db_filter
from app.bot.period_formatter import period_formatter
import uuid
import os

async def start(update: Update, context) -> None:
    await update.message.reply_text("Hi, send me an image of a receipt")
    #todo: add help command to describe bot features

async def handle_image(update: Update, context) -> None:
    photo= update.message.photo[-1]

    #set unique id and image path
    file_id = str(uuid.uuid4())
    image_path= os.path.join(IMAGES_DIR, f"{file_id}.jpg")

    #download and save temporary image
    file= await context.bot.get_file(photo.file_id)
    await file.download_to_drive(image_path)

    #send to ai_parser
    try:
        parsed_data= parse_receipt(image_path)
    except Exception as e:
        await update.message.reply_text(str(e))
        return

    #save to db parsed data
    receipt_id=save_receipt(parsed_data)
    #delete image
    os.remove(image_path)

    #bot answer
    await update.message.reply_text(format_message_receipt(parsed_data, receipt_id))

async def recap(update: Update, context ) -> None:
    #take the argument after the command, join the chunk into string
    period= "".join(context.args)
    #obtain number of days to subtract
    formatted_period= period_formatter(period)

    #filter data based on period
    filtered_receipt= filter_period(formatted_period)

    if not filtered_receipt:
        await update.message.reply_text("🧐 No data found for the selected period")
        return

    #bot answer with formatted data
    await update.message.reply_text(format_db_filter(filtered_receipt))

def main():
    init_db()
    # Create the Application and pass it your bot's token.
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))
    app.add_handler(CommandHandler("recap", recap))
    app.run_polling()
if __name__ == "__main__":
    main()
