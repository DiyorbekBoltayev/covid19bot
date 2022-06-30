from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='10'),
            KeyboardButton(text='11'),
        ],
        [
            KeyboardButton(text='100'),
            KeyboardButton(text='111'),
        ],
        [
            KeyboardButton(text='biror bir matn'),
            KeyboardButton(text='inline'),
        ],
        [
            KeyboardButton(text='/menu')
        ]
    ],
    resize_keyboard=True
)