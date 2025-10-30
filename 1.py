a = int(input("введите первое число: "))
b = int(input("введите второе число: "))
for i in range(a,b):
    if i % 7 == 0:
        print(i, end=" ")