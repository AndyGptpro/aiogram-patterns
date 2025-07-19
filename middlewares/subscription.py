# middlewares/subscription.py

from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

class ChannelSubscriptionMiddleware(BaseMiddleware):
    """
    Middleware для проверки подписки пользователя на обязательный канал.
    """
    def __init__(self, channel_id: str | int):
        self.channel_id = channel_id

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        
        bot = data['bot']
        
        try:
            member = await bot.get_chat_member(chat_id=self.channel_id, user_id=event.from_user.id)
            # Пропускаем, если пользователь подписан, является админом или создателем
            if member.status in ['member', 'administrator', 'creator']:
                return await handler(event, data)
        except Exception as e:
            # Обработка случая, если бот не админ в канале или канал указан неверно
            print(f"Ошибка проверки подписки: {e}")
            await event.answer("Возникла техническая проблема. Пожалуйста, попробуйте позже.")
            return

        # Если пользователь не подписан
        channel_info = await bot.get_chat(self.channel_id)
        invite_link = await channel_info.export_invite_link()
        await event.answer(
            f"Для доступа к боту, пожалуйста, подпишитесь на наш канал.\n\n"
            f"Ссылка на канал: {invite_link}"
        )
        return
