per_cent = {'ТКБ':5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Размер вклада: "))
deposit = []

for key in per_cent.keys():
    print('Процентная ставка->', per_cent[key])
    deposit.append(per_cent[key] * money / 100)
maximum = max(deposit)

print("Прибыль в год =", sorted(deposit))
print("Максимальная сумма, которую вы можете заработать =", (maximum))