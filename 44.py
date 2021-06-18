import telebot
import requests
from telebot import types
TOKEN = '1851326077:AAH6B3JS_zCtla9CQNlQSZ2xJi66VBVNE7M'
WEATHERR_TOKEN='eb88425e5f2fd948d36beee71dc1be21'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start','help','films','weather','find','profile','calculator','nice','test'])

def start_bot(message):
    if message.text.lower()=='/start':
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt1=types.KeyboardButton('/start')
        bt2=types.KeyboardButton('/help')
        bt3=types.KeyboardButton('/film')
        bt4=types.KeyboardButton('/weather')
        bt5=types.KeyboardButton('/find')
        bt6=types.KeyboardButton('/profile')
        bt7=types.KeyboardButton('/calculator')
        bt8=types.KeyboardButton('/nice')
        bt9=types.KeyboardButton('/test')
        keyboard.add(bt1)
        keyboard.add(bt2)
        keyboard.add(bt3)
        keyboard.add(bt4)
        keyboard.add(bt5)
        keyboard.add(bt6)
        keyboard.add(bt7)
        keyboard.add(bt8)
        keyboard.add(bt9)
        bot.send_message(message.chat.id,'Hello world<:! \n I am  your new assistant. if you want to start enter\n/start\n/help\n/film\n/weather\n/find\n/profile\n/calculator\n/nice\n',reply_markup=keyboard)
        
    elif message.text.lower()=='/help':
        bot.send_message(message.chat.id,'You in help center')
    elif message.text.lower() == '/films':
        keyboard = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton('Шутеичка',callback_data='joke')
        google = types.InlineKeyboardButton(
            'Го в гугл',
            url='https://google.ru')
        
        keyboard.add(btn)
        keyboard.add(google)
        
        bot.send_message(message.chat.id,
                         'you are finding a film',
                         reply_markup=keyboard)
    elif message.text.lower() == '/test':
        keyboard = types.InlineKeyboardMarkup()
        aaa = types.InlineKeyboardButton('a',callback_data='boke')
        ddd = types.InlineKeyboardButton('d',callback_data='doke')
        bbb = types.InlineKeyboardButton('g',callback_data='doke')
        
        
        
        keyboard.add(aaa)
        keyboard.add(ddd)
        keyboard.add(bbb)
        
        
        bot.send_message(message.chat.id,
                         'What letter does the English alphabet begin with ?',
                         reply_markup=keyboard)
        
    elif message.text.lower()=='/weather':
        bot.send_message(message.chat.id,'You are finding the weather')
        bot.send_message(message.chat.id,'Enter your city')
        bot.register_next_step_handler(message,weather_menu)
        
         
        
    elif message.text.lower()=='/nice':
        bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=Akwm2UZJ34o')
    
    elif message.text.lower()=='/calculator':
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1=types.KeyboardButton('minus-')
        btn2=types.KeyboardButton('plus+')
        btn3=types.KeyboardButton('division/')
        btn4=types.KeyboardButton('multiplication*')
        btn5=types.KeyboardButton('remainder%')
        btn6=types.KeyboardButton('exponentiation**')
        btn7=types.KeyboardButton('whole from division//')
        keyboard.add(btn1)
        keyboard.add(btn2)
        keyboard.add(btn3)
        keyboard.add(btn4)
        keyboard.add(btn5)
        keyboard.add(btn6)
        keyboard.add(btn7)
        bot.send_message(message.chat.id,'Wellcome to calculator! you can use(+,-,/,*,//,**,%) to work in this comand  ',reply_markup=keyboard)
        bot.register_next_step_handler(message,calc_choose)
        
def calc_choose(message):
    if message.text=='plus+':
        bot.send_message(message.chat.id,'You choose plus ')
        bot.send_message(message.chat.id,'Enter a number separated by a space')
        bot.register_next_step_handler(message,calc_result_plus)
    if message.text=='minus-':
        bot.send_message(message.chat.id,'You choose minus ')
        bot.send_message(message.chat.id,'Enter a number separated by a space')
        bot.register_next_step_handler(message,calc_result_minus)
    if message.text=='division/':
        bot.send_message(message.chat.id,'You choose division  ')
        bot.send_message(message.chat.id,'Enter a number separated by a space')
        bot.register_next_step_handler(message,calc_result_division)
    if message.text=='multiplication*':
        bot.send_message(message.chat.id,'You choose multiplication  ')
        bot.send_message(message.chat.id,'Enter a number separated by a space')
        bot.register_next_step_handler(message,calc_result_multiplication)
    if message.text=='remainder%':
        bot.send_message(message.chat.id,'You choose reminder  ')
        bot.send_message(message.chat.id,'Enter a number separated by a space')
        bot.register_next_step_handler(message,calc_result_remainder)
    if message.text=='exponentiation**':
        bot.send_message(message.chat.id,'You choose exponentiation  ')
        bot.send_message(message.chat.id,'Enter a number separated by a space')
        bot.register_next_step_handler(message,calc_result_exponentiation)
    if message.text=='whole from division//':
        bot.send_message(message.chat.id,'You choose whole from division  ')
        bot.send_message(message.chat.id,'Enter a number separated by a space')
        bot.register_next_step_handler(message,calc_result_divisionn)
        
