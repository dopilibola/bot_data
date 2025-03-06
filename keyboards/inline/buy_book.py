from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

book_keys = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            # locatsiya yoki contact tugmasini bosadigan narsa ekan 
            InlineKeyboardButton(text="locat", callback_data="mylocatior"),
            InlineKeyboardButton(text="contakt", callback_data="mycontact"),
        ],
    ]
)