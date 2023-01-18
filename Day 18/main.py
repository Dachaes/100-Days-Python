# Day 18 : Turtle Graphic - Spot Painting
import turtle as turtle_module
import random
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.gif', 42)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
#
# print(rgb_colors)

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
turtle_module.colormode(255)
color_list = [(254, 250, 237), (204, 246, 234), (255, 213, 255), (203, 213, 255), (203, 165, 116), (145, 96, 48),
              (73, 103, 135), (183, 149, 54), (214, 213, 131), (136, 65, 79), (69, 110, 76), (138, 170, 145),
              (104, 41, 53), (186, 149, 178), (144, 166, 204), (54, 40, 51), (153, 36, 0), (100, 38, 0),
              (153, 213, 157), (255, 170, 153), (204, 85, 102), (51, 43, 102), (255, 170, 204), (98, 170, 55),
              (102, 128, 204), (96, 85, 0), (221, 213, 0), (204, 170, 255), (255, 85, 51), (0, 43, 63), (0, 85, 102)]
tim.setheading(225)
tim.forward(300)
tim.setheading(180)
tim.forward(15)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
