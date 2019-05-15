import requests
import telebot
from json import loads

with open('t_token.txt') as token_file:
    token = token_file.read()
bot = telebot.TeleBot(token)


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
def send_city(message):
    msg_city = bot.reply_to(message, """\
    Where you want to see weather?
You can send city or town""")
    bot.register_next_step_handler(msg_city, send_date)


def send_date(msg_city):
    msg_date = bot.reply_to(msg_city, """\
    When you want to see weather?
You should send date as '2019/5/10'""")

    def forecast_(msg_date):
        forecast(msg_city, msg_date)
    bot.register_next_step_handler(msg_date, forecast_)


def question(city, date):
    response = requests.get('https://www.metaweather.com/api/location/search/?query=' + city)
    where = loads(response.text)
    response = requests.get('https://www.metaweather.com/api/location/{}/{}/'.format(where[0]["woeid"], date))
    loc = loads(response.text)
    state = loc[0]["weather_state_name"]
    temp_min = loc[0]["min_temp"]
    temp_max = loc[0]["max_temp"]
    return state, temp_min, temp_max


def forecast(msg_city, msg_date):
    try:
        weather_ = question(msg_city.text, msg_date.text)
        bot.reply_to(msg_date, 'State: {}'.format(weather_[0]))
        bot.reply_to(msg_date, 'The mininmum temperature is {}'.format(weather_[1]))
        bot.reply_to(msg_date, 'The maximum temperature is {}'.format(weather_[2]))
    except Exception:
        bot.reply_to(msg_date, 'oooops')

bot.polling()
