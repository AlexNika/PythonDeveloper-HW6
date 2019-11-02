# create Branch HW5
import os
import sys
import shutil
import platform


def separator(symbol, count=55):
    return symbol * count


def show_main_menu(sep='-', sep_count=55):
    print('Консольный файловый менеджер')
    print(separator('-', sep_count))
    print('1. Создать папку')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только папки')
    print('6. Посмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Смена рабочей директории')
    print('0. Выход')


def pwd_():
    return os.getcwd()


def md_(current_path, *args):
    # - Создать папку
    for name in args:
        dir_ = os.path.join(current_path, name)
        try:
            os.mkdir(dir_)
        except TypeError:
            print(f'ERROR - Неверно задан тип имени папки: {dir_}')
        except FileExistsError:
            print(f'ERROR - Невозможно создать. Папка уже существует: {dir_}')
        except PermissionError:
            print(f'ERROR - Не хватает прав доступа на создание папки: {dir_}')
        except OSError:
            print(f'ERROR - Синтаксическая ошибка в имени папки: {dir_}')
        else:
            print(f'Директория {dir_} создана.')


def rm_(current_path, *args):
    # - Удалить (файл/папку)
    for name in args:
        name_ = os.path.join(current_path, name)
        try:
            if os.path.exists(name_):
                if os.path.isdir(name_):
                    os.rmdir(name_)
                    print(f'Папка {name_} удалена.')
                elif os.path.isfile(name_):
                    os.remove(name_)
                    print(f'Файл {name_} удален.')
            else:
                print(f'ERROR - Невозможно удалить. Файл/папка не существует: {name_}')
        except PermissionError:
            if os.path.isdir(name_):
                print(f'ERROR - Не хватает прав доступа на удаление папки: {name_}')
            elif os.path.isfile(name_):
                print(f'ERROR - Не хватает прав доступа на удаление файла: {name_}')
        except OSError:
            if os.path.isdir(name_):
                print(f'ERROR - Невозможно удалить. Папка не пустая: {name_}')
                confirm = input(f'Удалить папку {name_} в любом случае (Да/Нет)?:').lower()
                if confirm == 'да':
                    shutil.rmtree(name_)
            elif os.path.isfile(name_):
                print(f'ERROR - {OSError.filename} : {OSError.strerror}')


def cp_(current_path, source, destination):
    # - Копировать (файл/папку)
    if source == destination:
        print('WARNING: Копирование файла/папки в самих себя невозможно!!!')
    else:
        source_ = os.path.join(current_path, source)
        destination_ = os.path.join(current_path, destination)
        try:
            if os.path.exists(source_):
                if os.path.isdir(source_):
                    shutil.copytree(source_, destination_)
                    print(f'Папка {source_} скопирована.')
                elif os.path.isfile(source_):
                    shutil.copyfile(source_, destination_)
                    print(f'Файл {source_} скопирован.')
            else:
                print(f'ERROR - Невозможно скопировать. Файл/папка не существует: {source_}')
        except IOError:
            print(f'ERROR - {IOError.strerror}')


def ls_d(path):
    # - Посмотреть только папки
    folders = []
    for item in os.listdir(path):
        if os.path.isdir(item):
            folders.append(item)
    return folders


def ls_a(path):
    # - Посмотреть только файлов
    files = []
    for item in os.listdir(path):
        if os.path.isfile(item):
            files.append(item)
    return files


def get_system_info():
    # - Просмотр информации об операционной системе
    os_, computer_name, os_version, os_build, cpu_architecture, cpu_model = platform.uname()
    architecture = platform.architecture()
    platform_ = sys.platform
    system_info = {'Архитектура': architecture, 'Платформа': platform_, 'Операционная система': os_,
                   'Версия операционной системы': os_version, 'Релиз операционной системы': os_build,
                   'Архитектура процессора': cpu_architecture, 'Модель процессора': cpu_model,
                   'Имя компьютера': computer_name}
    return system_info


def cd_(current_path, new_folder):
    # - Смена рабочей директории
    print(f'Текущая рабочая папка: {current_path}')
    try:
        os.chdir(new_folder)
        print(f'Текущая рабочая папка: {pwd_()}')
    except OSError:
        print(f'ERROR - {OSError.strerror}')
        os.chdir(current_path)
        print(f'Текущая рабочая папка не изменилась: {pwd_}')