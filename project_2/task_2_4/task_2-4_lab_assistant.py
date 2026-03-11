v = float(input("Введите нужный объем раствора (мл): "))
mass = v * 0.009
v_2 = round(v, 2)
mass_2 = round(mass, 2)
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n")
    file.write(f"Общий объем: {v_2} мл\n")
    file.write(f"Масса соли: {mass_2} г\n")
    file.write(f"Объем воды: {v_2} мл\n")

print("Рецепт сохранен в файл recipe.txt")