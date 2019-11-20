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
import os
import pickle
import requests
from lxml import html
from datetime import datetime


def exchange_rate(func):
    def wrapper(self, usd_rate, euro_rate):
        total_amount = self.balance
        print(f'Текущий баланс счета в $США: {(total_amount/usd_rate):.2f}')
        print(f'Текущий баланс счета в EURO: {(total_amount/euro_rate):.2f}')
        return func(self)
    return wrapper


class Account:
    def __init__(self, balance, history, plus, minus, usd, euro):
        self.balance = balance
        self.history = history
        self.plus = plus
        self.minus = minus
        self.usd = usd
        self.euro = euro

    def deposit(self, amount):
        cdt = datetime.today().strftime('%d/%m/%Y %H.%M.%S')
        self.plus += 1
        transaction = '+'
        self.balance += amount
        self.history.append([cdt, transaction, [amount]])

    @exchange_rate
    def get_balance(self):
        return self.balance

    def buy(self, amount, name):
        cdt = datetime.today().strftime('%d/%m/%Y %H.%M.%S')
        self.minus += 1
        transaction = '-'
        self.balance = self.balance - amount
        self.history.append([cdt, transaction, [name, amount]])

    def get_history(self, transaction='all'):
        print('<<< История счета! >>>' if self.history else '<<< Нет записей в истории счета! >>>')
        if transaction == '+':
            if self.plus != 0:
                print('Пополнения счета:')
                print(f'   ---> Всего операций пополнения: {self.plus}')
                print(*(f'{i[0]} ---> {i[1]} {" ".join(str(x) for x in i[2])}'
                        for i in self.history if i[1] == transaction), sep='\n')
            else:
                print('История пополнения счета:')
                print(f'   ---> Всего операций пополнения: {self.plus}')
                print('Вы еще не сделали ни одного пополнения!')
        elif transaction == '-':
            if self.minus != 0:
                print('История покупок:')
                print(f'   ---> Всего операций списания: {self.minus}')
                print(*(f'{i[0]} ---> {i[1]} {" ".join(str(x) for x in i[2])}'
                        for i in self.history if i[1] == transaction), sep='\n')
            else:
                print('История покупок:')
                print(f'   ---> Всего операций списания: {self.minus}')
                print('Вы пока не сделали ни одной покупки!')
        else:
            print('Вся история действий со счетом:')
            print(f'   ---> Всего операций по счету: {self.plus + self.minus}')
            print(*(f'{i[0]} ---> {i[1]} {" ".join(str(x) for x in i[2])}' for i in self.history), sep='\n')

    def clear_balance(self):
        self.balance = 0

    def clear_history(self):
        self.history = []
        self.plus = 0
        self.minus = 0


def read_data(filename1, filename2):
    balance = 0
    history = []
    plus = 0
    minus = 0
    if os.path.exists(filename1):
        with open(filename1, 'rb') as f:
            balance = pickle.load(f)
        f.close()
    if os.path.exists(filename2):
        with open(filename2, 'rb') as f:
            history = pickle.load(f)
            f.close()
            for item in history:
                if item[1] == '+':
                    plus += 1
                elif item[1] == '-':
                    minus += 1
    return balance, history, plus, minus


def write_data(balance, history, filename1, filename2):
    with open(filename1, 'wb') as f:
        pickle.dump(balance, f)
        f.close()
    with open(filename2, 'wb') as f:
        pickle.dump(history, f)
        f.close()


def separator(symbol, count):
    return symbol * count


def get_exchange_rate(cdt):
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/78.0.3904.97 Safari/537.36'}
    main_link = 'http://www.cbr.ru/currency_base/daily/?date_req='
    try:
        r = requests.get(f'{main_link}{cdt}', headers=header)
        root = html.fromstring(r.text)
        u_rate = float(root.xpath('//tr[12]/td[5]/text()')[0].replace(',', '.'))
        e_rate = float(root.xpath('//tr[13]/td[5]/text()')[0].replace(',', '.'))
    except requests.exceptions.RequestException as e:
        print(f'Ошибка получения курса валют - {e}')
        u_rate = 1
        e_rate = 1
    return u_rate, e_rate


