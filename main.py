# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
money = float(input("введите сумму депозита:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
banks = list(per_cent.keys())
percents = list(per_cent.values())
deposit = list()
deposit.append(int(money/100*float(percents[0])))
deposit.append(int(money/100*float(percents[1])))
deposit.append(int(money/100*float(percents[2])))
deposit.append(int(money/100*float(percents[3])))
print(f'\nДоход по депозиту составит:\n{banks[0]} банк - {deposit[0]} рублей\n{banks[1]} банк - {deposit[1]} ' f'рублей\n{banks[2]} банк - {deposit[2]} рублей\n{banks[3]} банк - {deposit[3]} рублей\n')
max_deposit = max(deposit)
print('Максимальная сумма, которую вы можете заработать: {} рублей.'.format(max_deposit))