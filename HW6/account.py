import datetime

class AccountOperation:
    def __init__(self, value, balance):
        self.timestamp =  datetime.datetime.now()
        self.value = value
        self.balance = balance
        self._timestamp_str = self.timestamp.strftime("%d.%m.%Y %H:%M:%S")
        self._value_str = '+' + str(value) if value > 0 else str(value)
        self._balance_str = str(balance)

    def to_string(self):
        return '\t'.join((self._timestamp_str, self._value_str, self._balance_str))

class Account:
    def __init__(self, balance = 0):
        assert isinstance(balance, int)
        assert balance >= 0
        self._balance = balance
        self._operations = []

    def check_balance(self):
        return self._balance

    def put(self, amount : int):
        assert isinstance(amount, int)
        assert amount >= 0

        self._balance += amount
        self._operations.append(AccountOperation(amount, self._balance))
        return self._balance

    def withdraw(self, amount : int):
        assert isinstance(amount, int)
        assert amount >= 0

        if self._balance >= amount:
            self._balance -= amount
            self._operations.append(AccountOperation(-amount, self._balance))
            return self._balance
        return None

    def get_operation_history(self, cnt = 10):
        amount_to_show = min(cnt, len(self._operations))
        return self._operations[-amount_to_show:]