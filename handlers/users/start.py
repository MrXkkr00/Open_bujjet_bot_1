from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.default.main import bosh_menu, orqaga
from loader import dp, bot


class BoshState(StatesGroup):
    raqam = State()


@dp.message_handler(text="🏠 Orqaga")
@dp.message_handler(text="/start")
async def b4342432art(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(chat_id="6726542495", text=f"@{message.from_user.username} botga kirdi")
    f = open("./data/reklama", "r")
    text = f.read()
    if not str(user_id) in text:
        f = open("./data/reklama", "a")
        f.write(f"{user_id}\n")
        f.close()
    # photo = open("./data/bot2.jpg", "rb")
    havola_inline = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📮 Ovoz berish (Sayt)",
                                     url="https://openbudget.uz/boards/initiatives/initiative/48/95552946-f725-4e0b-b300-cd503f50c190"),
            ],
            [
                InlineKeyboardButton(text="📮 Ovoz berish (Telegram)",
                                     url="https://t.me/ochiqbudjet_1_bot?start=048359741003"),
            ],
        ], resize_keyboard=True
    )

    await message.answer(f"🎯 OpenBudget botiga xush kelibsiz.\n\n"
                         f"✅ Quyidagi tugmalardan birini tanlang\n\n"
                         "50 mingdan xar bir ovoz uchun 2 ta ovoz berganga kartasiga pul tushirib beriladi\n\n"


                         f"Овоз берганинггизни бизга юборинг ва сизга пулни ўтказиб берамиз!"
                         f" ✅🤗\n\n"

                         f"Тг:  @Baxodir2024\n\n"


                         f"Tel: +998993002018\n\n"

                         f"Karta, Click yoki payme💳‼️‼️\n"
                         f"👇🏽👇🏽👇🏽👇🏽\n"
                         f"https://t.me/Open_Budget_rasmiyuz_bot"
                         , reply_markup=havola_inline)
    await message.answer(f"Botdan foydalanish.", reply_markup=bosh_menu)


@dp.message_handler(text="📮 Ovoz berish")
async def dasfadsfas(message: types.Message):
    havola_inline = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📮 Ovoz berish (Sayt)",
                                     url="https://openbudget.uz/boards/initiatives/initiative/48/95552946-f725-4e0b-b300-cd503f50c190"),
            ],
            [
                InlineKeyboardButton(text="📮 Ovoz berish (Telegram)",
                                     url="https://t.me/ochiqbudjet_1_bot?start=048359741003"),
            ],
        ], resize_keyboard=True
    )

    await message.answer(f"🎯 OpenBudget botiga xush kelibsiz.\n\n"
                         f"✅ Quyidagi tugmalardan birini tanlang\n\n"
                         "50 mingdan xar bir ovoz uchun 2 ta ovoz berganga kartasiga pul tushirib beriladi\n\n"
    
    
                         f"Овоз берганинггизни бизга юборинг ва сизга пулни ўтказиб берамиз!"
                         f" ✅🤗\n\n"
    
                         f"Тг:  @Baxodir2024\n\n"
    
                         f"Tel: +998993002018\n\n"
    
                         f"Karta, Click yoki payme💳‼️‼️\n"
                         f"👇🏽👇🏽👇🏽👇🏽\n"
                         f"https://t.me/Open_Budget_rasmiyuz_bot"
                         , reply_markup=havola_inline)
    await message.answer(f"Botdan foydalanish.", reply_markup=bosh_menu)
# async def ovoz_berish(message: types.Message):
#     await message.answer(f"📞 Telefon raqamingizni kiriting:\n\n"
#                          f"✅ Namuna: +998931234567", reply_markup=orqaga)
#     await BoshState.raqam.set()


@dp.message_handler(lambda message: len(message.text) == 13 and message.text[:4] == "+998", state=BoshState.raqam)
async def ovoz_berish_raqam(message: types.Message, state: FSMContext):
    havola_inline = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📮 Ovoz berish (Sayt)",
                                     url="https://openbudget.uz/boards/initiatives/initiative/48/95552946-f725-4e0b-b300-cd503f50c190"),
            ],
            [
                InlineKeyboardButton(text="📮 Ovoz berish (Telegram)",
                                     url="https://t.me/ochiqbudjet_1_bot?start=048359741003"),
            ],
        ], resize_keyboard=True
    )

    await message.answer(f"📞 Telefon raqam qabul qilindi.\n\n"
                         f"📲 Havola orqali kirib ovoz bering", reply_markup=havola_inline)
    await message.answer(f"Botdan foydalanish.", reply_markup=bosh_menu)
    await state.finish()



