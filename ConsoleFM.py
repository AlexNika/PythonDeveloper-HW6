# create Branch HW5
import module.my_bank_account as mba
import module.quiz_game as qg
from cfmlib import *
from datetime import datetime

sep_count = 55

while True:
    show_main_menu()
    print(separator('-', sep_count))
    current_path = pwd_()
    do = input('Выберите действие(1...11) или 0 для окончания работы: ')
    if do == '1':
        folder_name = input('Введите имя папки, которую надо создать: ')
        md_(current_path, folder_name)
        print(separator('-', sep_count))
    elif do == '2':
        name = input('Введите имя папки или файла, которые надо удалить: ')
        rm_(current_path, name)
        print(separator('-', sep_count))
    elif do == '3':
        source_name = input('Введите имя папки или файла, которые надо скопировать: ')
        destination_name = input('Введите новое имя папки или файла: ')
        cp_(current_path, source_name, destination_name)
        print(separator('-', sep_count))
    elif do == '4':
        folders_and_files = []
        folders = ls_d(current_path)
        files = ls_a(current_path)
        folders_and_files += (folders + files)
        for item in folders_and_files:
            print(item)
        print(separator('-', sep_count))
    elif do == '5':
        filename = 'listdir.txt'
        files = ls_a(current_path)
        folders = ls_d(current_path)
        tmp = save_ls2file(filename, files, folders)
        if tmp:
            print(f'Файл {filename} - перезаписан')
        else:
            print(f'Файл {filename} - создан')
        print(separator('-', sep_count))
    elif do == '6':
        folders = ls_d(current_path)
        for item in folders:
            print(item)
        print(separator('-', sep_count))
    elif do == '7':
        files = ls_a(current_path)
        for item in files:
            print(item)
        print(separator('-', sep_count))
    elif do == '8':
        info = get_system_info()
        for k, v in info.items():
            print(f'{k} - {v}')
        print(separator('-', sep_count))
    elif do == '9':
        author, version, status = get_author_info()
        print(f'Дата: {datetime.now()}')
        print(f'Автор программы: {author}')
        print(f'Версия программы: {version}')
        print(f'Статус программы: {status}')
        print(separator('-', sep_count))
    elif do == '10':
        qg.quiz_game()
        print(separator('-', sep_count))
    elif do == '11':
        mba.my_bank_account()
        print(separator('-', sep_count))
    elif do == '12':
        folder_name = input('Введите имя папки, в которую надо перейти: ')
        cd_(current_path, folder_name)
        print(separator('-', sep_count))
    elif do == '0':
        print('Выполение программы закончено. До свидания!')
        print(separator('-', sep_count))
        break
    else:
        print('Неверный пункт меню')
        print(separator('-', sep_count))