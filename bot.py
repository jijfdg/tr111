import logging
import asyncio
from datetime import datetime, timedelta
from aiohttp import ClientSession
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import sqlite3
import config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS rentals (
    user_id INTEGER PRIMARY KEY,
    phone_number TEXT,
    rental_end DATETIME
)
''')
conn.commit()

scheduler = AsyncIOScheduler()
scheduler.start()

RENTAL_OPTIONS = {
    '1_day': {'label': '1 день — 10 ₽', 'days': 1, 'price': 10},
    '7_days': {'label': '7 дней — 50 ₽', 'days': 7, 'price': 50},
    '30_days': {'label': '30 дней — 150 ₽', 'days': 30, 'price': 150},
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(RENTAL_OPTIONS[key]['label'], callback_data=key)]
        for key in RENTAL_OPTIONS
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Добро пожаловать в ItPhone SMS Bot\nВыберите срок аренды виртуального номера:", 
        reply_markup=reply_markup
    )

async def handle_rental_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    option = query.data
    if option not in RENTAL_OPTIONS:
        await query.edit_message_text("Ошибка выбора. Попробуйте снова.")
        return

    price = RENTAL_OPTIONS[option]['price']
    days = RENTAL_OPTIONS[option]['days']

    await query.edit_message_text(
        f"Вы выбрали аренду на {days} дней за {price} ₽.\n"
        f"Для оплаты используйте CryptoBot. (Здесь будет кнопка оплаты)"
    )

async def main():
    app = ApplicationBuilder().token(config.TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_rental_selection))
    print("Бот запущен...")
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
