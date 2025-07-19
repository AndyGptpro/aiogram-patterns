#!/usr/bin/env python3
"""
Пример бота, демонстрирующий использование всех паттернов из репозитория.

Этот файл НЕ предназначен для запуска как есть - это демонстрация интеграции
всех паттернов в один проект.

Для запуска:
1. Создайте файл .env с BOT_TOKEN=your_bot_token
2. Установите зависимости: pip install -r requirements.txt
3. Замените YOUR_CHANNEL_ID на реальный ID канала
4. Запустите: python example_bot.py
"""

import asyncio
import logging
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery

# Импорты наших паттернов
from keyboards.keyboard_factory import create_inline_keyboard
from fsm_states.survey_states import UserSurvey
from middlewares.subscription import ChannelSubscriptionMiddleware

# Загружаем переменные окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Получаем токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в переменных окружения!")

# ID канала для проверки подписки (замените на ваш)
YOUR_CHANNEL_ID = "@your_channel"  # или -1001234567890

# Инициализируем бота и диспетчер
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher(storage=MemoryStorage())

# Регистрируем middleware для проверки подписки
# Раскомментируйте строку ниже, если хотите включить проверку подписки
# dp.message.middleware(ChannelSubscriptionMiddleware(channel_id=YOUR_CHANNEL_ID))


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    """Обработчик команды /start с демонстрацией фабрики клавиатур."""
    
    # Используем паттерн создания клавиатур
    main_menu = create_inline_keyboard(
        width=2,
        # Аргументы создадут кнопки с автоматическими callback_data
        "Профиль", "Помощь",
        # kwargs для точного управления callback_data
        настройки="settings_menu",
        опрос="start_survey"
    )
    
    await message.answer(
        f"👋 <b>Добро пожаловать, {message.from_user.full_name}!</b>\n\n"
        "Этот бот демонстрирует использование паттернов aiogram 3.x.\n"
        "Выберите действие:",
        reply_markup=main_menu
    )


@dp.callback_query(lambda c: c.data == "профиль")
async def profile_callback(callback: CallbackQuery) -> None:
    """Обработчик кнопки 'Профиль'."""
    user = callback.from_user
    
    profile_info = (
        f"👤 <b>Ваш профиль:</b>\n\n"
        f"🆔 ID: <code>{user.id}</code>\n"
        f"👤 Имя: {user.full_name}\n"
        f"🔗 Username: @{user.username or 'не указан'}\n"
        f"🌐 Язык: {user.language_code or 'не определен'}"
    )
    
    back_keyboard = create_inline_keyboard(1, "🔙 Назад", назад="back_to_menu")
    
    await callback.message.edit_text(profile_info, reply_markup=back_keyboard)
    await callback.answer()


@dp.callback_query(lambda c: c.data == "помощь")
async def help_callback(callback: CallbackQuery) -> None:
    """Обработчик кнопки 'Помощь'."""
    help_text = (
        "❓ <b>Помощь по боту:</b>\n\n"
        "🤖 Этот бот демонстрирует паттерны aiogram 3.x:\n\n"
        "• <b>Фабрика клавиатур</b> - быстрое создание кнопок\n"
        "• <b>FSM состояния</b> - пошаговые диалоги\n"
        "• <b>Middleware</b> - проверка подписки на канал\n\n"
        "📖 Исходный код: github.com/your-username/telegram-bot-patterns"
    )
    
    back_keyboard = create_inline_keyboard(1, "🔙 Назад", назад="back_to_menu")
    
    await callback.message.edit_text(help_text, reply_markup=back_keyboard)
    await callback.answer()


@dp.callback_query(lambda c: c.data == "start_survey")
async def start_survey_callback(callback: CallbackQuery, state: FSMContext) -> None:
    """Начинаем опрос с использованием FSM состояний."""
    await callback.message.edit_text(
        "📝 <b>Начинаем опрос!</b>\n\n"
        "Как вас зовут?"
    )
    
    # Устанавливаем первое состояние FSM
    await state.set_state(UserSurvey.waiting_for_name)
    await callback.answer()


