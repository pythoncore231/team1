year = int(input("year = "))

if( (year % 4) == 0):
    if (year % 100) == 0:
        if not (year % 400) == 0:
            print("{0} is a leap year" .format ("year"))

        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

is_not_leap = True
if ((year % 4) == 0):
    if (year % 100) == 0:
        if not (year % 400) == 0:
            print("{0} is a leap year".format("year"))
            is_not_leap = False
if is_not_leap:
    print "{} is a leap year".format(year)

print "{} {} {}".format(1,2,3)
print "{2} {0} {1} {2}".format(1,2,3)

        # # if (year % 4) == 0 and (year % 100) == 0 and not (year % 400):
# if (year % 4) == 0 and (year % 100) == 0 and (year % 400) != 0:
#     print("{0} is a leap year".format(year))
# else:
#     print("{0} is not a leap year".format(year))