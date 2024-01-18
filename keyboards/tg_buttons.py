from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Questionnaire 🔥",
        callback_data="start_questionnaire"
    )
    check_ban_button = InlineKeyboardButton(
        "Check Ban Status",
        callback_data="check_ban_status"
    )
    markup.add(questionnaire_button)
    markup.add(check_ban_button)
    return markup



async def questionnaire_first_answers():
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "Python 🐍",
        callback_data="python2"
    )
    mojo_button = InlineKeyboardButton(
        "Mojo 🔥",
        callback_data="mojo"
    )



    markup.add(python_button)
    markup.add(mojo_button)
    return markup


async def football_button():
        return InlineKeyboardButton(
            "Football ⚽️",
            callback_data="football"
        )

async def basketball_answers():
    return InlineKeyboardButton(
        "Basketball 🏀",
        callback_data="basketball"
    )

async def iphone_button():
    return InlineKeyboardButton(
        "iPhone 📱",
        callback_data="iphone"
    )

async def samsung_button():
    return InlineKeyboardButton(
        "Samsung 📱",
        callback_data="samsung"
    )



async def questionnaire_second_answers():
    markup = InlineKeyboardMarkup()
    football_button = InlineKeyboardButton(
            "Football ⚽️",
            callback_data="football"
        )
    basketball_button = InlineKeyboardButton(
        "Basketball 🏀",
        callback_data="basketball"
    )
    markup.add(football_button)
    markup.add(basketball_button)
    return markup


async def questionnaire_third_answers():
    markup = InlineKeyboardMarkup()
    iphone_button = InlineKeyboardButton(
        "iPhone 📱",
        callback_data="iphone"
    )
    samsung_button = InlineKeyboardButton(
        "Samsung 📱",
        callback_data="samsung"
    )
    markup.add(iphone_button)
    markup.add(samsung_button)
    return markup