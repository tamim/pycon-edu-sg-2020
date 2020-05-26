import turtle

class StrangeTurtle(turtle.Turtle):
    """StrangeTurtle is a class for new type of turtle"""
    def forward(self, pixel):
        super().backward(pixel)

    def backward(self, pixel):
        super().forward(pixel)

    def left(self, angle):
        super().right(angle)

    def right(self, angle):
        print("I won't turn right, because I am ajob!")


if __name__ == "__main__":
    monty = StrangeTurtle()

    jhonty = turtle.Turtle()
    jhonty.shape("turtle")

    monty.left(30)
    jhonty.left(30)

    monty.forward(200)
    jhonty.forward(200)

    monty.left(45)
    jhonty.left(45)

    monty.backward(100)
    jhonty.backward(100)

    monty.right(90)
    jhonty.right(90)

    monty.forward(10)
    jhonty.forward(10)

    turtle.done()