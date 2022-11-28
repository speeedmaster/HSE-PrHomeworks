# использовал метод __setattr__

class SimpleCalc:
    def register_operation(self, name, value):
        self.__setattr__(name, value)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":
    calc = SimpleCalc()
    calc.register_operation('add', add)
    calc.register_operation('sub', sub)
    calc.register_operation('pow3', lambda x: x ** 3)
    print(f"5 + 4 = {calc.add(5, 4)}")
    print(f"5 - 4 = {calc.sub(5, 4)}")
    print(f"3^3 = {calc.pow3(3)}")