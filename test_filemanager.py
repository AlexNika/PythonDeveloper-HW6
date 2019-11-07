from cfmlib import *
import module.my_bank_account as mba
import contextlib


def test_get_system_info():
    """
    :return: test assertions for "get_system_info" function from console file manager
    """
    info = get_system_info()
    assert info.get('Архитектура') == ('32bit', 'WindowsPE')
    assert info.get('Платформа') == 'win32'
    assert info.get('Операционная система') == 'Windows'
    assert info.get('Версия операционной системы') == '10'
    assert info.get('Релиз операционной системы') == '10.0.18362'
    assert info.get('Архитектура процессора') == 'AMD64'
    assert info.get('Модель процессора') == 'Intel64 Family 6 Model 58 Stepping 9, GenuineIntel'
    assert info.get('Имя компьютера') == 'VEGA'


def test_get_author_info():
    """
    :return: test assertions for "get_author_info" function from console file manager
    """
    assert get_author_info()[0] == 'Александр Николаев'


def test_version_info():
    """
    :return: test assertions for "get_version_info" function from console file manager
    """
    assert get_author_info()[1] == '1.0.1'


def test_status_info():
    """
    :return: test assertions for "get_status_info" function from console file manager
    """
    assert get_author_info()[2] == 'Development'


def test_separator():
    """
    :return: test assertions for "separator" function from console file manager
    """
    assert separator('~', 5) == '~~~~~'


def test_is_correct_choice():
    """
    :return: test assertions for correct input from console file manager
    """
    menu_items = ('1. Создать папку',
                  '2. Удалить (файл/папку)',
                  '3. Копировать (файл/папку)',
                  '4. Просмотр содержимого рабочей директории',
                  '5. Посмотреть только папки',
                  '6. Посмотреть только файлы',
                  '7. Просмотр информации об операционной системе',
                  '8. Создатель программы',
                  '9. Играть в викторину',
                  '10. Мой банковский счет',
                  '11. Смена рабочей директории',
                  '0. Выход')
    assert is_correct_choice('0', menu_items) == True


def test_pwd_():
    """
    :return: test assertions for "pwd_" function from console file manager
    Dirty function test!!!
    """
    assert pwd_() == 'C:\\Users\\alexn\\Documents\\GITREPO\\PythonDeveloper\\HW6'


def test_ls_d():
    """
    :return: test assertions for "ls_d" (show only folders) function from console file manager
    Dirty function test!!!
    """
    assert ls_d(pwd_()) == ['.git', '.idea', '.pytest_cache', 'module', 'venv', '__pycache__']


def test_ls_a():
    """
    :return: test assertions for "ls_a" (show only files) function from console file manager
    Dirty function test!!!
    """
    assert ls_a(pwd_()) == ['.gitignore', 'cfmlib.py', 'ConsoleFM.py', 'LICENSE', 'README.md', 'test_filemanager.py',
                            'test_python.py']


def test_md_(monkeypatch):
    """
    :return: test assertions for "md_" (make folder) function from console file manager
    Dirty function test!!!
    """
    folder = 'In_good_we_trust'
    with contextlib.redirect_stdout(None):
        rm_(pwd_(), folder)
        monkeypatch.setattr('builtins.input', lambda x: folder)
        md_(pwd_(), folder)
    assert os.path.exists(folder)
    with contextlib.redirect_stdout(None):
        rm_(pwd_(), folder)


def test_account_initial_state():
    """
    :return:  test assertions for "get_balance" function from bank account module
    """
    my_test_account = mba.Account(1000, [])
    assert my_test_account.get_balance() == 1000


def test_account_state_after_deposit():
    """
    :return:  test assertions for "deposit" function from bank account module
    """
    my_test_account = mba.Account(13000, [])
    my_test_account.deposit(2000)
    assert my_test_account.get_balance() == 15000


def test_account_state_after_purchase():
    """
    :return:  test assertions for "buy" function from bank account module
    """
    my_test_account = mba.Account(5000, [])
    my_test_account.buy(1500, 'Еда')
    assert my_test_account.get_balance() == 3500
