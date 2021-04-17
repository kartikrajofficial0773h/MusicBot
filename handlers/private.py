from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Dear {message.from_user.first_name}!

😁 I am KINGBOT Music Player. 

🥳 I can play music in your Telegram Group's Voice Chat😉

Developed by ⚡ @Kartikrajofficial ⚡

My commands - /play, /stop, /skip, /pause, /resume, which work in grp

Thanks for using .

Regrards [KINGBOT](https://t.me/KINGBOTOFFICIAL)
**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 DEPLOY LINK🛠", url="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fkartikrajofficial%2FMusicBot&template=https%3A%2F%2Fgithub.com%2Fkartikrajofficial%2FMusicBot")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/KINGBOTOFFICIALCHAT"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/KINGBOTOFFICIAL"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/KINGBOTMUSICBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**⭐KINGBOT MUSIC PLAYER IS ALWAYS ACTIVE!!⭐**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/KINGBOTOFFICIAL")
                ]
            ]
        )
   )
