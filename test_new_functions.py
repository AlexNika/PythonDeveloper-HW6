from datetime import datetime
from cfmlib import *
import module.my_bank_account as mba


def test_save_ls2file():
    current_path = pwd_()
    filename = 'listdir.txt'
    # files_and_folders = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            files_test = f.readline()
            folders_test = f.readline()
        f.close()
        files_test = files_test[6:-1].split(', ')
        folders_test = folders_test[5:].split(', ')
        files = ls_a(current_path)
        folders = ls_d(current_path)
        assert files_test.sort() == files.sort()
        assert folders_test.sort() == folders.sort()


def test_account_clear_balance_and_history():
    cdt = datetime.today().strftime('%d.%m.%Y')
    usd, euro = mba.get_exchange_rate(cdt)
    my_test_account = mba.Account(5000, [], 1, 0, usd, euro)
    my_test_account.buy(1500, 'Еда')
    balance_test = 0
    history_test = []
    plus_test = 0
    minus_test = 0
    my_test_account.clear_balance()
    my_test_account.clear_history()
    total_amount = my_test_account.get_balance(usd, euro)
    history = my_test_account.history
    plus = my_test_account.plus
    minus = my_test_account.minus
    assert balance_test == total_amount
    assert history_test == history
    assert plus_test == plus
    assert minus_test == minus


def test_exchange_rate():
    now = '01.11.2019'
    usd_test = 63.7748
    euro_test = 71.1918
    usd, euro = mba.get_exchange_rate(now)
    assert usd_test == usd
    assert euro_test == euro
