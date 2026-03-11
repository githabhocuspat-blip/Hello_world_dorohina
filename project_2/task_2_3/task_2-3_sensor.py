operator = input("Введите имя оператора: ")
pres = input("Введите текущее значение датчика давления: ")
with open("sensor_log.txt", "w") as file:
    file.write(operator + "\t" + pres)
print("Данные успешно сохранены в sensor_log.txt")