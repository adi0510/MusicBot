from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>
I am  Music Player  bot that lets you play music in your Telegram groups.
Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ Commands", url="https://telegra.ph/AAdi-03-17"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/trhofficial"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/teamroargaming"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters2)
async def start2(_, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
