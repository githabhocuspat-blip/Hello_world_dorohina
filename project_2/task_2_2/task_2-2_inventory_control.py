name = input()
quantity = int(input())
print(f"Реактив {name} поступил на склад в количестве {quantity} шт.")

file = open("inventory.txt", "w")
file.write(f"Реактив {name} поступил на склад в количестве {quantity} шт.")
file.close()