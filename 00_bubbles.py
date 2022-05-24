# -*- coding: utf-8 -*-
import random

import simple_draw as sd

width = 1200
height = 600
sd.resolution = (width, height)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.Point(width // 2, height // 2)
for step in range(1, 4):
    sd.circle(point, 5 * step)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def draw_bubble(centre, step, color=sd.COLOR_YELLOW):
    for i in range(1, 4):
        sd.circle(centre, step * i, color)


# Нарисовать 10 пузырьков в ряд
start_point = sd.Point(width//10 - 5, height//10)
for i in range(1, 11):
    point = sd.Point(start_point.x * i, start_point.y)
    draw_bubble(point, 5)

# Нарисовать три ряда по 10 пузырьков
for j in range(1, 4):
    start_point = sd.Point(width//10 - 5, height//10 - 5)
    for i in range(1, 11):
        point = sd.Point(start_point.x * i, start_point.y * j)
        draw_bubble(point, 5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for i in range(100):
    point = sd.Point(random.randint(0, width), random.randint(0, height))
    color = sd.random_color()
    draw_bubble(point, 15, color)
sd.pause()
