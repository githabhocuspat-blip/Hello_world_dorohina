seq = ["ATATACGCGTA", "CTTCGGNGGA"]
for sequence in seq:
    print(f"\nПоследовательность целиком: {sequence}")
    print("Построчно:")
    
    for letter in sequence:
        print(letter)
print("\nЦикл выполнен")