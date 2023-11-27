from aiogram import types
from dispatcher import dp, bot
from aiogram.utils import executor
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from bs4 import BeautifulSoup
import requests


async def get_joke():
    joke_html = requests.get('https://nekdo.ru/random/').text
    joke_text = BeautifulSoup(joke_html, 'lxml').find('div', class_='text').get_text()
    return joke_text


@dp.message_handler(text=['кокос анекдот', 'кокос расскажи анекдот', 'кокос пошути', 'кокос расскажи шутку', 'Кокос анекдот', 'Кокос расскажи анекдот', 'Кокос пошути', 'Кокос расскажи шутку'])
async def joke(message: types.Message):
    text = await get_joke()
    await message.answer(text)