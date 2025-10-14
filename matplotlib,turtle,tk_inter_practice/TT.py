# Turtle code
"""
Turtle Graphics Theory:

1. Basic Concepts:
    - Turtle graphics simulates a turtle with a pen moving on a canvas
    - The turtle can move forward/backward and turn left/right
    - Commands build drawings step by step

2. Main Components:
    - Screen: The drawing canvas
    - Turtle: The drawing cursor
    - Pen: Controls line properties (color, width)

3. Common Commands:
    - forward()/backward(): Move turtle
    - right()/left(): Rotate turtle
    - penup()/pendown(): Control drawing
    - color(): Set pen color
    - begin_fill()/end_fill(): Fill shapes

4. Coordinates:
    - Default (0,0) is screen center
    - Positive x is right
    - Positive y is up
"""
# import turtle 
# screen = turtle.Screen()
# screen.bgcolor("black")
# pen = turtle.Turtle()
# pen.pensize(5)
# pen.color("red","yellow")
# pen.begin_fill()
# for i in range(4):
#     pen.forward(100)
#     pen.right(90)

# pen.end_fill()
# pen.hideturtle()
# turtle.done()  

# import turtle 

# screen = turtle.Screen()
# screen.bgcolor("black")
# pen = turtle.Turtle()
# pen.pensize(5)
# pen.speed(5)
# pen.color("red","yellow")

# # colors = ["red", "purple", "blue", "green", "orange", "yellow"]
# pen.begin_fill()
# for i in range(6):
#     pen.forward(100)
#     pen.right(60)

# pen.end_fill()
# pen.hideturtle()
# turtle.done()  


# import turtle 

# screen = turtle.Screen()
# screen.bgcolor("black")
# pen = turtle.Turtle()
# pen.pensize(5)
# pen.speed(5)
# pen.pensize(3)

# colors = ["red", "purple", "blue", "green", "orange", "yellow"]
# pen.begin_fill()
# for i in range(5):
#     pen.pencolor(colors[i % 6])
#     pen.forward(100)
#     pen.right(72)

# pen.end_fill()
# pen.hideturtle()
# turtle.done()  


# import turtle 

# screen = turtle.Screen()
# screen.bgcolor("black")
# pen = turtle.Turtle()
# pen.pensize(5)
# pen.speed(5)

# colors = ["red", "purple", "blue", "green", "orange", "yellow"]
# pen.begin_fill()
# for i in range(3):
#     pen.pencolor(colors[i % 3])
#     pen.backward(100)
#     pen.right(120)

# pen.end_fill()
# pen.hideturtle()
# turtle.done()  

# import turtle 

# screen = turtle.Screen()
# screen.bgcolor("black")
# pen = turtle.Turtle()
# pen.pensize(5)
# pen.speed(5)

# colors = ["red", "purple", "blue", "green", "orange", "yellow"]
# pen.begin_fill()
# for i in range(5):
#     pen.pencolor(colors[i % 6])
#     pen.forward(100)
#     pen.right(144)

# pen.end_fill()
# pen.hideturtle()
# turtle.done()  


# import turtle 

# screen = turtle.Screen()
# screen.bgcolor("black")
# pen = turtle.Turtle()
# pen.pensize(5)
# pen.speed(5)
# a=100
# b=50
# pen.color("red","yellow")
# pen.begin_fill()
# for i in range(2):
#     pen.forward(a)
#     pen.right(90)
#     pen.forward(b)
#     pen.right(90)

# pen.end_fill()
# pen.hideturtle()
# turtle.done() 


# 1. Square
# import turtle
# pen = turtle.Turtle()
# pen.color("red", "yellow")
# pen.begin_fill()
# for _ in range(4):
#     pen.forward(100)
#     pen.right(90)
# pen.end_fill()
# turtle.done()

#2. Rectangle
# import turtle
# pen = turtle.Turtle()
# pen.color("blue", "green")
# pen.begin_fill()
# for _ in range(2):
#     pen.forward(150)
#     pen.right(90)
#     pen.forward(80)
#     pen.right(90)
# pen.end_fill()
# turtle.done()

# #3. Circle
# import turtle

# pen = turtle.Turtle()
# pen.color("purple", "pink")
# pen.begin_fill()
# pen.circle(60)
# pen.end_fill()
# turtle.done()

# #4. Triangle
# import turtle

# pen = turtle.Turtle()
# pen.color("black", "orange")
# pen.begin_fill()
# for _ in range(3):
#     pen.forward(120)
#     pen.right(120)
# pen.end_fill()
# turtle.done()

# #5. Pentagon
# import turtle

# pen = turtle.Turtle()
# pen.color("brown", "lightgreen")
# pen.begin_fill()
# for _ in range(5):
#     pen.forward(100)
#     pen.right(72)
# pen.end_fill()
# turtle.done()

# #6. Hexagon
# import turtle

# pen = turtle.Turtle()
# pen.color("darkblue", "lightyellow")
# pen.begin_fill()
# for _ in range(6):
#     pen.forward(80)
#     pen.right(60)
# pen.end_fill()
# turtle.done()

# #7. Star
# import turtle

# pen = turtle.Turtle()
# pen.color("darkred", "lightblue")
# pen.begin_fill()
# for _ in range(5):
#     pen.forward(150)
#     pen.right(144)
# pen.end_fill()
# turtle.done()

# #8. Spiral
# import turtle

# pen = turtle.Turtle()
# pen.color("navy")
# pen.speed(0)
# for i in range(50):
#     pen.forward(i * 5)
#     pen.right(45)
# turtle.done()

# #9. Spirograph
# import turtle

# pen = turtle.Turtle()
# pen.color("magenta")
# pen.speed(0)
# for i in range(36):
#     pen.circle(100)
#     pen.right(10)
# turtle.done()