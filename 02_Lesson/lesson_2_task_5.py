def month_to_season(month):
    if 3 <= month <= 5:
        return "Весна"
    elif 6 <= month <= 8:
        return "Лето"
    elif 9 <= month <= 11:
        return "Осень"
    elif 1 <= month <= 12:
        return "Зима"
    else:
        return "Ошибка"
    
month = int(input("Введите номер месяца (1-12): "))
print(month_to_season(month)) 