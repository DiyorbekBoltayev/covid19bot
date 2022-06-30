from aiogram import types



from loader import dp


@dp.message_handler()
async def command_error(message: types.Message):
    await message.answer(f"Kechirasiz , {message.from_user.full_name}!\n"
                         f"{message.text} buyrug'u mavjud emas")