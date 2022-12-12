import random
import turtle
import colorgram

turtle.colormode(255)
tur = turtle.Turtle()
screen = turtle.Screen()

rgb_colors = []
colors = colorgram.extract('hirst_spot.PNG', 30)

#Create a color palette
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

width = screen.window_width()
height = screen.window_height()

radius = int(input("Input Dot size: "))
gap = radius+int(input("Input Gap size:"))

how_many_dotsX = (width-radius/2)/gap
how_many_dotsY = (height-radius/2)/gap
tur.penup()
tur.speed(0)
tur.hideturtle()

#Dot drawing
for i in range(int(how_many_dotsY)):
    tur.goto(-width / 2+radius, -height / 2 + (gap * i)+radius)
    for j in range(int(how_many_dotsX)):
        tur.dot(radius, random.choice(rgb_colors))
        tur.forward(gap)
screen.exitonclick()
