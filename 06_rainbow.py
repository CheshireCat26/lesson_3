# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
width = 1200
height = 600
sd.resolution = (width, height)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
i = 0
for color in rainbow_colors:
    sd.line(sd.Point(50, 50 + (5 * i)), sd.Point(350, 450 + (5 * i)), color, 4)
    i += 1

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
i = 0
for color in rainbow_colors:
    sd.circle(sd.Point(width // 2, -height // 2 - (5 * i)), radius=height - (5 * i), color=color, width=10)
    i += 1
sd.pause()
