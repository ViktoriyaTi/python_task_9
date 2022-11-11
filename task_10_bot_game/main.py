from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler,ConversationHandler,MessageHandler,Filters
from random import randint
reply_keyboard = [['/play','/information','/exit']]
stop_keyboard = [['/stop']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
stop_markup = ReplyKeyboardMarkup(stop_keyboard, one_time_keyboard=False)

TOKEN = '5731398378:AAEaDxn-_DIYoh1Yuya7zgYOOEfDWe62Iwc'

candies = 0
player_candies = 0
max_candies = 28


def start(update, context):
    update.message.reply_text(
        "Давайте поиграем в игру? Игра в конфеты. Если знаешь правила смело нажимай кнопку play, в противном случае ознакомься с правилами - кнопка information.",
        reply_markup=markup
    )


def play(update, context):
    global candies
    update.message.reply_text(
    "Введите количество конфет, которое будет на кону (пример: 2021).\nМаксимальное количество конфет, которое можно взять за один раз - 28 шт", reply_markup=stop_markup)
    return 1


def get_candy(update, context): 
    global candies
    try:
        candies= int(update.message.text)
        update.message.reply_text(f"Ваш ход! На столе осталось {candies} конфет. Сколько конфет вы возьмете от 1 до 28 включительно?")
        return 2
    except ValueError:
        update.message.reply_text("Введите число больше 28") 
        return 1


def input_value(update, context):
    global player_candies, max_candies
    player_candies = int(update.message.text)
    if player_candies <= 0 or player_candies >= max_candies + 1:
        return 0
    else:
        return 1


def player_turn(update, context):
    global candies, player_candies, max_candies
    try:
        if input_value(update, context) == 1:
            candies -= player_candies
            bot_move = randint(1,max_candies)
            update.message.reply_text(f"На столе осталось {candies} конфет.")
            if candies > max_candies:
                update.message.reply_text(f"Бот взял {bot_move} конфет")
                candies -= bot_move
                if  candies > max_candies:
                    update.message.reply_text(f"Ваш ход! На столе {candies} конфет. Сколько конфет вы возьмете?")
                else:  
                    update.message.reply_text("Поздравляем вы победили!", reply_markup=markup)
                    context.bot.send_photo(update.effective_chat.id, photo=open('1.png', 'rb'))
                    return ConversationHandler.END
                return 2
            else:        
                update.message.reply_text("Увы, выиграл Бот!\nПопробуйте еще раз", reply_markup=markup)
                context.bot.send_photo(update.effective_chat.id, photo=open('2.jpg', 'rb'))
                return ConversationHandler.END
        else:
            input_value(update, context)
            update.message.reply_text("ОШИБКА!Введите корректное количество конфет в диапозоне от 1 до 28 включительно!")        
    except ValueError:
            update.message.reply_text("Введите число") 
            return 2


def exit(update, context):
    update.message.reply_text(
        "Всего хорошего! До встречи!",
        reply_markup=ReplyKeyboardRemove()
    )


def information(update, context):
    update.message.reply_text(
        "Правила игры\nНа столе лежит 2021 конфета.\nИграют два игрока (бот и человек) делая ход друг после друга.\nПервым будет ваш ход.\nЗа один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.\n(Приведен пример с количеством конфет,пользователь сам вносит значения количества конфет, которое находится кону)", reply_markup=markup
    )


def stop(update, context):
    update.message.reply_text(f"Всего доброго!",stop_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


stop_handler = CommandHandler('stop', stop)


play_handler = ConversationHandler(
    entry_points=[CommandHandler('play', play)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, get_candy)],
        2: [MessageHandler(Filters.text & ~Filters.command, player_turn)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("information", information))
    dp.add_handler(play_handler)
    dp.add_handler(CommandHandler("exit", exit))
    dp.add_handler(stop_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
