# keyboards/keyboard_factory.py

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def create_inline_keyboard(width: int, *args: str, **kwargs: str):
    """
    Создает инлайн-клавиатуру с заданными кнопками.

    :param width: Количество кнопок в одном ряду.
    :param args: Тексты для кнопок (callback_data будет сгенерирован как 'text:lower').
    :param kwargs: Пары "текст":"callback_data" для кнопок.
    :return: Объект инлайн-клавиатуры.
    """
    builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    if args:
        for button_text in args:
            callback_data = button_text.lower().replace(' ', '_')
            buttons.append(InlineKeyboardButton(text=button_text, callback_data=callback_data))
    
    if kwargs:
        for text, callback_data in kwargs.items():
            buttons.append(InlineKeyboardButton(text=text, callback_data=callback_data))

    builder.add(*buttons)
    builder.adjust(width)
    
    return builder.as_markup()
