tickets_num = int(input("Введите количество билетов:"))
total_price = 0

for ticket in range (tickets_num):
    age = int(input(f"Введите возраст постетителя {ticket + 1}:"))
    if age < 18:
        continue
    elif 18 <= age < 25:
        total_price += 990
    elif 25 <= age < 99:
        total_price += 1390
    else:
        print("Неверный возраст. Начните заново.")
        break
if tickets_num > 3:
    total_price *= .9
print("Общая стоимость билетов:", total_price)