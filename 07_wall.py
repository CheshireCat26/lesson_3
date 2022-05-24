# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
width = 1200
height = 600
sd.resolution = (width, height)


def draw_brick(left_right_corner):
    point_a = left_right_corner
    point_b = sd.Point(left_right_corner.x + 100, left_right_corner.y)
    point_c = sd.Point(left_right_corner.x, left_right_corner.y + 50)
    point_d = sd.Point(left_right_corner.x + 100, left_right_corner.y + 50)

    sd.line(point_a, point_b)
    sd.line(point_a, point_c)
    sd.line(point_c, point_d)


for x in range(0, width, 100):
    for y in range(0, height, 50):
        draw_brick(sd.Point(x, y))

sd.pause()
