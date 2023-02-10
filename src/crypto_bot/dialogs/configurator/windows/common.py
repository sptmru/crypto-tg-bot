import logging
from typing import Callable

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const

import src.crypto_bot.messages.dialogs.configurator.windows as messages

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
                        await message.answer(messages.unknown_error())
                    except:
                        logger.exception("Exception")
                case CallbackQuery():  # type: ignore
                    message: Message = arg0.message
                    try:
                        await message.answer(messages.unknown_error())
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
    await call.message.answer(messages.cancel_text())
    await manager.done()


def get_back_cancel_keyboard(
    window_name: str, on_back: Callable | None = None, show_back: bool = True
) -> Row:
    if show_back:
        row = Row(
            Button(
                Const(messages.back_text()), id=f"{window_name}_back", on_click=on_back
            ),
            Button(
                Const(messages.cancel_text()),
                id=f"{window_name}_cancel",
                on_click=cancel,
            ),
        )
    else:
        row = Row(
            Button(
                Const(messages.cancel_text()),
                id=f"{window_name}_cancel",
                on_click=cancel,
            ),
        )
    return row
