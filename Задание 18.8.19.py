ticket = int(input("Ввести количество билетов "))
price = 0
for value in range(ticket):
    age = int(input("Ввести возраст "))
    if  18 <= age <= 25:
        price = price + 990
        print("Cумма покупки", price, "p")
    elif age > 25:
        price = price + 1390
        print("Cумма покупки", price, "p")
    elif age < 18:
        price = price + 0
        print("Cумма покупки", price, "p")
if ticket > 3:
        price = price - (price / 10)
        print (" Итоговая цена билетов со скидкой", int(price), "р")