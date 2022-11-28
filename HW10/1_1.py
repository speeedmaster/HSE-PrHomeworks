# Реализовали шаблон синглтон

from threading import Thread, Lock
class SingletonMeta(type):
    lock = Lock()
    versions = {}

    def __call__(cls,*args,**kwargs):
        cls.lock.acquire()
        if cls not in cls.versions:
            version = super().__call__(*args, **kwargs)
            cls.versions[cls] = version
        cls.lock.release()
        return cls.versions[cls]

class ClassMustBeSingleton(metaclass=SingletonMeta):
    # Мы используем это поле, чтобы доказать, что наш Singleton действительно работает.
    value: str = None

    def __init__(self, value: str):
        self.value = value


def check_singleton(value: str) -> None:
    singleton = ClassMustBeSingleton(value)
    print(singleton.value)

if __name__ == "__main__":
    print("Value must be the same!\n"
    "If values are different - there were TWO object creation!")

    process_1 = Thread(target=check_singleton, args=("FOO",))
    process_2 = Thread(target=check_singleton, args=("BOO",))
    process_1.start()
    process_2.start()