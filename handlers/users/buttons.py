from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(text='10')
async def cmd_10(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n"
                         f"Siz tanlagan raqam {message.text}")

@dp.message_handler(text='11')
async def cmd_11(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n"
                         f"Siz tanlagan raqam {message.text}")

@dp.message_handler(text='100')
async def cmd_100(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n"
                         f"Siz tanlagan raqam {message.text}")
