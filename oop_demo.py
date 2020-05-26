import turtle


nonte = turtle.Turtle()

fonte = turtle.Turtle()

print(type(nonte))

nonte.speed(4)
nonte.shape("circle")

fonte.speed(1)
fonte.shape("square")

nonte.left(30)
nonte.forward(200)
fonte.backward(250)

turtle.exitonclick()