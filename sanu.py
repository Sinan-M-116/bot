import os

from pyrogram import Client, filters

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Pr0fess0r_99= Client(

    "Welcome-Bot",

     bot_token = os.environ["BOT_TOKEN"],

     api_id = int(os.environ["API_ID"]),

     api_hash = os.environ["API_HASH"]

)

@bots_sinan.on_message(filters.command("start"))

async def start(client: Pr0fess0r_99, update):

    start_msg = "👋Hy {}, Iam Simple  Welcome Bot\n\nBot Owner Only /admin\n\nMaintained By @sinzz_botz"

    bot_username = await client.get_me()

    link = "SinzzBotz/10"

    reply_markup = InlineKeyboardMarkup(

        [             

            [

                InlineKeyboardButton

                    (

                         "🤖More Bots", url="t.me/SinzzBotz/12"

                    ),

                InlineKeyboardButton

                    (

                         "🎉 Open Source", url="https://t.me/sinzzbotz/12" # sinan-m-116/Welcome-Bot-sinzz

                    )

            ],   

            [

                InlineKeyboardButton

                   (

                        "➕️ Add Me To Your Chats ➕️", url=f"http://t.me/{bot_username.username}?startgroup=botstart"

                   )

            ]

        ] 

    )                       

    await update.reply_text(

        text=start_msg.format(update.from_user.mention), reply_markup=reply_markup)

print("""Auto Welcome Bot Started

Maintained By @sinzzbotz""")

Pr0fess0r_99.run()

print("""Auto Welcome Bot Started

Maintained By @sinzzbotz""")

bots_sinan.run()
