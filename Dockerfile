# Dockerfile

# Используем официальный образ Python 3.13.4
FROM python:3.13.4-slim

WORKDIR /app

# Копируем все файлы проекта
COPY . /app

# Обновляем pip и устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Запуск бота
CMD ["python", "bot.py"]
