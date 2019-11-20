# create Branch HW5
import os
import sys
import shutil
import platform

__author__ = 'Александр Николаев'
__version__ = '1.0.1'
__status__ = 'Development'


def separator(symbol, count=55):
    return symbol * count


def show_main_menu(sep='-', sep_count=55):
    print('Консольный файловый менеджер')
    print(separator('-', sep_count))
    print('1. Создать папку')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Посмотреть содержимого рабочей директории')
    print('5. Сохранить содержимое рабочей директории в файл')
    print('6. Посмотреть только папки')
    print('7. Посмотреть только файлы')
    print('8. Просмотр информации об операционной системе')
    print('9. Создатель программы')
    print('10. Играть в викторину')
    print('11. Мой банковский счет')
    print('12. Смена рабочей директории')
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
            print(f'ERROR - Не хватает прав доступа на удаление папки: {name_}' if os.path.isdir(name_) else
                  f'ERROR - Не хватает прав доступа на удаление файла: {name_}')
        except OSError:
            if os.path.isdir(name_):
                print(f'ERROR - Невозможно удалить. Папка не пустая: {name_}')
                confirm = input(f'Удалить папку {name_} в любом случае (Да/Нет)?:').lower()
                if confirm == 'да':
                    shutil.rmtree(name_)
            else:
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
    return [item for item in os.listdir(path) if os.path.isdir(item)]


def ls_a(path):
    # - Посмотреть только файлов
    return [item for item in os.listdir(path) if os.path.isfile(item)]


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


def get_author_info():
    return __author__, __version__, __status__


def is_correct_choice(choice, menu_items):
    return choice.isdigit() and 0 <= int(choice) <= len(menu_items)


def save_ls2file(filename, files, folders):
    files = f'files: {", ".join(files)}\n'
    folders = f'dirs: {", ".join(folders)}'
    is_exist = False
    if os.path.exists(filename):
        is_exist = True
    with open(filename, 'w') as f:
        f.write(files)
        f.write(folders)
    f.close()
    return is_exist
