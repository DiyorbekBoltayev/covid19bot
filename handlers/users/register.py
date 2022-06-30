import types

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from states import register
from loader import dp

@dp.message_handler(Command('register')) #==/register
async def register_1(message:types.Message):
    await message.answer("Ro'yhatdan o'tish boshlandi ! \n Iltimos Ism Familyangizni kiriting : ")
    await register.test1.set()

@dp.message_handler(state=register.test1,)
async def state1(message: types.Message, state:FSMContext):
    answer=message.text

    await state.update_data(test1=answer)
    await message.answer(f'{answer} Yoshingiz nechchida ?')
    await register.test2.set()

@dp.message_handler(state=register.test2,)
async def state1(message: types.Message, state:FSMContext):
    answer = message.text

    await state.update_data(test2=answer)
    dat= await state.get_data()
    name=dat.get('test1')
    age=dat.get('test2')
    await state.get_data('test2')
    await message.answer(f"Ro'yhatdan o'tish muvaffaqqiyatli amalga oshirildi ! \n"
                         f"Sizning ismingiz: {name} \n"
                         f"Sizning yoshingiz: {age} \n")
    await state.finish()
