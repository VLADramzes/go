# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

Ticket=int(input("Сколько вам необходимо билетов:"))
print("введите возраст посетителей:")
price=0
for i in range(Ticket):
    age=int(input())
    if age<18:
        price=price+0
    elif 18<=age<25:
        price=price+990
    else:
        price=price+1390
if Ticket>3:
    discount=0.9
else:
    p=1
print("цена:", price*discount)

