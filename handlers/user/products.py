from aiogram import F,Router
from aiogram.types import Message,CallbackQuery
from keyboards.inline import products_inline,cart_keyboard
from filters.filter import RoleFilter

router=Router()

@router.message(lambda msg: msg.text == "Mahsulotlar")
async def show_products(message: Message, db):
    products = await db.get_products()
    await message.answer(
        "🛍 Mahsulotlar:",
        reply_markup=products_inline(products)
    )

@router.callback_query(F.data.startswith("adminproduct_"),RoleFilter("user"))
async def add_to_cart(call: CallbackQuery,db):

    product_id = int(call.data.split("_")[1])
    user_id = await db.get_user_id(call.from_user.id)

    await db.add_product_to_cart(int(user_id), product_id)

    await call.answer("Mahsulot savatchaga qo'shildi 🛒")

@router.message(F.text == "🛒 Savatcha")
async def show_cart(message: Message,db):
    user_id = await db.get_user_id(message.from_user.id)
    products = await db.get_cart_products(user_id)

    if not products:
        await message.answer("Savatcha bo'sh")
        return

    await message.answer(
        "Savatchangiz:",
        reply_markup=cart_keyboard(products)
    )