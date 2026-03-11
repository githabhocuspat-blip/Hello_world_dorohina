donor = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
patient = input("Введите группу крови пациента (I, II, III, IV): ").strip().upper()
if donor == "I":
    print("Переливание возможно")
elif donor == patient:
    print("Переливание возможно")
elif donor == "II" and patient == "IV":
    print("Переливание возможно")
elif donor == "III" and patient == "IV":
    print("Переливание возможно")
else:
    print("Переливание Нельзя")