def calc_result_plus(message):
    nums=message.text.split()
    num1=int(nums[0])
    num2=int(nums[1])
    
    bot.send_message(message.chat.id,f"Rusult={num1+num2}={num1}+{num2}")
    

def calc_result_minus(message):
    nums=message.text.split()
    num1=int(nums[0])
    num2=int(nums[1])
    
    bot.send_message(message.chat.id,f"Rusult={num1-num2}={num1}-{num2}")
    
def calc_result_division(message):
    nums=message.text.split()
    num1=int(nums[0])
    num2=int(nums[1])
    
    bot.send_message(message.chat.id,f"Rusult={num1/num2}={num1}/{num2}")   

def calc_result_multiplication(message):
    nums=message.text.split()
    num1=int(nums[0])
    num2=int(nums[1])
    
    bot.send_message(message.chat.id,f"Rusult={num1*num2}={num1}*{num2}")
    
def calc_result_remainder(message):
    nums=message.text.split()
    num1=int(nums[0])
    num2=int(nums[1])
    
    bot.send_message(message.chat.id,f"Rusult={num1%num2}={num1}%{num2}")

def calc_result_exponentiation(message):
    nums=message.text.split()
    num1=int(nums[0])
    num2=int(nums[1])
    
    bot.send_message(message.chat.id,f"Rusult={num1**num2}={num1}**{num2}")
    
def calc_result_divisionn(message):
    nums=message.text.split()
    num1=int(nums[0])
    num2=int(nums[1])
    
    bot.send_message(message.chat.id,f"Rusult={num1//num2}={num1}//{num2}")

  
    if message.text.lower()=='/find':
        bot.send_message(message.chat.id,'You finding for something')
 
    elif message.text.lower()=='/profile':
        bot.send_message(message.chat.id,'You went to your profile ')
        bot.send_message(message.chat.id,'Enter your name: ')
        bot.register_next_step_handler(message,enter_name)

@bot.message_handler(content_type=['text'])
def enter_name(message):
    name=message.text
    bot.send_message(message.chat.id, f"Your name is {name}")
    bot.send_message(message.chat.id, f"enter your age:")
    bot.register_next_step_handler(message,enter_age)
    
@bot.message_handler(content_type=['text'])
def enter_age(message):
    age=message.text
    bot.send_message(message.chat.id, f"Your age is {age} year/years ")
    bot.send_message(message.chat.id, f"enter your phone number:")
    bot.register_next_step_handler(message,enter_phonenumber)

@bot.message_handler(content_type=['text'])
def enter_phonenumber(message):
    phonenumber=message.text
    bot.send_message(message.chat.id, f"Your phone number is {phonenumber}")
    bot.send_message(message.chat.id, f"enter favorite film/s :")
    bot.register_next_step_handler(message,enter_favoritefilm)
    
@bot.message_handler(content_type=['text'])
def enter_favoritefilm(message):
    favoritefilm=message.text
    bot.send_message(message.chat.id, f"Your favorite film/s  is {favoritefilm}")
    bot.send_message(message.chat.id, f"enter your city:")
    bot.register_next_step_handler(message,enter_city)

@bot.message_handler(content_type=['text'])
def enter_city(message):
    city=message.text
    bot.send_message(message.chat.id, f"Your city is {city}")
@bot.callback_query_handler(func=lambda x: x.data == 'joke')
def joke_fn(message):
    bot.send_message(message.from_user.id, "Колобок повесился!")
@bot.callback_query_handler(func=lambda x: x.data == 'boke')
def joke_fn(message):
    bot.send_message(message.from_user.id, "correct")
@bot.callback_query_handler(func=lambda x: x.data == 'doke')
def joke_fn(message):
    bot.send_message(message.from_user.id, "wrong")
    #weather
    
def weather_menu(message):
    city=message.text
    # tolka 1 -vei sait
    API_URL=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=eb88425e5f2fd948d36beee71dc1be21'
    r=requests.get(API_URL)
    w=r.json()
    print(r.text)
    bot.send_message(message.chat.id,f"city:{w['sys']['name']-273.15}")
    bot.send_message(message.chat.id,f"temp:{w['main']['temp']-273.15}")
    bot.send_message(message.chat.id,f"pressure:{w['main']['pressure']-273.15}")
    bot.send_message(message.chat.id,f"humidity:{w['main']['humidity']-273.15}")
    
    
    


bot.polling()   






