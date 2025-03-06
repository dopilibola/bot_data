from aiogram import types
from loader import dp

@dp.inline_handler()
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="kurs001",
                title="vbhbhd", 
                input_message_content=types.InputTextMessageContent(
                    message_text="trhtrnhjrnhjtrnjkhtrenkhnrekjhnenhjtrhjtrhjtrnhrt"
                ),
                # url  url yozsa bo'ladi 
                # thumb_url link 
                # description text
            )
        ]
    )