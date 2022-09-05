
class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def make(self):
        pass


class Figure:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


class Rectangle(Figure):
    def __init__(self, x, y, color, width, height):
        Figure.__init__(self, x, y, color)
        self.width = width
        self.height = height

    def draw(self, canvas):
        pass


class Square(Figure):
    def __init__(self, x, y, color, length):
        Figure.__init__(self, x, y, color)
        self.length = length

    def draw(self, canvas):
        pass
