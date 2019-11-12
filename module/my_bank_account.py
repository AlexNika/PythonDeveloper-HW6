# create Branch HW5
"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""


class Account:
    plus = 0
    minus = 0

    def __init__(self, balance, history):
        self.balance = balance
        self.history = history

    def deposit(self, amount):
        self.plus += 1
        transaction = '+'
        self.balance += amount
        self.history.append([transaction, [amount]])

    def get_balance(self):
        return self.balance

    def buy(self, amount, name):
        self.minus += 1
        transaction = '-'
        self.balance = self.balance - amount
        self.history.append([transaction, [name, amount]])

    def get_history(self, transaction='all'):
        if len(self.history) == 0:
            print('Нет записей в истории счета!')
        if transaction == '+':
            if self.plus != 0:
                print('История пополнения счета:')
                print(f'   ---> Всего операций пополнения: {self.plus}')
                for item in self.history:
                    if item[0] == transaction:
                        print(item[0], ':', *item[1])
            else:
                print('История пополнения счета:')
                print(f'   ---> Всего операций пополнения: {self.plus}')
                print('Вы еще не сделали ни одного пополнения!')
        elif transaction == '-':
            if self.minus != 0:
                print('История покупок:')
                print(f'   ---> Всего операций списания: {self.minus}')
                for item in self.history:
                    if item[0] == transaction:
                        print(item[0], ':', *item[1])
            else:
                print('История покупок:')
                print(f'   ---> Всего операций списания: {self.minus}')
                print('Вы пока не сделали ни одной покупки!')
        else:
            print('Вся история действий со счетом:')
            print(f'   ---> Всего операций по счету: {self.plus+self.minus}')
            for item in self.history:
                print(item[0], ':', *item[1])


def separator(symbol, count):
    return symbol * count


def my_bank_account():
    my_account = Account(0, [])
    sep_count = 55

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история пополнений')
        print('4. история покупок')
        print('5. посмотреть баланс счета')
        print('6. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            deposit_amount = int(input('Введите сумму пополнения счета: '))
            my_account.deposit(deposit_amount)
            print(f'Вы пополнили счет. Текущий баланс счета: {my_account.get_balance()}')
            print(separator('-', sep_count))
        elif choice == '2':
            purchase_amount = int(input('Введите сумму покупки: '))
            if purchase_amount > my_account.get_balance():
                print('У вас не достаточно средств на счете. Покупка не возможна!')
                print(f'Текущий баланс счета: {my_account.get_balance()}')
                print(separator('-', sep_count))
            else:
                purchase_name = input('Введите название покупки: ')
                my_account.buy(purchase_amount, purchase_name)
                print(f'Вы произвели покупку "{purchase_name}". Текущий баланс счета: {my_account.get_balance()}')
                print(separator('-', sep_count))
        elif choice == '3':
            my_account.get_history('+')
            print(separator('-', sep_count))
        elif choice == '4':
            my_account.get_history('-')
            print(separator('-', sep_count))
        elif choice == '5':
            print(f'Текущий баланс счета: {my_account.get_balance()}')
        elif choice == '6':
            print('Выполение программы закончено. До свидания!')
            print(separator('-', sep_count))
            break
        else:
            print('Неверный пункт меню')
            print(separator('-', sep_count))