@dp.message(UserSurvey.waiting_for_name)
async def process_name(message: Message, state: FSMContext) -> None:
    """Обрабатываем имя пользователя."""
    # Сохраняем имя в состоянии
    await state.update_data(name=message.text)
    
    await message.answer(
        f"👋 Приятно познакомиться, <b>{message.text}</b>!\n\n"
        "Сколько вам лет? (введите число)"
    )
    
    # Переходим к следующему состоянию
    await state.set_state(UserSurvey.waiting_for_age)


@dp.message(UserSurvey.waiting_for_age)
async def process_age(message: Message, state: FSMContext) -> None:
    """Обрабатываем возраст пользователя."""
    try:
        age = int(message.text)
        if age <= 0 or age > 150:
            raise ValueError()
            
        # Сохраняем возраст
        await state.update_data(age=age)
        
        # Получаем все данные из состояния
        data = await state.get_data()
        
        # Создаем клавиатуру для подтверждения
        confirm_keyboard = create_inline_keyboard(
            width=2,
            подтвердить="confirm_survey",
            заново="restart_survey"
        )
        
        await message.answer(
            f"✅ <b>Проверьте ваши данные:</b>\n\n"
            f"👤 Имя: {data['name']}\n"
            f"🎂 Возраст: {age} лет\n\n"
            "Все верно?",
            reply_markup=confirm_keyboard
        )
        
        # Переходим к состоянию подтверждения
        await state.set_state(UserSurvey.waiting_for_confirmation)
        
    except ValueError:
        await message.answer(
            "❌ Пожалуйста, введите корректный возраст (число от 1 до 150)"
        )


@dp.callback_query(lambda c: c.data == "confirm_survey", UserSurvey.waiting_for_confirmation)
async def confirm_survey(callback: CallbackQuery, state: FSMContext) -> None:
    """Подтверждаем данные опроса."""
    data = await state.get_data()
    
    # Очищаем состояние
    await state.clear()
    
    # Создаем клавиатуру для возврата в главное меню
    back_keyboard = create_inline_keyboard(1, "🏠 Главное меню", главное_меню="back_to_menu")
    
    await callback.message.edit_text(
        f"🎉 <b>Спасибо за участие в опросе!</b>\n\n"
        f"📊 Ваши данные сохранены:\n"
        f"👤 Имя: {data['name']}\n"
        f"🎂 Возраст: {data['age']} лет\n\n"
        f"✨ Опрос завершен успешно!",
        reply_markup=back_keyboard
    )
    await callback.answer("✅ Данные сохранены!")


@dp.callback_query(lambda c: c.data == "restart_survey")
async def restart_survey(callback: CallbackQuery, state: FSMContext) -> None:
    """Перезапускаем опрос."""
    await state.clear()
    await start_survey_callback(callback, state)


@dp.callback_query(lambda c: c.data == "back_to_menu")
async def back_to_menu(callback: CallbackQuery, state: FSMContext) -> None:
    """Возврат в главное меню."""
    # Очищаем состояние на всякий случай
    await state.clear()
    
    main_menu = create_inline_keyboard(
        width=2,
        "Профиль", "Помощь",
        настройки="settings_menu",
        опрос="start_survey"
    )
    
    await callback.message.edit_text(
        f"🏠 <b>Главное меню</b>\n\n"
        "Выберите действие:",
        reply_markup=main_menu
    )
    await callback.answer()


async def main() -> None:
    """Основная функция для запуска бота."""
    try:
        # Удаляем webhook (если был установлен)
        await bot.delete_webhook(drop_pending_updates=True)
        
        # Запускаем long polling
        logging.info("🚀 Бот запущен!")
        await dp.start_polling(bot)
        
    except Exception as e:
        logging.error(f"❌ Ошибка при запуске бота: {e}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        # Проверяем наличие токена
        if not BOT_TOKEN:
            print("❌ Ошибка: BOT_TOKEN не найден!")
            print("Создайте файл .env и добавьте: BOT_TOKEN=your_bot_token")
            exit(1)
        
        # Запускаем бота
        asyncio.run(main())
        
    except KeyboardInterrupt:
        print("\n👋 Бот остановлен пользователем")
    except Exception as e:
        print(f"💥 Критическая ошибка: {e}")
        exit(1)
