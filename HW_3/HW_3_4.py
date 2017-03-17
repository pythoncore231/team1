# -*- coding: utf-8 -*-

side_A = float(raw_input(u'Введіть розмір сторони A: '))
side_B = float(raw_input(u'Введіть розмір сторони B: '))
side_C = float(raw_input(u'Введіть розмір сторони C: '))
Perimeter = (side_A + side_B + side_C)
polu_P = Perimeter / 2
S = float

if side_A >= side_B + side_C or side_B >= side_A + side_C or side_C >= side_A + side_B:
    print "{}".format(u"Трикутників з такими сторонами не існує")
else:
    S = (polu_P * (polu_P - side_A) * (polu_P - side_B) * (polu_P - side_C)) ** 0.5
    print u"Периметр такого трекутника {}".format(Perimeter)
    print u"Площа такого трикутника {}".format(S)
