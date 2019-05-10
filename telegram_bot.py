import requests
import telebot

with open('t_token.txt') as token_file:
    token = token_file.read()
bot = telebot.TeleBot(token)
user_dict = {}


class Weather:
    def __init__(self):
        self.when = None
        self.where = None


@bot.message_handler(commands=['start', 'hello'])
def send_hello(message):
    bot.reply_to(message, """\
    Hi there, I am WeatherBot.
    I am here to predict weather for you, ask me something!\
    """)


@bot.message_handler(commands=['weather'])
def send_where(message):
    msg = bot.reply_to(message, """\
    Where you want to see weather?
    You can send city or town""")
    bot.register_next_step_handler(msg, send_when)


def send_when(message):
    try:
        chat_id = message.chat.id
        user = Weather()
        user.where = message.text
        user_dict[chat_id] = user
        msg = bot.reply_to(message, """\
        When you want to see weather?
        You should send date as '2019/5/10'""")
        bot.register_next_step_handler(msg, weather)
    except Exception:
        bot.reply_to(message, 'oooops')


def question(user):
    response = requests.get('https://www.metaweather.com/api/location/search/?query='+user.where)
    where = response.text
    woeid = where.find('"woeid":')
    where = where[woeid+8:where.find(',', woeid+1)]
    response = requests.get('https://www.metaweather.com/api/location/{}/{}/'.format(where, user.when))
    when = response.text.split(sep=',')
    return when


def weather(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.when = message.text
        answer = question(user)
        bot.reply_to(message, answer)
    except Exception:
        bot.reply_to(message, 'oooops')


bot.polling(none_stop=True, interval=1)

