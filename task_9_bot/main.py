
from telegram import Bot, Update
from telegram.ext import (CommandHandler, ConversationHandler, MessageHandler,
                          Updater, Filters)
from db import init_database, show_all as sa, add_person 

bot_token = "5771868767:AAE15LHUORFPe3osnpewdftp9uUhmCW1PYY"
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

# pip install python-telegram-bot==13.14
# Updater → Dispatсher → Handlers → start → wait_for_the_end
# Updater - взаимодействие между клиентом и сервером
# Dispatсher - отвечает за вызов обработчика сообщений
# Handlers - обработчики сообщений


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             f"Привет! Это список сотрудников.\nПокажем весь справочник?/show_all\nДобавим нового сотрудника?/new_add\n")


start_handler = CommandHandler('start', start)


def show_all(update, context):
     sa(init_database('employeers.db'))
     update.message.reply_text("Выполнено успешно!")
     return ConversationHandler.END

show_all_handler = CommandHandler('show_all', show_all)

def new_add(update, context):
    new_surname, new_name, new_job_title = context.bot.send_message(update.effective_chat.id, "Введите фамилию, имя, должность нового сотрудника через пробел: ")
    add_person ('employeers.db', new_surname, new_name, new_job_title)
    update.message.reply_text("Добавлена новая информация - успешно!")


new_add_handler = CommandHandler('new_add', new_add)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(show_all_handler)
dispatcher.add_handler(new_add_handler)
updater.start_polling()
updater.idle()
