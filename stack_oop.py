class Stack:
    def __init__(self):
        self._data = list()

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if len(self._data) > 0:
            self._data.pop()

    def size(self):
        return len(self._data)

    def empty(self):
        return len(self._data) == 0

    def top(self):
        if len(self._data) > 0:
            return self._data[-1]
        return None
