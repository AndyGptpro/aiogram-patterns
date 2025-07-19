# 🚀 Быстрый старт

## Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/your-username/telegram-bot-patterns.git
   cd telegram-bot-patterns
   ```

2. **Создайте виртуальное окружение:**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Настройте переменные окружения:**
   ```bash
   # Скопируйте пример файла
   cp .env.example .env
   
   # Отредактируйте .env и добавьте ваш BOT_TOKEN
   ```

## Запуск примера

1. **Получите токен бота от [@BotFather](https://t.me/BotFather)**

2. **Добавьте токен в файл `.env`:**
   ```
   BOT_TOKEN=ваш_токен_здесь
   ```

3. **Запустите пример:**
   ```bash
   python example_bot.py
   ```

## Использование паттернов

### 1. Быстрое создание клавиатур
```python
from keyboards import create_inline_keyboard

keyboard = create_inline_keyboard(
    width=2,
    "Кнопка 1", "Кнопка 2",
    специальная_кнопка="custom_callback"
)
```

### 2. FSM состояния для диалогов
```python
from fsm_states import UserSurvey
from aiogram.fsm.context import FSMContext

@dp.message(Command("survey"))
async def start_survey(message: Message, state: FSMContext):
    await state.set_state(UserSurvey.waiting_for_name)
    await message.answer("Как вас зовут?")
```

### 3. Проверка подписки на канал
```python
from middlewares import ChannelSubscriptionMiddleware

# Применяется ко всем сообщениям
dp.message.middleware(ChannelSubscriptionMiddleware(channel_id="@your_channel"))
```

## Развертывание

Следуйте инструкции в [`deployment/railway_guide.md`](deployment/railway_guide.md) для развертывания на Railway.

## Помощь

- 📖 [Полная документация](README.md)
- 🤝 [Как внести вклад](CONTRIBUTING.md)
- 🚀 [Развертывание](deployment/railway_guide.md)

---

**Удачной разработки! 🎯**
