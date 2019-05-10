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
    when = response.text
    print(when)
    state_loc = len('"weather_state_name":"') + when.find('"weather_state_name":"')
    temp_min_loc = len('"min_temp":')+when.find('"min_temp":')
    temp_max_loc = len('"max_temp":')+when.find('"max_temp":')
    state = when[state_loc:when.find('"', state_loc+2)]
    temp_min = when[temp_min_loc:when.find('"', temp_min_loc+2) - 1]
    temp_max = when[temp_max_loc:when.find('"', temp_max_loc+2) - 1]
    # print(state)
    return state, temp_min, temp_max


def weather(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.when = message.text
        weather_ = question(user)
        bot.reply_to(message, 'State: {}'.format(weather_[0]))
        bot.reply_to(message, 'The mininmum temperature is {}'.format(weather_[1]))
        bot.reply_to(message, 'The maximum temperature is {}'.format(weather_[2]))
    except Exception:
        bot.reply_to(message, 'oooops')


bot.polling(none_stop=True, interval=1)

