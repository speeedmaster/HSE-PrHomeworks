# Применил шаблон Object Pool

from abc import ABC, abstractmethod
from time import sleep
from threading import Lock


class DbConnector(ABC):
    def __init__(self):
        # Долгое создание коннектора к базе
        sleep(5)

    @abstractmethod
    def current_time(self) -> str:
        pass


class OracleDb(DbConnector):
    def current_time(self) -> str:
        return "SELECT sysdate FROM dual"


class PostgreSQL(DbConnector):
    def current_time(self) -> str:
        return "SELECT 'now'::datetime"

class DBPoolMeta(type):
    versions = {}
    lock = Lock()

    def __call__(cls, *args, **kwargs):
        cls.lock.acquire()
        if cls not in cls.versions:
            version = super().__call__(*args, **kwargs)
            cls.versions[cls] = version
        cls.lock.release()
        return cls.versions[cls]


class DBPool(metaclass=DBPoolMeta):
    pool = {}

    def get_factory(self, type):
        if type not in self.pool:
            if type == 'oracle':
                self.pool[type] = OracleDb()
            elif type == 'postgres':
                self.pool[type] = PostgreSQL()
        return self.pool[type]

# коннектор к пулу объектов


class DBPoolConnector():
    def __init__(self, type):
        self.type = type

    def current_time(self):
        return DBPool().get_factory(self.type)


def client_code(connector: DBPoolConnector) -> None:
    print(f"Run DB queue: {connector.current_time()}")


if __name__ == "__main__":
    client_code(DBPoolConnector('oracle'))
    client_code(DBPoolConnector('postgres'))

    client_code(DBPoolConnector('oracle'))
    client_code(DBPoolConnector('postgres'))
