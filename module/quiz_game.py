# create Branch HW5
# -*- coding: utf-8 -*-
import random
"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
"""
        Год рождения Жана Антуана Ватто - 10.10.1684
        Год рождения Джузеппе Верди - 10.10.1813
        Год рождения Алексея Константиновича Толстого - 05.09.1817
        Год рождения Фритьоф Нансена - 10.10.1861
        Год рождения Владимира Обручева - 28.09.1863
        Год рождения Шарлотты Купер - 22.09.1870
        Год рождения Людвига Мизеса - 29.09.1881
        Год рождения Альберто Джакометти - 10.10.1901
        Год рождения Ванды Якубовской - 10.10.1907
        Год рождения Бруно Фрейндлиха - 10.10.1909
"""
# За основу взято задание из 3-го ДЗ - victory.py
# код переписан с импользованием 2-х функций


day_name = {'01': 'Первое',
            '02': 'Второе',
            '03': 'Третье',
            '04': 'Четвертое',
            '05': 'Пятое',
            '06': 'Шестое',
            '07': 'Седьмое',
            '08': 'Восьмое',
            '09': 'Девятое',
            '10': 'Десятое',
            '11': 'Одиннадцатое',
            '12': 'Двенадцатое',
            '13': 'Тринадцатое',
            '14': 'Четырнадцатое',
            '15': 'Пятнадцатое',
            '16': 'Шестнадцатое',
            '17': 'Семнадцатое',
            '18': 'Восемнадцатое',
            '19': 'Девятнадцатое',
            '20': 'Двадцатое',
            '21': 'Двадцать первое',
            '22': 'Двадцать второе',
            '23': 'Двадцать третье',
            '24': 'Двадцать четвертое',
            '25': 'Двадцать пятое',
            '26': 'Двадцать шестое',
            '27': 'Двадцать седьмое',
            '28': 'Двадцать восьмое',
            '29': 'Двадцать девятое',
            '30': 'Тридцатое',
            '31': 'Тридцать первое'}
month_name = {'01': 'января',
              '02': 'февраля',
              '03': 'марта',
              '04': 'апреля',
              '05': 'мая',
              '06': 'июня',
              '07': 'июля',
              '08': 'августа',
              '09': 'сентября',
              '10': 'октября',
              '11': 'ноября',
              '12': 'декабря'}
question = 'Введите дату рождения '


def check_answer(celebrities_, person_, output_=True):
    answer_ = input(question + person_ + ' в формате dd.mm.yyyy: ')
    correct_ = False
    if answer_ == celebrities_.get(person_):
        correct_ = True
        if output_:
            print('Верно!')
    else:
        b_day = celebrities_.get(person_).split('.')
        b_in_text = day_name[b_day[0]] + ' ' + month_name[b_day[1]] + ' ' + b_day[2] + ' года'
        if output_:
            print(f'Не верно! Правильная дата рождения {person_} = {b_in_text}')
    return correct_


def statistic_output(correct, incorrect):
    q_ty = correct + incorrect
    print()
    print(f'Количество правильных ответов: {correct}')
    print(f'Количество неправильных ответов: {incorrect}')
    print(f'Процент правильных ответов: {correct * 100 / q_ty}')
    print(f'Процент неправильных ответов: {round(100 * (1 - correct / q_ty), 1)}\n')


def quiz_game():
    print('Викторина - угадай год рождения знаменитых людей')
    print('------------------------------------------------')
    print('Правила:')
    print('Вам будет предложено ответить на 10 вопросов.')
    print('Чем больше правильных ответов, тем лучше :)))')
    print('В конце викторины, вы можете запустить ее вновь.')
    print('Удачи!!!\n')
    celebrities = {'Жана Антуана Ватто': '10.10.1684',
                   'Джузеппе Верди': '10.10.1813',
                   'Алексея Константиновича Толстого': '05.09.1817',
                   'Фритьоф Нансена': '10.10.1861',
                   'Владимира Обручева': '28.09.1863',
                   'Шарлотты Купер': '22.09.1870',
                   'Людвига Мизеса': '29.09.1881',
                   'Альберто Джакометти': '10.10.1901',
                   'Ванды Якубовской': '10.10.1907',
                   'Бруно Фрейндлиха': '10.10.1909'}
    again = 1
    q_number = 5
    while again:
        correct_answers = 0
        random_celebrities = random.sample(celebrities.keys(), q_number)
        for person in random_celebrities:
            answer = check_answer(celebrities, person)
            if answer:
                correct_answers += 1
        statistic_output(correct_answers, q_number - correct_answers)
        again = input('Хотите запустить викторину снова - Да/Нет?: ').lower()
        if again == 'да':
            again = 1
            print('Продолжаем...\n')
        elif again == 'нет':
            again = 0
            print('Викторина закончена, спасибо за ваши ответы!')
        else:
            print('Викторина закончена, т.к. вы ввели не понятное значение')
            break