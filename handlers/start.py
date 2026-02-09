from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.types import Message
from keyboards.reply import start_reply,register_reply

router=Router()

@router.message(CommandStart())
async def start_handler(msg:Message,db):
    if await db.is_user_exists(msg.from_user.id):
        await msg.answer(f"Assalomu Alaykum {msg.from_user.full_name}, botga xush kelibsiz",reply_markup=start_reply())
    else:
        await msg.answer(f"Assalomu Alaykum {msg.from_user.full_name}, botga xush kelibsiz",reply_markup=register_reply())