from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_test=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='10'),
            KeyboardButton(text='11'),
        ],
        [
            KeyboardButton(text='/menu')
        ]
    ],
    resize_keyboard=True
)