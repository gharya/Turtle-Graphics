'''
Project 1 - Turtle Art - Spring 2022
Author: Arya Ghaderi 9063-38229

This program uses turtle graphics to generate a drawing of Someone playing basketball

I have neither given or received unauthorized assistance on this assignment.
Signed: Arya Ghaderi
'''

import turtle
turtle.setup(700, 650)
turtle.title('Project 1 - Turtle Art - Arya Ghaderi')

turtle.penup()
turtle.goto(325,0)
turtle.pensize(18)
turtle.pencolor('maroon')

#border
turtle.pendown()
turtle.setheading(90)
turtle.forward(350)
turtle.setheading(180)
turtle.forward(650)
turtle.setheading(270)
turtle.forward(700)
turtle.setheading(0)
turtle.forward(650)
turtle.setheading(90)
turtle.forward(350)

#grass
turtle.penup()
turtle.goto(0,-200)
turtle.setheading(0)
turtle.pencolor('green')
turtle.pendown()
turtle.fillcolor('green')
turtle.begin_fill()
turtle.forward(310)
turtle.setheading(270)
turtle.forward(135)
turtle.setheading(180)
turtle.forward(620)
turtle.setheading(90)
turtle.forward(135)
turtle.setheading(0)
turtle.forward(310)
turtle.end_fill()

#sky
turtle.penup()
turtle.goto(0, -182)
turtle.color('blue')
turtle.pendown()
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.forward(310)
turtle.setheading(90)
turtle.forward(515)
turtle.setheading(180)
turtle.forward(620)
turtle.setheading(270)
turtle.forward(515)
turtle.setheading(0)
turtle.forward(310)
turtle.end_fill()

#sun
turtle.penup()
turtle.goto(225,175)
turtle.pendown()
turtle.begin_fill()
turtle.color('yellow')
turtle.fillcolor('yellow')
turtle.circle(65)
turtle.end_fill()

#right leg
turtle.penup()
turtle.goto(0,-182)
turtle.pensize(15)
turtle.pencolor('black')
turtle.forward(15)
turtle.setheading(135)
turtle.pendown()
turtle.forward(25)

#left leg
turtle.penup()
turtle.goto(0,-182)
turtle.setheading(180)
turtle.forward(20)
turtle.setheading(45)
turtle.pendown()
turtle.forward(25)

turtle.setheading(90)
turtle.forward(100)

#arms
turtle.setheading(315)
turtle.forward(60)
turtle.setheading(135)
turtle.forward(60)
turtle.setheading(180)
turtle.forward(60)

#neck
turtle.setheading(0)
turtle.forward(60)
turtle.setheading(90)
turtle.forward(40)

#head
turtle.penup()
turtle.setheading(0)
turtle.forward(5)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(35)
turtle.end_fill()

#ball
turtle.penup()
turtle.goto(70,-182)
turtle.pencolor('orange')
turtle.setheading(90)
turtle.forward(30)
turtle.pendown()
turtle.fillcolor('orange')
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

#basketball hoop pole
turtle.penup()
turtle.goto(300,-182)
turtle.pencolor('black')
turtle.setheading(90)
turtle.pendown()
turtle.forward(350)

#basketball rim
turtle.setheading(270)
turtle.forward(45)
turtle.pensize(10)
turtle.pencolor('red')
turtle.setheading(180)
turtle.forward(75)

#basketball net
turtle.pencolor('white')
turtle.setheading(270)
turtle.forward(75)
turtle.setheading(0)
turtle.forward(45)
turtle.setheading(90)
turtle.forward(75)

#fix
turtle.pencolor('red')
turtle.setheading(180)
turtle.forward(45)
turtle.color('red')