# Как развернуть Telegram-бота на Railway

Railway — одна из самых простых платформ для хостинга ботов. Вот пошаговая инструкция:

### 1. Подготовка проекта

- **`main.py`**: Убедитесь, что ваш основной файл запускает бота. Для `aiogram` 3.x это обычно выглядит так:
  ```python
  import asyncio
  # ... другие импорты
  
  async def main():
      # ... ваш код инициализации
      await dp.start_polling(bot)

  if __name__ == '__main__':
      asyncio.run(main())
  ```

- **`requirements.txt`**: Создайте этот файл и перечислите в нем все зависимости. Как минимум:
  ```
  aiogram==3.x.x
  python-dotenv==1.x.x
  ```

- **`Procfile`**: Создайте файл с именем `Procfile` (без расширения) и напишите в нем одну строку. Эта команда указывает Railway, как запустить вашего бота:
  ```
  worker: python main.py
  ```

### 2. Развертывание на Railway

1. Зарегистрируйтесь на [railway.app](https://railway.app) с помощью вашего GitHub-аккаунта.

2. Нажмите "New Project" и выберите "Deploy from GitHub repo".

3. Выберите ваш репозиторий с ботом.

4. Railway автоматически обнаружит `Procfile` и начнет развертывание.

### 3. Настройка переменных окружения

⚠️ **Никогда не храните токен бота в коде!**

1. В интерфейсе вашего проекта на Railway перейдите во вкладку "Variables".

2. Нажмите "New Variable".

3. Создайте переменную `BOT_TOKEN` и вставьте в значение токен вашего бота.

4. В коде `main.py` получайте токен из окружения:
   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()  # Загружает переменные из .env для локального теста

   BOT_TOKEN = os.getenv("BOT_TOKEN")
   bot = Bot(token=BOT_TOKEN)
   ```

После добавления переменной Railway автоматически перезапустит вашего бота, и он будет работать в облаке.
