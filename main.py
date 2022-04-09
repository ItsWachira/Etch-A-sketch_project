from turtle import Turtle, Screen

tim_turtle = Turtle()
screen = Screen()


def move_forward():
    tim_turtle.forward(50)


def move_backwards():
    tim_turtle.backward(50)


def move_anticlockwise():
    tim_turtle.right(90)


def move_clockwise():
    tim_turtle.left(90)


def home():
    tim_turtle.home()
    tim_turtle.clear()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_anticlockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="h", fun=home)

screen.exitonclick()
