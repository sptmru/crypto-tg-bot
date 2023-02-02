import logging
from typing import Callable

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

logger = logging.getLogger("__name__")


def exception_handler(func: Callable) -> Callable:
    async def wrapper(*args, **kwargs):
        try:
            await func(*args, **kwargs)
        except:  # pylint: disable=bare-except
            logger.exception("Exception")
            arg0 = args[0]
            match arg0:
                case Message():  # type: ignore
                    message: Message = arg0
                    try:
                        await message.answer("Произошла неизвестная ошибка!")
                    except:
                        logger.exception("Exception")
                case CallbackQuery():  # type: ignore
                    message: Message = arg0.message
                    try:
                        await message.answer("Произошла неизвестная ошибка!")
                    except:
                        logger.exception("Exception")
                case _:
                    pass

    return wrapper


@exception_handler
async def cancel(
    call: CallbackQuery, button: Button, manager: DialogManager
):  # pylint: disable=unused-argument
    await call.message.delete()
    await call.message.answer("Отмена")
    await manager.done()
