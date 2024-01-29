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
    registration_button = InlineKeyboardButton(
        "Start Registration 🧲",
        callback_data="registration"
    )
    my_profile_button = InlineKeyboardButton(
        "Profile 🗒️",
        callback_data="my_profile"
    )
    view_profiles_button = InlineKeyboardButton(
        "View Profiles 🧑🏻‍💻",
        callback_data="view_profiles"
    )
    reference_button = InlineKeyboardButton(
        "Referral Menu 🐉",
        callback_data="reference_menu"
    )
    latest_news_button = InlineKeyboardButton(
        "Latest News 🗞️",
        callback_data="latest_news"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(view_profiles_button)
    markup.add(reference_button)
    markup.add(latest_news_button)
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


async def like_dislike_keyboard(owner):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Like 👍🏻",
        callback_data=f"like_{owner}"
    )
    dislike_button = InlineKeyboardButton(
        "Dislike 👎🏻",
        callback_data=f"dislike_{owner}"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup


async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    update_button = InlineKeyboardButton(
        "Update 💵",
        callback_data="update_profile"
    )
    delete_button = InlineKeyboardButton(
        "Delete ❌",
        callback_data="delete_profile"
    )
    markup.add(update_button)
    markup.add(delete_button)
    return markup

async def referral_keyboard():
    markup = InlineKeyboardMarkup()
    generate_button = InlineKeyboardButton(
        "Generate Link 🔗",
        callback_data="generate_link"
    )
    my_refs = InlineKeyboardButton(
        "My referrals",
        callback_data="my_r"
    )
    markup.add(generate_button)
    markup.add(my_refs)
    return markup