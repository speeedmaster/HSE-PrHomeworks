from account import Account

import pytest

def test_init():
    acc0 = Account()
    assert acc0.check_balance() == 0
    acc1 = Account(100)
    acc1.check_balance() == 100

def test_withdraw():
    acc = Account(100)
    assert acc.put(50) == 150
    assert acc.check_balance() == 150
    assert acc.put(1000) == 1150
    assert acc.check_balance() == 1150

def test_withdraw_ok():
    acc = Account(100)
    assert acc.withdraw(50) == 50
    assert acc.check_balance() == 50
    assert acc.withdraw(30) == 20
    assert acc.check_balance() == 20
    assert acc.withdraw(20) == 0
    assert acc.check_balance() == 0

def test_withdraw_failed():
    acc = Account(100)
    assert acc.withdraw(10000) == None
    assert acc.check_balance() == 100

def test_operations_size():
    acc = Account(100)
    acc.withdraw(10000)
    acc.put(2000)
    acc.withdraw(1000)
    acc.withdraw(1)
    assert len(acc.get_operation_history()) == 3
    acc.withdraw(10000)
    acc.withdraw(1000)
    assert len(acc.get_operation_history()) == 4

def test_operations_content():
    acc = Account(100)
    for i in range(1, 10):
        acc.put(i * 100)
    history = acc.get_operation_history()
    expected_balance = 100
    for i in range(1, 10):
        expected_balance += i * 100
        assert history[i - 1].value == i * 100
        assert history[i - 1].balance == expected_balance
        assert history[i - 1].to_string() == f'{history[i - 1].timestamp.strftime("%d.%m.%Y %H:%M:%S")}\t+{i * 100}\t{expected_balance}'

    for i in range(1, 10):
        acc.withdraw(i * 100)
    history = acc.get_operation_history(9)
    for i in range(1, 10):
        expected_balance -= i * 100
        assert history[i - 1].value == i * -100
        assert history[i - 1].balance == expected_balance
        assert history[i - 1].to_string() == f'{history[i - 1].timestamp.strftime("%d.%m.%Y %H:%M:%S")}\t-{i * 100}\t{expected_balance}'
