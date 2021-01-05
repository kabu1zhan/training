import telebot
from telebot import types
import yaml
from pprint import pprint
token = '1181992733:AAH79PQaMpHMJfazGSL4SZNLGSzdCWPc5Y4'
url = 'https://api.telegram.org/bot1181992733:AAH79PQaMpHMJfazGSL4SZNLGSzdCWPc5Y4/getUpdates'
bot = telebot.TeleBot(token)
mylist = []
USERS = {}

#Действия при команде старт
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    key_start = types.KeyboardButton("/start")
    key_add = types.KeyboardButton("/add")
    key_list = types.KeyboardButton("/list")
    key_reset = types.KeyboardButton("/reset")
    markup.add(key_start, key_add, key_list, key_reset)

    bot.send_message(message.chat.id, 'Привет я бот заметка, вы можете отправить мне вашу заметку или посмотреть список сохраненых мест\n'
                                      'C помощью /add вы можете ввести адресс\n'
                                      'C помощью /list вы можете вывести сохраненные места\n'
                                      'C помощью /reset вы можете удалить данные', parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['add'])
def perehod(message):
    bot.send_message(message.chat.id, 'Введите адрес')
    bot.register_next_step_handler(message, zapis)

def zapis(message):
    global id
    id = message.from_user.id
    mylist.append(message.text)
    to_yaml = {id:mylist}
    for i in to_yaml:
        if id == i:
            with open('adresa.yml', 'a') as f:
                yaml.dump(to_yaml, f)
                print(to_yaml)
        else:
            continue

@bot.message_handler(commands=['list'])
def vivod(message):
    with open('adresa.yml') as f:
        templates = yaml.safe_load_all(f)
        for i in templates:
            for k, v in i.items():
                if k == message.from_user.id:
                    bot.send_message(message.chat.id, 'Адреса {0}'.format(', '.join(v)))
                    print(v)

#Запуск бота
bot.polling(none_stop=True)