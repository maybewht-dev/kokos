from aiogram import types
from dispatcher import dp, bot
import sqlite3

@dp.message_handler(text=['установка приветствия', 'Установка приветствия', 'установка приветствий', 'Установка приветствий'])
async def greeting_installing(message: types.Message):
    await message.answer(f"""Полная инструкция по установке приветствия тут:
truepixel.ru/docs/kokos""")



@dp.message_handler(commands=['приветствие', 'Приветствие'], commands_prefix="+")
async def add_greeting(message: types.Message):
    if message.chat.type != 'private':
        try:
            db = sqlite3.connect('chapcha_data_base.db')
            c = db.cursor()
            c.execute("INSERT INTO chat_data VALUES (?, ?, ?, ?, ?)",
                      (message.chat.id, '<b>- {имя} добро пожаловать в чат!</b>', '', '1', 'NO'))
            db.commit()
            db.close()
        except:
            pass
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        gc = True
        try:
            com = message.text[13:]
            img = com.split(' ')[-1]
            lll = len(img) + 1
            text = com[:-lll]
            c.execute(f"UPDATE chat_data SET chat_welcome_text = '{text}', chat_welcome_image = '{img}' WHERE chat_id = {message.chat.id}")
            await message.answer("✅ Приветствие установлено!")
        except:
            await message.answer("+приветствие Текст Число/Ссылка")
        db.commit()
        db.close()
    else:
        await message.answer("Приветствия недоступны в лс кокоса")

@dp.message_handler(commands=['приветствие', 'Приветствие'], commands_prefix="-")
async def del_greeting(message: types.Message):
    if message.chat.type != 'private':
        try:
            db = sqlite3.connect('chapcha_data_base.db')
            c = db.cursor()
            c.execute("INSERT INTO chat_data VALUES (?, ?, ?, ?, ?)",
                      (message.chat.id, '<b>- {имя} добро пожаловать в чат!</b>', '', '1', 'NO'))
            db.commit()
            db.close()
        except:
            pass
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        gc = True
        try:
            c.execute(f"UPDATE chat_data SET chat_welcome_text = 'Отсутствует', chat_welcome_image = '0' WHERE chat_id = {message.chat.id}")
            await message.answer("❎ Приветствие удалено!")
        except:
            pass
        db.commit()
        db.close()
    else:
        await message.answer("Приветствия недоступны в лс кокоса")

@dp.message_handler(commands=['приветствие', 'Приветствие', ' приветствие', ' Приветствие'], commands_prefix="!./")
async def greeting(message: types.Message):
    if message.chat.type != 'private':
        try:
            db = sqlite3.connect('chapcha_data_base.db')
            c = db.cursor()
            c.execute("INSERT INTO chat_data VALUES (?, ?, ?, ?, ?)",
                      (message.chat.id, '<b>- {имя} добро пожаловать в чат!</b>', '', '1', 'NO'))
            db.commit()
            db.close()
        except:
            pass
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        gc = True
        try:
            c.execute(f"SELECT chat_welcome_text, chat_rules, chat_welcome_image FROM chat_data WHERE chat_id = {message.chat.id}")
            items = c.fetchall()
            for el in items:
                cwt = el[0]
                cr = el[1]
                cwi = el[2]
            if cwi == '0' and cwt != "Отсутствует":
                await message.answer(cwt, parse_mode="HTML")
                gc = False
            elif cwi == '1':
                img_url = 'https://i.imgur.com/g5vLRJ2.jpeg'
            elif cwi == '2':
                img_url = 'https://i.imgur.com/g5vLRJ2.jpeg'
            elif cwi == '3':
                img_url = 'https://i.imgur.com/g5vLRJ2.jpeg'
            elif cwi == '4':
                img_url = 'https://i.imgur.com/g5vLRJ2.jpeg'
            elif cwi == '5':
                img_url = 'https://i.imgur.com/g5vLRJ2.jpeg'
            elif cwi == '6':
                img_url = 'https://i.imgur.com/g5vLRJ2.jpeg'
            elif cwi == '7':
                img_url = 'https://i.imgur.com/g5vLRJ2.jpeg'
            elif cwi == '8':
                img_url = 'https://i.imgur.com/g5vLRJ2.jpeg'
            elif cwi == '9':
                img_url = 'https://i.imgur.com/g5vLRJ2.jpeg'
            elif cwi == '10':
                img_url = 'https://i.imgur.com/g5vLRJ2.jpeg'
            elif cwi == '11':
                img_url = 'https://i.imgur.com/g5vLRJ2.jpeg'
            elif cwi == '12':
                img_url = 'https://i.imgur.com/g5vLRJ2.jpeg'
            elif cwi == '13':
                img_url = 'https://i.imgur.com/g5vLRJ2.jpeg'
            elif cwi == '14':
                img_url = 'https://i.imgur.com/g5vLRJ2.jpeg'
            elif cwi == '15':
                img_url = 'https://i.imgur.com/g5vLRJ2.jpeg'
            else:
                img_url = cwi
            if gc and cwt != "отсутствует":
                try:
                    await message.answer(f"🗓 Приветствие:<a href='{img_url}'> </a>\n{cwt}", parse_mode="HTML")
                except:
                    await message.answer(f"🗓 Приветствие:\n{cwt}")
            elif gc and cwt == "Отсутствует":
                await message.answer("🗓 Приветствие отсутствует")
        except:
            await message.answer("Пропишите эту команду в группе с ботом")
        db.commit()
        db.close()
    else:
        await message.answer("Приветствия недоступны в лс кокоса")