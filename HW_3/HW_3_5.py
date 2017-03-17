# -*- coding: utf-8 -*-

k = int(raw_input(u'Введіть день року: '))
if k < 1 or k > 365:
    print u"Введіть число від 1 до 365"
n = (7 + k) % 7
if n == 1:
    print u"Це понеділок"
if n == 2:
    print u"Це вівторок"
if n == 3:
    print u"Це середа"
if n == 4:
    print u"Це четвер"
if n == 5:
    print u"Це п'ятниця"
if n == 6:
    print u"Це субота"
if n == 0:
    print u"Це неділя"
