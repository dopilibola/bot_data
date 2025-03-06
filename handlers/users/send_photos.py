from aiogram import types 
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile
from keyboards.inline.buy_book import book_keys
from loader import dp, bot

# rasmni olib data basega qoshidanigan funksiya 
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)

# video olib data basega qoshidanigan funksiya 
@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)

# kitob degan sozni yozgandan keyin rasm chiqarib beradi va 2ta tugma chiqarib beradi 
# koment olinganlari xar xil yol bilan bo'lgan narsalar 
@dp.message_handler(Command("kitob"))
async def send_foto(message: types.Message):
    # rasmni 3 xil orqali yuborsa boladi id url va file url ruxsat berilishi kerak bomasa no
    # photo_id = "AgACAgIAAxkBAAIEzmfHCx9WB26RmjbYVxqKYdTtaq3GAAKp6jEbQi04Ss0skOUDdyEeAQADAgADeQADNgQ"
    # photo_url = ""
    photo_file = InputFile(path_or_bytesio="photo/123.jpg")
    # rasm xoxlagan tarzda yuborish mumkun /kitob jonatganda 
    msg = "<b>dsadsadssadsdsda</b>\n"
    msg += "<b>dasadsafasfsfwre</b>\n\n"
    await message.reply_photo(photo_file, caption=msg, reply_markup=book_keys)

    # await message.reply_photo(photo_id, caption="123")
    # await message.answer_photo(photo_id, caption="123")
    # await bot.send_photo(chat_id=message.from_user.id, photo=photo_id,
    #                      caption="qweqewqeqw")






# @dp.message_handler(Command("kurslar"))
# async def send_courses(message: types.Message):
#     album = types.MediaGroup()
#     photo1 = "AgACAgIAAxkBAAIEzmfHCx9WB26RmjbYVxqKYdTtaq3GAAKp6jEbQi04Ss0skOUDdyEeAQADAgADeQADNgQ"
#     photo2 = "AgACAgIAAxkBAAIEzmfHCx9WB26RmjbYVxqKYdTtaq3GAAKp6jEbQi04Ss0skOUDdyEeAQADAgADeQADNgQ"
#     photo3 = "AgACAgIAAxkBAAIEzmfHCx9WB26RmjbYVxqKYdTtaq3GAAKp6jEbQi04Ss0skOUDdyEeAQADAgADeQADNgQ"
#     album.attach_photo(photo=photo1)
#     album.attach_photo(photo=photo2)
#     album.attach_photo(photo=photo3, caption="qweqewqeqw")

#     await message.reply_media_group(media=album)
    

    