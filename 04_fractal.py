# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1300, 700)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,
def draw_branches_v1(start_point, angle, branch_length):
    delta_angle = random.randint(20, 41)
    angle_left = angle + delta_angle
    angle_right = angle - delta_angle
    vector_left = sd.get_vector(start_point, angle_left, branch_length)
    vector_right = sd.get_vector(start_point, angle_right, branch_length)
    sd.line(start_point, vector_left.end_point)
    sd.line(start_point, vector_right.end_point)
    end_left = vector_left.end_point
    end_right = vector_right.end_point
    delta_length_left = 0.01 * random.randint(70, 151)
    branch_length_left = int(branch_length * 0.75 * delta_length_left)
    delta_length_right = 0.01 * random.randint(70, 151)
    branch_length_right = int(branch_length * 0.75 * delta_length_right)
    if branch_length > 3:
        draw_branches(end_left, angle_left, branch_length_left)
        draw_branches(end_right, angle_right, branch_length_right)
    return end_left, end_right  # ,current_angle


def draw_branches_v2(start_point, angle, branch_length):
    vector = sd.get_vector(start_point, angle, branch_length)
    end_vector = vector.end_point
    sd.line(start_point, end_vector)
    limit_angle = 40
    limit_length_branch = 20
    delta_angle = 30*random.randint(100-limit_angle,101+limit_angle)/100

    start_point = end_vector
    angle_left = angle - delta_angle
    angle_right = angle + delta_angle
    branch_length=int(branch_length*0.75*random.randint(100-limit_length_branch,101+limit_length_branch)/100)
    if branch_length>2:
        draw_branches_v2(start_point,angle_left,branch_length)
        draw_branches_v2(start_point, angle_right, branch_length)



root_point = sd.get_point(700, 0)
draw_branches_v2(start_point=root_point, angle=90, branch_length=150)

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
