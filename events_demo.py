import turtle


def move_forward():
   nonte.forward(30)

def turn_left():
   nonte.left(45)

def turn_right():
   nonte.right(45)

def exit():
    turtle_screen.bye()

def clear():
    nonte.clear()


if __name__ == "__main__":    
    turtle_screen = turtle.Screen()

    nonte = turtle.Turtle() 
    nonte.shape("turtle")

    turtle_screen.onkey(move_forward, "Up")
    turtle_screen.onkey(turn_left, "Left")
    turtle_screen.onkey(turn_right, "Right")
    turtle_screen.onkey(exit, "q")
    turtle_screen.onkey(exit, "Escape")
    turtle_screen.onkey(clear, "c")

    turtle_screen.listen()
    turtle_screen.mainloop()