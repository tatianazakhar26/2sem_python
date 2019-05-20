import requests
import telebot
from datetime import datetime, timedelta
from json import loads

with open('t_token.txt') as token_file:
    token = token_file.read()
bot = telebot.TeleBot(token)


user_dict = {}


@bot.message_handler(commands=['start', 'hello'])
def send_hello(message):
    bot.reply_to(message, """\
    Hi there, I am WeatherBot.
I am here to predict weather for you, ask me something!
Firstly you need to choose your city or town with command \set_location.\
    """)


@bot.message_handler(commands=['set_location'])
def send_city(message):
    msg_city = bot.reply_to(message, """\
Write me city or town you would like to know about.\
    """)
    bot.register_next_step_handler(msg_city, register_city)


def register_city(msg_city):
    try:
        city = msg_city.text
        user = msg_city.chat.id
        response = requests.get('https://www.metaweather.com/api/location/search/?query=' + city.lower())
        loc = loads(response.text)
        user_dict[user] = loc[0]["woeid"]
        bot.reply_to(msg_city, """\
You changed location successfully!\
        """)
    except Exception:
        bot.reply_to(msg_city, 'An error occurred.')


@bot.message_handler(commands=['weather'])
def send_weather(message):
    if message.chat.id in user_dict:
        msg_date = bot.reply_to(message, """\
When you want to see weather?
You should send date as '2019/5/10'""")

        def forecast_w(msg):
            forecast(msg, msg.text)

        bot.register_next_step_handler(msg_date, forecast_w)
    else:
        bot.reply_to(message, """\
Firstly you need to choose your city or town with command \set_location.\
        """)


@bot.message_handler(commands=['today'])
def send_today(message):
    if message.chat.id in user_dict:
        td = datetime.today()
        date_td = '{0}/{1}/{2}'.format(td.year, int(td.month), int(td.day))
        forecast(message, date_td)
    else:
        bot.reply_to(message, """\
Firstly you need to choose your city or town with command \set_location.\
        """)


@bot.message_handler(commands=['tomorrow'])
def send_tomorrow(message):
    if message.chat.id in user_dict:
        delta = timedelta(1)
        tm = datetime.today() + delta
        date_tm = '{0}/{1}/{2}'.format(tm.year, int(tm.month), int(tm.day))
        forecast(message, date_tm)
    else:
        bot.reply_to(message, """\
Firstly you need to choose your city or town with command \set_location.\
        """)


def question(city, date):
    response = requests.get('https://www.metaweather.com/api/location/{}/{}/'.format(city, date))
    loc = loads(response.text)
    state = loc[0]["weather_state_name"]
    temp_min = round(float(loc[0]["min_temp"]), 2)
    temp_max = round(float(loc[0]["max_temp"]), 2)
    message = """\
State: {0}
The minimum temperature is {1}
The maximum temperature is {2}\
    """.format(state, temp_min, temp_max)
    return message


def forecast(msg, date):
    try:
        city = user_dict[msg.chat.id]
        message = question(city, date)
        bot.reply_to(msg, message)
    except Exception:
        bot.reply_to(msg, 'An error occurred.')


bot.polling()
