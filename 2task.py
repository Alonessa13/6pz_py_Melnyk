stock = 20
quantity = int(input("Введіть кількість товару: "))
if quantity <= 0:
    print("Помилка: некоректна кількість!")
    exit()
if quantity > stock:
    print("На складі недостатньо товару!")
    exit()
print("Ваше замовлення прийнято!")
