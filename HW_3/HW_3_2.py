# -*- coding: utf-8 -*-

year = int(raw_input(u'Введіть рік: '))
month = int(raw_input(u'Введіть місяць: '))
day = int(raw_input(u'Введіть день: '))


if year % 4 == 0 and year % 100 != 0:
    leap = True
elif year % 400 == 0:
    leap = True
else:
    leap = False

# Місяць
if month < 1 or month > 12:
    print u"#0 Невірно вказано місяць"

# 1
if day <= 0:
    print u"#1 Невірно вказано день"
# 1.1
if day > 31:
    print u"#1.1 Невірно вказано день"
# 2
if month == 2:
    # 2.1
    if leap is True and day > 29:
        print u"#2.1 Невірно вказано день"
    # 2.2
    elif leap is False and day > 28:
        print u"#2.2 Невірно вказано день"
    # 2.3
    else:
        print u"#2.3 {} рік, {} місяць, {} день.".format(year, month, day)
# 3
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    # 3.1
    if day > 31:
        print u"#3.1 Невірно вказано день"
    # 3.2
    else:
        print u"#3.2 {} рік, {} місяць, {} день.".format(year, month, day)
# 4
if month == 4 or month == 6 or month == 9 or month == 11:
    # 4.1
    if day > 30:
        print u"#4.1 Невірно вказано день"
    # 4.2
    else:
        print u"#4.2 {} рік, {} місяць, {} день.".format(year, month, day)
