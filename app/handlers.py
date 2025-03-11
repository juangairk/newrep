
from aiogram import F,Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart,Command
import app.keyboards as kb
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext


router = Router()

class Register (StatesGroup):
    name = State()
    age = State()
    number = State()


@router.message(CommandStart())
async  def cmd_start(message:Message):
    await message.answer('privet', reply_markup=kb.main)
    await message.reply('hihihi')

@router.message(Command('help'))
async def cmd_help(message:Message):
    await message.answer("can i help you")

@router.message(F.text == "Каталог")
async def cmd_nice(message:Message):
    await message.answer("Выберите категорию товара",reply_markup=kb.catalog)

@router.callback_query(F.data == 'tshirt')
async def tshirt(callback : CallbackQuery):
    await callback.answer('вы выбрали категорию',show_alert=True)
    await callback.message.answer('Вы выбрали футболки')

@router.message(Command('register'))
async def register (message:Message,state : FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя')

@router.message(Register.name)
async def register (message:Message,state : FSMContext):
    await  state.update_data(name=message.text )
    await state.set_state(Register.age)
    await  message.answer('Введите возраст')

@router.message (Register.age)
async def register_age(message: Message, state: FSMContext):
    await  state.update_data(age=message.text)
    await state.set_state(Register.number)
    await  message.answer('Ваш номер телефона',reply_markup=kb.get_number)

@router.message (Register.number,F.contact)
async def register_number (message:Message,state: FSMContext):
    await state.update_data(number= message.contact.phone_number)
    data = await  state.get_data()
    await message.answer(f"Ваше имя: {data['name']}\nВаш возраст: {data['age']}\nНомер: {data['number']}")
    await state.clear()
