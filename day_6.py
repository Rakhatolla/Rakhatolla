import telebot
from telebot import types
import requests


TOKEN = '1812545270:AAFfODIb2VUQvLIiCMYPeTODY9QKNKr19gc'

WEATHER_TOKEN = 'cc2d757656721c7838f819f150c7f7e6'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','weather', 'help', 'profile', 'calc'])
def start_bot(message):
    if message.text.lower() == '/start':
        keyboard = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton('Шутеичка',callback_data='joke')
        google = types.InlineKeyboardButton(
            'Го в гугл',
            url='https://google.ru')
        
        keyboard.add(btn)
        keyboard.add(google)
        
        bot.send_message(message.chat.id,
                         'Всем привет!\n Я новый бот',
                         reply_markup=keyboard)
    
    elif message.text.lower() == '/help':
        bot.send_message(message.chat.id, 'Вы в разделе Помощь')
    
    elif message.text.lower() == '/weather':
        bot.send_message(message.chat.id, 'Вы в разделе Погоды')
        bot.send_message(message.chat.id, 'Введите название города')
        bot.register_next_step_handler(message, weather_menu)
        
    elif message.text.lower() == '/profile':
        bot.send_message(message.chat.id, 'Вы в разделе Профиль')
        bot.send_message(message.chat.id, 'Введите ваше имя: ')
        bot.register_next_step_handler(message, enter_name)

    elif message.text.lower() == '/calc':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Сумма')
        btn2 = types.KeyboardButton('Минус')
        keyboard.add(btn1)
        keyboard.add(btn2)
        
        bot.send_message(message.chat.id,
                         'Калькулятор! Выберите действие',
                         reply_markup=keyboard)
        
        bot.register_next_step_handler(message, calc_choose)
        
# выбор действия калькулятора      
def calc_choose(message):
    if message.text.lower() == 'сумма':
        bot.send_message(message.chat.id, "Вы выбрали сумму.")
        bot.send_message(message.chat.id, "Введите числа через пробел")
        bot.register_next_step_handler(message, calc_result_sum)
    
    if message.text.lower() == 'минус':
        bot.send_message(message.chat.id, "Вы выбрали вычитание.")
        bot.send_message(message.chat.id, "Введите числа через пробел")
        bot.register_next_step_handler(message, calc_result_minus)
      
    
def calc_result_sum(message):
    nums = message.text.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    
    bot.send_message(message.chat.id, f"Результат {num1 + num2}")

def calc_result_minus(message):
    nums = message.text.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    
    bot.send_message(message.chat.id, f"Результат {num1 - num2}")
    

@bot.message_handler(content_type=['text'])
def enter_name(message):
    name = message.text
    bot.send_message(message.chat.id, f"Вас зовут: {name}")
    bot.send_message(message.chat.id, f"А сколько вам лет?")
    
        
@bot.callback_query_handler(func=lambda x: x.data == 'joke')
def joke_fn(message):
    bot.send_message(message.from_user.id, "Колобок повесился!")


# ПОГОДА
def weather_menu(message):
    city = message.text
    API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}'
    r = requests.get(API_URL)
    w = r.json()
    bot.send_message(message.chat.id, f"В городе: {w['name']}")
    bot.send_message(message.chat.id, f"Температура: {w['main']['temp']-273.15}")
    
    
    

bot.polling()    
    