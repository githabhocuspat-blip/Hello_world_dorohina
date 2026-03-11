name = input("Введите название питательной среды: ")
agar = input("Введите концентрацию агара (%): ")
temp = input("Введите температуру стерилизации (°C): ")

with open("recipe.txt", "w") as file:
    file.write(name + "\n")
    file.write("- Концентрация агара: " + agar + "%\n")
    file.write("- Температура стерилизации: " + temp + "°C\n")

print("Файл 'recipe.txt' успешно сформирован!")