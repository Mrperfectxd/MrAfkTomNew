from pyrogram.types import InlineKeyboardButton
import config
from ShrutiMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text="👻 ᴅᴇᴠᴇʟᴏᴘᴇʀ 👻", url="https://t.me/MrPerfectXd"),
            InlineKeyboardButton(text="🛡️ᴏᴜʀ ɢʀᴏᴜᴘs🛡️", url="https://t.me/Our_Groupps")
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="👻 ᴅᴇᴠᴇʟᴏᴘᴇʀ 👻", url="https://t.me/MrPerfectXd"),
            InlineKeyboardButton(text="🛡️ ᴏᴜʀ ɢʀᴏᴜᴘs 🛡️", url="https://t.me/Our_Groupps")
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")
        ],
    ]
    return buttons
