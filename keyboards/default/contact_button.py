from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# contact yuboradigan tugmacha 
keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="contact",
                                                      request_contact=True)
                                   ]
                               ])