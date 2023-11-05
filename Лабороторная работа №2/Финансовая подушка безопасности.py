money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0
remaining_money = money_capital + salary - spend
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while remaining_money > 0 :
    spend = spend + spend * increase
    remaining_money = remaining_money + salary - spend
    count += 1

print("Количество месяцев, которое можно протянуть без долгов:", count)
