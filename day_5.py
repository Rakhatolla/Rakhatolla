# Создать пустой массив. Заполнить 10 числами.
# Найти в этом массиве максимальное число.

# a = []
# a.append(123)
# a.append(5)
# a.append(250)
# a.append(100)
# 
# maximum = 0
# for x in a:
#     if x > maximum:
#         maximum = x
# 
# print(f'Maximum: {maximum}')
# print(max(a))

# Функция - часть кода, которую можно выполнить неоднократно.

def show():
    print('hello')
    print('how are you?')
    
# show()
# show()

# def summa(a = 0, b = 0):
#     res = a + b
#     print(f'Result sum: {res}')
# 
# summa(5, 20)
# summa(3)
# summa()

# def hello2(name='Гость'):
#     print(f'Привет, {name}')
# 
# hello2()
# hello2('Петя')


def repeat(s='', n=2):
    print(s*n)

repeat('мама', 5)