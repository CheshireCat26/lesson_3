# -*- coding: utf-8 -*-

# (определение функций)
import random

import simple_draw as sd

width = 1200
height = 600
sd.resolution = (width, height)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(centre):
    sd.circle(centre)
    sd.line(sd.Point(centre.x - 20, centre.y - 20), sd.Point(centre.x + 20, centre.y - 20))
    sd.line(sd.Point(centre.x - 30, centre.y + 20), sd.Point(centre.x - 10, centre.y + 20))
    sd.line(sd.Point(centre.x + 10, centre.y + 20), sd.Point(centre.x + 30, centre.y + 20))


for i in range(10):
    smile(sd.Point(random.randint(0, width), random.randint(0, height)))

sd.pause()
