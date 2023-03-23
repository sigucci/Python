from email import message_from_binary_file, message_from_bytes
from pyexpat.errors import messages
import pythonconfig
import logging

from aiogram import Bot, Dispatcher, executor, types
from pythontest import SQLighter

#Задаем уровень логов
logging.basicConfig(level=logging.INFO)

#Инициализация бота
bot = Bot(token=pythonconfig.API_TOKEN)
dp = Dispatcher(bot)

#Инициализация соединения с БД
db = SQLighter('db.db')

#Команда активации подписки
@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if(not db.subscriber_exists(message.from_user.id)):
        #Если юзера нет в базе, добавляем его
        db.add_subscriber(message.from_user.id)
    else:
        #Если пользователь есть, обновляем статус подписки
        db.update_subscriptions(message.from_user.id, True)

    await message.answer("Вы успешно подписались на рассылку!")
    
#Команда отписки
@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if(not db.subscriber_exists(message.from_user.id)):
        db.add_subscriber(message.from_user.id, False)
        await message.answer("Вы итак не подписаны.")
    else:
        db.update_subscriptions(message.from_user.id, False)
        await message.answer("Вы успешно отписались от рассылки.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)