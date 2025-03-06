from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from keyboards.default.location_button import keyboard
from utils.misc.get_distance import choose_shortest
from loader import dp

@dp.callback_query_handler(text="mylocation")
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text="lokatsiya tasha ", reply_markup=keyboard)
# locatsiyaniki  sorab oladi yuborishini soreydi 




@dp.message_handler(content_types='location')
async def get_contact(message: Message):
    # locatsiyani taxliol qilib chiqadi 
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    
    #foydalanuvchi ma'lumotini olish 
    closest_shops = choose_shortest(location)

# locatsiyani olchab chiqadi 
    
    # yuboradigan text yozib chiqamiz qancha uzoq yoki yaqinligini 
    text = "\n\n".join([f"<a href='{url}'>{shop_name}</a>\n masofa: {distance:.1f} km."
                    for shop_name, distance, url, shop_location in closest_shops])

    
# locatsiyani jonatish eng yaqinini 
    await message.answer(f"rahmat\n"
                     f"Latitude = {latitude}\n"
                     f"longitude = {longitude}\n\n"
                     f"{text}", disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove())
    
    # har bir yaqin foydalanuvchiga jonatish 
    for shop_name, distance, url, shop_location in closest_shops:
        await message.answer_location(latitude=shop_location["lat"],
                                      longitude=shop_location["lon"])
        # sikil qilindi 