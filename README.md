# ItPhone SMS Bot

Telegram-бот для аренды виртуальных номеров через Itphone с оплатой криптовалютой через CryptoBot.

## Возможности
- Аренда виртуальных номеров на 1, 7 или 30 дней
- Оплата в криптовалюте через CryptoBot
- Пересылка входящих SMS пользователю
- Автоматическое отключение по окончании срока аренды

## Установка

1. Клонируйте репозиторий
```bash
git clone https://github.com/yourusername/itphone_sms_bot.git
cd itphone_sms_bot
```

2. Создайте виртуальное окружение и установите зависимости
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

3. В `config.py` впишите свои ключи:
- TELEGRAM_TOKEN — токен Telegram-бота
- ITPHONE_API_KEY — API-ключ Itphone
- CRYPTOBOT_TOKEN — токен CryptoBot

4. Запустите бота
```bash
python bot.py
```

## Хостинг

Рекомендуется запускать бота на Replit, Railway, Render или VPS.

## Лицензия

MIT License
