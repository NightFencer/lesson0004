# -*- coding: utf-8 -*-

# pip install simple_draw

import simple_draw as sd

sd.resolution = (1300, 700)
# нарисовать треугольник из точки (50, 300) с длиной стороны 200
length = 200
point = sd.get_point(30, 30)
v1 = sd.get_vector(point, 0, 200, 3)
v1.draw()
v1 = sd.get_vector(v1.end_point, 120, 200, 3)
v1.draw()
v1 = sd.get_vector(v1.end_point, 240, 200, 3)
v1.draw()


# v1 = sd.get_vector(start_point=point, angle=0, length=200, width=3)
# v1.draw()
#
# v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=200, width=3)
# v2.draw()
#
# v3 = sd.get_vector(start_point=v2.end_point, angle=240, length=200, width=3)
# v3.draw()

# определить функцию рисования треугольника из заданной точки с заданным наклоном
def triangle(point, angle=0):
    vect = sd.get_vector(point,angle,200,4)
    vect.draw()
    for i in range(1,3):
        vect = sd.get_vector(vect.end_point, angle + i * 120, 200, 4)
        vect.draw()

point = sd.get_point(300, 300)
triangle(point,angle=3.3333)
point = sd.get_point(400, 0)
triangle(point,angle=90)
point = sd.get_point(800, 600)
triangle(point,angle=180)
point = sd.get_point(600, 100)





    #
    # v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=3)
    # v1.draw()
    #
    # v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=200, width=3)
    # v2.draw()
    #
    # v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=200, width=3)
    # v3.draw()


# point_0 = sd.get_point(300, 300)
#
# for angle in range(0, 361, 30):
#     triangle(point=point_0, angle=angle)

sd.pause()
