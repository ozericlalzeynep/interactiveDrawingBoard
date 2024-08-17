import turtle

drawingBoard = turtle.Screen()
drawingBoard.bgcolor("light green")
drawingBoard.title("Python Turtle")

instanceTurtle = turtle.Turtle()

def turtleForward():
    instanceTurtle.forward(100)

def rotateRight():
    #instanceTurtle.right(10)
    instanceTurtle.setheading(instanceTurtle.heading() - 10)

def rotateLeft():
    instanceTurtle.left(10)

def turtleReturnHome():
    instanceTurtle.penup()
    instanceTurtle.home()
    instanceTurtle.pendown()

def clearScreen():
    instanceTurtle.clear()
    turtleReturnHome()

def turtlePenUp():
    instanceTurtle.penup()

def turtlePenDown():
    instanceTurtle.pendown()

drawingBoard.listen()
drawingBoard.onkey(fun=turtleForward,key="space")
drawingBoard.onkey(fun=rotateRight, key="Down")
drawingBoard.onkey(fun=rotateLeft, key="Up")
drawingBoard.onkey(fun=clearScreen, key="c")
drawingBoard.onkey(fun=turtleReturnHome, key="o")
drawingBoard.onkey(fun=turtlePenUp, key="u")
drawingBoard.onkey(fun=turtlePenDown, key="d")

turtle.mainloop()