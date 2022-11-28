# Использовал шаблон декоратор

from abc import ABC, abstractmethod


class BaseProcessing(ABC):
    def __init__(self):
        self._money_on_debit_card = 0.0
        self._money_on_deposit = 0.0

    @abstractmethod
    def deposit_money(self, value: float):
        pass

    def get_debit_card_balance(self) -> float:
        return self._money_on_debit_card

    def get_deposit_balance(self) -> float:
        return self._money_on_deposit


class TinkoffProcessingDecorImpl(BaseProcessing):
    def __init__(self):
        super().__init__()
        self._logger = Logger()

    def deposit_money(self, value: float):
        self._logger.info(f'Newe debit request. Amount = {value}.')
        self._money_on_debit_card += value / 2
        self._money_on_deposit += value / 2


class TinkoffProcessing(TinkoffProcessingDecorImpl):
    def deposit_money(self, value: float):
        super().deposit_money(value)
        self._money_on_debit_card += value


class Logger:
    def info(self, message: str):
        print(f"Log INFO message: {message}")


def client_code():
    account = TinkoffProcessing()
    print(f"Debit card: {account.get_debit_card_balance()}")
    print(f"Deposit: {account.get_deposit_balance()}")

    account.deposit_money(100)

    print(f"Debit card: {account.get_debit_card_balance()}")
    print(f"Deposit: {account.get_deposit_balance()}")


if __name__ == "__main__":
    client_code()