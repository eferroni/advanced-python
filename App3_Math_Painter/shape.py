class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


class Rectangle(Shape):
    def __init__(self, x, y, color, width, height):
        Shape.__init__(self, x, y, color)
        self.width = width
        self.height = height

    def draw(self, canvas):
        canvas.data[
            self.x:(self.x + self.height),
            self.y:(self.y + self.width),
        ] = self.color


class Square(Shape):
    def __init__(self, x, y, color, length):
        Shape.__init__(self, x, y, color)
        self.length = length

    def draw(self, canvas):
        canvas.data[
            self.x:(self.x + self.length),
            self.y:(self.y + self.length),
        ] = self.color
