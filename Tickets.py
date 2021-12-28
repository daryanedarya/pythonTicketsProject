tickets = int(input("Введите необходимое число билетов: "))
price = []
for i in range(1, tickets+1):
    age = int(input(f"Введите возраст {i} посетителя: "))
    if 0 < age < 18:
        price.append(0)
    else:
        if 18 <= age < 25:
            price.append(990)
        else:
            if 25 <= age < 100:
                price.append(1390)

if tickets > 3: # скидка 10% при покупке более 3 билетов
    print("Сумма к оплате с учетом скидки: ", sum(price) - ((sum(price) / 100) * 10), "рублей")
else:
    print("Сумма к оплате: ", sum(price), "рублей")