import logging

import pyrogram
from tgtlg import AUTH_CHANNEL, LOGGER

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(
            f"""<b>Not Authorized to be here.</b>\n\n<b>Current Chat ID: <code>{message.chat.id}</code>""", parse_mode="html")
        # leave chat
        await client.leave_chat(chat_id=message.chat.id, delete=True)
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
     await message.reply_text("no one gonna help you 🤣🤣🤣🤣", quote=True)
     channel_id = str(AUTH_CHANNEL)[4:]
     message_id = 99
