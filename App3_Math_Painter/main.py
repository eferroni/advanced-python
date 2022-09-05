from random import randint
from canvas import Canvas
from shape import Rectangle, Square

COLORS = {
    "white": (255, 255, 255),
    "black": (0, 0, 0)
}

canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))
canvas_color = input("Enter canvas color (white or black): ")
canvas = Canvas(width=canvas_width, height=canvas_height, color=COLORS[canvas_color])

while True:
    shape = input("What do you want to draw? Enter q for quit.")

    if shape == 'q':
        break

    if shape not in ['rectangle', 'square']:
        print('Sorry, you dont have this shape for you...')
        continue

    x = int(input(f"Enter the x of the {shape}: "))
    y = int(input(f"Enter the y of the {shape}: "))
    red = input(f"How much red should the {shape} have? ")
    green = input(f"How much red should the {shape} have? ")
    blue = input(f"How much red should the {shape} have? ")
    if shape == 'rectangle':
        rec_width = int(input("Enter the width of the rectangle: "))
        rec_height = int(input("Enter the height of the rectangle: "))
        rectangle = Rectangle(
            x=x,
            y=y,
            color=(red, green, blue),
            height=rec_height,
            width=rec_width
        )
        rectangle.draw(canvas)
    elif shape == 'square':
        sq_length = int(input("Enter the length of the square: "))
        square = Square(
            x=x,
            y=y,
            color=(red, green, blue),
            length=sq_length,
        )
        square.draw(canvas)


canvas.make('images/canvas.png')