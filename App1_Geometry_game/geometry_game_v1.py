from random import randint
import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point_1.x <= self.x <= rectangle.point_2.x and rectangle.point_1.y <= self.y <= rectangle.point_2.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

    def __str__(self) -> str:
        return f'Point Coords: {self.x}, {self.y}'


class Rectangle:
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2

    def __str__(self) -> str:
        return f'Rectangle Coords: {self.point_1.x}, {self.point_1.y} and {self.point_2.x}, {self.point_2.y}'

    def get_area(self):
        x = abs(self.point_1.x - self.point_2.x)
        y = abs(self.point_1.y - self.point_2.y)
        return x * y


class GuiRectangle(Rectangle):
    def draw(self, canvas):
        x = abs(self.point_1.x - self.point_2.x)
        y = abs(self.point_1.y - self.point_2.y)
        canvas.penup()
        canvas.goto(self.point_1.x, self.point_1.y)

        canvas.pendown()
        canvas.forward(x)
        canvas.left(90)
        canvas.forward(y)
        canvas.left(90)
        canvas.forward(x)
        canvas.left(90)
        canvas.forward(y)


class GuiPoint(Point):
    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


myturtle = turtle.Turtle()

rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)), Point(randint(10, 400), randint(10, 400)))
rectangle.draw(canvas=myturtle)

user_point = GuiPoint(randint(0, 9), randint(0, 9))
user_point.draw(canvas=myturtle)

turtle.done()