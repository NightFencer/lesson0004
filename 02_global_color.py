# -*- coding: utf-8 -*-
import simple_draw as sd

# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)
a = (8, 600, 100, 100, 22, (255, 0, 0))


def polygonner(side_quantity, x, y, length, angle_0, color):
    color_s = color
    init_point = sd.get_point(x, y)
    start_point = init_point
    poly_angle = 360 / side_quantity
    for i in range(0, side_quantity):
        vector = sd.get_vector(start_point, angle_0 + poly_angle * i, length)
        finish_point = vector.end_point
        if i == side_quantity - 1:
            finish_point = init_point
        poly_side(start_point, finish_point, color_s)
        start_point = finish_point


def poly_side(start_p, finish_p, color_s):
    sd.circle(start_p, 10)
    sd.line(start_p, finish_p, color_s, 5)
    sd.circle(start_p, 7)


color_dict = {'COLOR_RED': (255, 0, 0), 'COLOR_ORANGE': (255, 127, 0),
              'COLOR_YELLOW': (255, 255, 0),'COLOR_GREEN': (0, 255, 0),
              'COLOR_CYAN': (0, 255, 255), 'COLOR_BLUE': (0, 0, 255),
              'COLOR_PURPLE': (255, 0, 255)}
print('Выберите номер цвета из списка:')
for i in range(0,len(color_dict)):
    print(color_dict['COLOR_RED'])
colors_names = 'COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE'
colors = colors_names.split(', ')
print('Выберете номер цвета:')
for i in range(0, len(colors)):
    colors[i] = colors[i][6:]
    print(i, colors[i])
color_ind = int(input('0-6?'))
if 0<=color_ind<7:
    color_key = 'COLOR_'+ colors[color_ind]
    poly_color =(color_dict[color_key])
else:
    print('Корявый номер, цвет будет белый')
    poly_color =(255,255,255)

poly_side_number = int(input('сколько сторон нарисовать?'))
poly_arg = [poly_side_number,600,100,100,22,poly_color]
polygonner(*poly_arg)

# num = int(input('0-6?'))
#
# if 0 <= num <= 6:
#     print('Вы выбрали', colors[num])
# else:
#     print('Некорректный ввод')
#
# sd.COLOR_RED

# poly_arg = [8,600,100,100,22,(255,0,0)]
# polygonner(*poly_arg)


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код

sd.pause()
