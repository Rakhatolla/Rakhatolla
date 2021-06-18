m=int(input(" enter m "))
n=int(input(" enter n "))
a=n+1
summa=0
for n in range(m,a):
    if m<=n:
        m=m+1
        summa=summa+m**m
        print=(summa)