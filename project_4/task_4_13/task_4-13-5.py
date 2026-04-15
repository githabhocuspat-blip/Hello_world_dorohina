n = int(input("Сколько чисел? "))
max = float(input("Введите 1-е число: "))

for i in range(n - 1):
    n = float(input("Введите следующее число: "))
    if n > max:
        max = n

print("Максимум:", max)
