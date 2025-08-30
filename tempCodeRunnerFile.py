import turtle 

screen = turtle.Screen()
screen.bgcolor("black")
pen = turtle.Turtle()
pen.speed(5)
pen.pensize(3)

colors = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(360):
    pen.pencolor(colors[i % 6])
    pen.forward(100)
    pen.right(60)
    pen.forwar