def my_bank_account():
    account_balance_filename = 'account_balance.pkl'
    account_history_filename = 'account_history.pkl'
    total_amount, history, plus, minus = read_data(account_balance_filename, account_history_filename)
    cdt = datetime.today().strftime('%d.%m.%Y')
    usd_rate, euro_rate = get_exchange_rate(cdt)
    my_account = Account(total_amount, history, plus, minus, usd_rate, euro_rate)
    sep_count = 55

    while True:
        print('1. Пополнение счета')
        print('2. Покупка')
        print('3. Посмотреть полную историю по счету')
        print('4. Посмотреть историю пополнений')
        print('5. Посмотреть историю покупок')
        print('6. Показать баланс счета')
        print('7. Очистить историю и обнулить баланс')
        print('0. Выход')
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            try:
                deposit_amount = abs(float(input('Введите сумму пополнения счета: ')))
            except ValueError:
                print('Неверно введена сумма пополнения. Сумма должна быть в формате XXXX.XX (например: 1999.99)')
                deposit_amount = 0
            my_account.deposit(deposit_amount)
            total_amount = my_account.get_balance(usd_rate, euro_rate)
            print(f'Текущий баланс счета в РУБ.: {total_amount:.2f}')
            print('Вы пополнили счет!')
            print(separator('-', sep_count))
        elif choice == '2':
            try:
                purchase_amount = abs(float(input('Введите сумму покупки: ')))
                if purchase_amount > total_amount:
                    print(f'Текущий баланс счета в РУБ.: {total_amount:.2f}')
                    print('У вас не достаточно средств на счете. Покупка не возможна!')
                    print(separator('-', sep_count))
                else:
                    purchase_name = input('Введите название покупки: ')
                    my_account.buy(purchase_amount, purchase_name)
                    print(f'Вы произвели покупку "{purchase_name}" на сумму {purchase_amount}')
                    total_amount = my_account.get_balance(usd_rate, euro_rate)
                    print(f'Текущий баланс счета в РУБ.: {total_amount:.2f}')
                    print(separator('-', sep_count))
            except ValueError:
                print('Неверно введена сумма покупки. Сумма должна быть в формате XXXX.XX (например: 1999.99)')
                purchase_amount = 0
                purchase_name = 'Неудачная покупка'
                my_account.buy(purchase_amount, purchase_name)
                print(f'Вы произвели покупку "{purchase_name}" на сумму {purchase_amount}')
                total_amount = my_account.get_balance(usd_rate, euro_rate)
                print(f'Текущий баланс счета в РУБ.: {total_amount:.2f}')
                print(separator('-', sep_count))
        elif choice == '3':
            my_account.get_history()
            print(separator('-', sep_count))
        elif choice == '4':
            my_account.get_history('+')
            print(separator('-', sep_count))
        elif choice == '5':
            my_account.get_history('-')
            print(separator('-', sep_count))
        elif choice == '6':
            total_amount = my_account.get_balance(usd_rate, euro_rate)
            print(f'Текущий баланс счета в РУБ.: {total_amount:.2f}')
            print(separator('-', sep_count))
        elif choice == '7':
            my_account.clear_balance()
            my_account.clear_history()
            total_amount = my_account.get_balance(usd_rate, euro_rate)
            history = []
            write_data(total_amount, history, account_balance_filename, account_history_filename)
            print(f'Текущий баланс счета: {total_amount:.2f}')
            print('БАЛАНС ОБНУЛЕН!')
            print('ИСТОРИЯ ОЧИЩЕНА!')
            print(separator('-', sep_count))
        elif choice == '0':
            write_data(total_amount, history, account_balance_filename, account_history_filename)
            print('Выполение программы закончено. До свидания!')
            print(separator('-', sep_count))
            break
        else:
            print('Неверный пункт меню')
            print(separator('-', sep_count))
