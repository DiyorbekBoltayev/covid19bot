from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu=InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text='xabar',callback_data='xabar'),
        InlineKeyboardButton(text='link',url="https://www.youtube.com/watch?v=2Il_Ab-s0W8&ab_channel=Redly"),
    ],
    [
        InlineKeyboardButton(text='alert',callback_data='alert')
    ]
])