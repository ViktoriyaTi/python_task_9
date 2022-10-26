# pip install python-telegram-bot==13.14
# Updater → Dispatсher → Handlers → start → wait_for_the_end
# Updater - взаимодействие между клиентом и сервером
# Dispatсher - отвечает за вызов обработчика сообщений
# Handlers - обработчики сообщений

from telegram import Bot
from telegram.ext import (CommandHandler, ConversationHandler, MessageHandler,
                          Updater, Filters)

from db import init_database, show_all as sa, add_person, find_person, del_person, update_info

bot_token = "5771868767:AAE15LHUORFPe3osnpewdftp9uUhmCW1PYY"
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(
        update.effective_chat.id,f"Здравствуйте!\nЭто список сотрудников организации.\nПоказать весь справочник?/show_all \nДобавить нового сотрудника?/new_add \nНайти сотрудника по фамилии?/find_info \nУдалить сотрудника из справочника?/del_info \nОбновить сведения о фамилии сотрудника?/update_surname \nЗавершить работу со справочником?/stop")


start_handler = CommandHandler('start', start)


def show_all(update, context):
     sa(init_database('employeers.db'))
     update.message.reply_text("Выполнено успешно!")
     return ConversationHandler.END

     
show_all_handler = CommandHandler('show_all', show_all)


def new_add(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "Введите фамилию, имя, табельный номер, должность нового сотрудника через пробел: ")
    return 1


def add(update, context):
    new_surname, new_name, new_personal_number, new_job_title = update.message.text.split()
    print(new_surname, new_name, new_personal_number, new_job_title)
    add_person('employeers.db', new_surname, new_name, new_personal_number, new_job_title)
    update.message.reply_text("Добавлена новая информация - успешно!")
    return ConversationHandler.END


def find_info(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "Введите фамилию сотрудника для поиска в базе данных: ")
    return 1


def find(update, context):
    find_surname = update.message.text
    print(find_surname)
    if find_person('employeers.db',find_surname)!= []:
        update.message.reply_text("Операция по поиску сотрудника прошла успешно!")  
    else:
        update.message.reply_text(f"Сотрудник {find_surname} отсутствует в базе данных.")   
    return ConversationHandler.END


def del_info(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "Введите фамилию сотрудника для её удаления из базы данных: ")
    return 1


def delete(update, context):
    del_surname = update.message.text
    print(del_surname)
    if find_person('employeers.db', del_surname) != []:
        del_person('employeers.db', del_surname)
        update.message.reply_text(f"Операция по удалению записи о сотруднике {del_surname} прошла успешно!")
    else: 
        update.message.reply_text(f"Сотрудник {del_surname} отсутствует в базе данных.")   
    return ConversationHandler.END

def update_surname(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "Введите старую фамилию сотрудника, затем новую фамилию через пробел: ")
    return 1

def update_surname_info(update, context):
    old_info, new_info = update.message.text.split()
    if find_person('employeers.db', old_info) != []:
        update_info('employeers.db', old_info, new_info)
        update.message.reply_text(f"Операция по обновлению записи сотрудника по фамилии {old_info} прошла успешно! Фамилия изменена на {new_info}.")
    else: 
        update.message.reply_text(f"Сотрудник {old_info} отсутствует в базе данных.")
    return ConversationHandler.END


def stop(update, context):
    update.message.reply_text(f"Всего доброго!")
    return ConversationHandler.END


stop_handler = CommandHandler('stop', stop)


add_handler = ConversationHandler(
    entry_points=[CommandHandler('new_add', new_add)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, add)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)


find_handler = ConversationHandler(
    entry_points=[CommandHandler('find_info', find_info)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, find)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)


delete_person_handler = ConversationHandler(
    entry_points=[CommandHandler('del_info', del_info)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, delete)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)


update_surname_info_handler = ConversationHandler(
    entry_points=[CommandHandler('update_surname', update_surname)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, update_surname_info)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(show_all_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(find_handler)
dispatcher.add_handler(delete_person_handler)
dispatcher.add_handler(update_surname_info_handler)
dispatcher.add_handler(stop_handler)
updater.start_polling()
updater.idle()
