class Rectangle:
    def __init__(self, height, width = None) -> None:
        assert height > 0.0, 'unable to create rectangle with non-positive heihgt'
        assert width > 0.0, 'unable to create rectangle with non-positive width'
        self._height = height
        self._width = width

    def area(self):
        return self._height * self._width

    def perimeter(self):
        return 2 * (self._height + self._width)

    def shape(self):
        return (self._height, self._width)

class Square(Rectangle):
    def __init__(self, height, width = None) -> None:
        assert height > 0.0, 'unable to create square with non-positive heihgt'
        if width:
            if height != width:
                print('unable to create square with differet height and width, width parameter will be ignored')
        self._height = height
        self._width = height

def check(figure: Rectangle):
    print(f'Got {type(figure).__name__}: {figure.shape()}; area: {figure.area()}; perimeter: {figure.perimeter()}')

if __name__ == '__main__':
    a = Rectangle(10, 25)
    check(a)

    b = Square(10)
    check(b) # принцип Лисков не нарушен

    c = Square(10, 25)
    check(c)

    d = Rectangle(-1, 20)