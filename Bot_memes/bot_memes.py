import random
import json


from aiogram import Bot, Dispatcher, executor, types
from get_memes_for_api import get_memes

token = '6117953281:AAFIaHpk9DhK7s-G1RhnoGmL7Yrpko_fc_4'
bot = Bot(token=token)
disp = Dispatcher(bot)


@disp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Мем")
    keyboard.add(button_1)
    await message.answer(
        "Для того чтобы получить мем нажмите на кнопку!\n",
        reply_markup=keyboard)


@disp.message_handler(lambda message: message.text == "Мем")
async def parser_memes(message: types.Message):
    with open('memes.json', 'r') as file:
        mem = random.choice(json.load(file)['img'])
    await bot.send_photo(message.chat.id, mem)

if __name__ == '__main__':
    get_memes("https://api.memegen.link/images")
    executor.start_polling(disp, skip_updates=True)
