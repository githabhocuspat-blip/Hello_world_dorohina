a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
d = float(input("Введите d: "))
min = a
if b < min:
    min = b
if c < min:
    min = c
if d < min:
    min = d

print("Минимум:", min)
