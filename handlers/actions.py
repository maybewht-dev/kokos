from aiogram import types
from dispatcher import dp
from aiogram.dispatcher.filters import Text

@dp.message_handler(text=['Кокос действия', 'Действия', 'кокос действия', 'действия'])
async def hit(message: types.Message):
    await message.answer("""<b>Список действий</b>

ударить
погладить
дать пять
обнять
избить
убить
поцеловать""", parse_mode="HTML")

@dp.message_handler(Text(startswith=['Ударить', 'ударить']))
async def hit(message: types.Message):
    com = message.text[8:]
    if com.find('''
''') == 0:
        com = com[1:]
    try:
        if com == '':
            await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> ударил(а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>', parse_mode="HTML")
        else:
            await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> ударил(а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\nИ сказал(а): {com}', parse_mode="HTML")
    except:
        pass

@dp.message_handler(Text(startswith=['Погладить', 'погладить']))
async def pogl(message: types.Message):
    com = message.text[10:]
    if com.find('''
''') == 0:
        com = com[1:]
    try:
        if com == '':
            await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> погладил(а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>', parse_mode="HTML")
        else:
            await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> погладил(а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\nИ сказал(а): {com}', parse_mode="HTML")
    except:
        pass

@dp.message_handler(Text(startswith=['Изнасиловать', 'изнасиловать']))
async def pogl(message: types.Message):
    com = message.text[13:]
    if com.find('''
''') == 0:
        com = com[1:]
    try:
        if com == '':
            await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> изнасиловал(а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>', parse_mode="HTML")
        else:
            await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> изнасиловал(а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\nИ сказал(а): {com}', parse_mode="HTML")
    except:
        pass

@dp.message_handler(Text(startswith=['Избить', 'избить']))
async def pogl(message: types.Message):
    com = message.text[7:]
    if com.find('''
''') == 0:
        com = com[1:]
    try:
        if com == '':
            await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> избил(а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>', parse_mode="HTML")
        else:
            await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> избил(а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\nИ сказал(а): {com}', parse_mode="HTML")
    except:
        pass

@dp.message_handler(Text(startswith=['Поцеловать', 'поцеловать']))
async def pogl(message: types.Message):
    com = message.text[9:]
    if com.find('''
''') == 0:
        com = com[1:]
    try:
        if com == '':
            await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> поцеловал(а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>', parse_mode="HTML")
        else:
            await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> поцеловал(а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\nИ сказал(а): {com}', parse_mode="HTML")
    except:
        pass

@dp.message_handler(Text(startswith=['Дать пять', 'Дать пять']))
async def pogl(message: types.Message):
    com = message.text[10:]
    if com.find('''
''') == 0:
        com = com[1:]
    try:
        if com == '':
            await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> дал(а) пять <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>', parse_mode="HTML")
        else:
            await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> дал(а) пять <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\nИ сказал(а): {com}', parse_mode="HTML")
    except:
        pass

@dp.message_handler(Text(startswith=['Отшлепать', 'отшлепать']))
async def pogl(message: types.Message):
    com = message.text[10:]
    if com.find('''
''') == 0:
        com = com[1:]
    try:
        if com == '':
            await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> отшлепал(а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>', parse_mode="HTML")
        else:
            await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> отшлепал(а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\nИ сказал(а): {com}', parse_mode="HTML")
    except:
        pass

@dp.message_handler(Text(startswith=['Обнять', 'обнять']))
async def pogl(message: types.Message):
    com = message.text[7:]
    if com.find('''
''') == 0:
        com = com[1:]
    try:
        if com == '':
            await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> обнял(а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>', parse_mode="HTML")
        else:
            await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> обнял(а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\nИ сказал(а): {com}', parse_mode="HTML")
    except:
        pass

@dp.message_handler(Text(startswith=['Убить', 'убить']))
async def pogl(message: types.Message):
    com = message.text[6:]
    if com.find('''
''') == 0:
        com = com[1:]
    try:
        if com == '':
            await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> убил(а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>', parse_mode="HTML")
        else:
            await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> убил(а) <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\nИ сказал(а): {com}', parse_mode="HTML")
    except:
        pass