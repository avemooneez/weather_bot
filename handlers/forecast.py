from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from keyboards import main
from db import Database
import requests


router = Router()
db = Database("./database.db")

@router.message(F.location)
async def give_forecast(message: Message):
    await message.answer(f"{message.location.latitude, message.location.longitude}")
