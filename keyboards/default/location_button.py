from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# locatsiya yuboraadigan tugma 
keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="location ",
                                                      request_location=True)
                                   ]
                               ])