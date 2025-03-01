from loader import dp, bot 
from aiogram.types import ContentType, Message
from pathlib import Path
# fideo file audio bitta joyga yigadiigan hk narsa 
download_path = Path().joinpath("dowloads", "categories")
download_path.mkdir(parents=True, exist_ok=True)

@dp.message_handler()
async def text_hendler(message: Message):
    await message.reply("siz matin yubordiz")


@dp.message_handler(content_types=ContentType.DOCUMENT)
async def doc_handler(message: Message):
    await message.document.download(destination=download_path)
    doc_id = message.document.file_id
    await message.reply("siz document yubordiz\n"
                        f"file_id = {doc_id}")
    

# @dp.message_handler(content_types=ContentType.VIDEO)
@dp.message_handler(content_types='video')
async def video_handler(message: Message):
    await message.video.download(destination=download_path)
    # doc_id = message.document.file_id
    await message.reply("siz video yubordiz\n"
                        f"file_id = {message.video.file_id}")


@dp.message_handler(content_types='photo')
async def photo_handler(message: Message):
    await message.photo[-1].download(destination=download_path)
    # doc_id = message.document.file_id
    await message.reply("siz rasm yubordiz\n"
                        f"file_id = {message.photo[-1].file_id}")
    
@dp.message_handler(content_types=ContentType.ANY)
async def any_handler(message: Message):
    await message.reply(f"{message.content_type} qabul qilindi")