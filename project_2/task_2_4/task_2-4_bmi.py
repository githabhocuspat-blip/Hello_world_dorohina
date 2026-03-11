mass = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (см): "))
height_m = height / 100
bmi = mass / (height_m ** 2)
print("\n--- Отчет о состоянии здоровья ---")
print(f"Рост:\t{height} см")
print(f"Вес:\t{mass} кг")
print(f"Индекс массы тела:\t{bmi:.2f}")