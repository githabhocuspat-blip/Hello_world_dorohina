capsul = int(input("Введите общее количество произведенных капсул: "))
size = int(input("Введите количество капсул в одной упаковке: "))
pack = capsul // size
remaining = capsul % size
print("\n--- Отчет фасовочного цеха ---")
print(f"Полных упаковок: {pack}")
print(f"Остаток капсул: {remaining}")