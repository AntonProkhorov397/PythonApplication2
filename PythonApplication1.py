#17
Z=int(input("Sisesta arv "))
for i in range(1,10):
    print(Z,"*",i,"=",Z*i)
#15
for j in range(0,10):
    for i in range(0,10):
        print(i,end=" ")
    print()

for j in range(1,10):
    for i in range(1,10):
        print(f"{(j*i):2}",end=" ")
    print()
#16
for j in range(0,10):
    for i in range(0,10):
        if j==i:
            print(i,end=" ")
        else:
            print("0",end=" ")
    print()

import random
a=random.randint(1,10)
while True:
    text=input("Введите число или стоп для выхода: ")
    if text=="стоп":
        print("Выход из программы! До встречи! Загадано было",a)
        break
    elif text==a:
        print("Победа")
        break
    else:
        print("Попробуйте еще")