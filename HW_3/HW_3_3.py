# -*- coding: utf-8 -*-

a = float(raw_input(u'Введіть a: '))
b = float(raw_input(u'Введіть b: '))
c = float(raw_input(u'Введіть c: '))
x = float
D = b ** 2 - 4 * a * c

if a != 0:
    if D == 0:
        x = -b / 2 * a
        print u"x =", x
    elif D > 0:
        x_1 = (-b + D ** 0.5) / 2 * a
        x_2 = (-b - D ** 0.5) / 2 * a
        print "x_1 = {}".format(x_1)
        print "x_2 = {}".format(x_2)
    else:
        print u"Корінь відсутній"
else:
    print u"'a' не повинно дорівнювати 0"
