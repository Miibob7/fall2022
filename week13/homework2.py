import turtle
t= turtle.Turtle()
t.pen(pencolor = "blue", fillcolor = "yellow", pensize = 3, speed = 3)
turtle.Screen().bgcolor("dark blue")

#face and border
t.begin_fill()
t.penup()
t.goto(0, -100)
t.pendown()
t.circle(150)
t.penup()
t.end_fill()

#left eye

t.color("blue")
t.goto(-60, -50)

t.begin_fill()
t.pendown()
t.circle(25)
t.penup()
t.end_fill()

#right eye

t.forward(100)
t.begin_fill()
t.pendown()
t.circle(25)
t.penup()
t.end_fill()

#mouth

t.pensize(12)
t.goto(-47, 67)
t.left(35)
t.pendown()
t.forward(30)
t.right(45)
t.pendown()
t.forward(50)
t.right(30)
t.pendown()
t.forward(30)




