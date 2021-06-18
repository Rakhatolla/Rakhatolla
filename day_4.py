# summa = 0
# for x in range(300, 350):
#     print(x)
#     summa = summa + x
# 
# print(f'Summa {summa}')
# Вывести числа в диапазоне от 50 до 100,
# которые делятся на 3 без остатка
# 
# Пользователь вводит 10 чисел найти их
# сумму и среднее арифметическое

# summa = 0
# k = 5
# for x in range(k):
#     num = int(input(f'Введите {x+1} число'))
#     summa = summa + num
# 
# print(f'Summa {summa}')
# print(f'Srednee {summa/k}')

# список - последовательность из значений.
# индекс - порядковый номер

# names = ['Александр', 'Виктор', 'Мадияр', 'Мансур']

# print(names[3])

# for name in names:
#     print(name)

# names.append('Санат')
# names.remove('Александр')
# print(names)


nums = [1,2,7,10,5,10,50]

summa = 0
for x in nums:
    print(x)
    summa  = summa + x
    
print(f'Summa {summa}')

# print(len(nums))
print(sum(nums))
    
    
    

