import logging
from aiogram import Bot, Dispatcher, executor, types
from confiqSQL import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_hallo(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здравствуйте.\nПожалуйста, введите имя пользователя.')

@dp.message_handler(commands=['commands'])
async def process_hallo(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вот список моих команд:\n/start - вернуться к началу\n/commands - показать все команды\n/stop - закончить разговор')

@dp.message_handler(commands=['stop'])
async def process_hallo(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пока!\nРад был пообщаться =)')

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)

if __name__ == '__main__':
    executor. start_polling(dp, skip_updates=True)
