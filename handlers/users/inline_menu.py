from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.default import kb_menu, kb_test
from keyboards.inline import ikb_menu
from loader import dp

@dp.message_handler(text='inline')
async def inline_menu(message:types.Message):
    await message.answer('inline tugmalarni chiqarish',reply_markup=ikb_menu)

@dp.callback_query_handler(text='xabar')
async def xabar(call:CallbackQuery):
    await call.message.answer('tugmalar o`zgardi',reply_markup=kb_test)

@dp.callback_query_handler(text='alert')
async def alert(call: CallbackQuery):
    await call.answer('Bu alert xabar edi',show_alert=True)
