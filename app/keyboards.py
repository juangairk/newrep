from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,
                           InlineKeyboardButton,InlineKeyboardMarkup
                           )


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text="Корзина")],
                                     [KeyboardButton(text="Контакты"),
                                     KeyboardButton(text="О нас")]],
                           resize_keyboard=True,
                           input_field_placeholder="Выберите пункт меню")

catalog = InlineKeyboardMarkup(inline_keyboard=
                [[InlineKeyboardButton(text='Футболки',callback_data='tshirt')],
                [InlineKeyboardButton(text='Кроссовки',callback_data='sneakers')],
                [InlineKeyboardButton(text='Кепки',callback_data='cap')]])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='отправить номер',
                                                           request_contact=True)]],
                                 resize_keyboard=True)