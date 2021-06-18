x=3
y=2
for x in range(3,25):
    if x%3==0 and y%2==0:
        print(f'за {x} часа {y} амебы')
        x=x+3
        y=2+y