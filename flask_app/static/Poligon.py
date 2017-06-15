# -*- coding: utf-8 -*-

"""Please provide full program code (on Python language) of parse_number(num) function 
which returns the dict with following structure: 
{odd: number of odd digits in input value, even: number of even digits of input value} 
or false when wrong input value.
num - input number.

NOTE: Assume that the "zero" digit also belongs to even numbers
EXAMPLE OF Inputs/Ouputs when using this function:
>>>print parse_number(34567)
{'odd': 3, 'even': 2}
>>>print parse_number(100)
{'odd': 1, 'even': 2}
>>>print parse_number("word")
False"""


def parse_number(num):

    odd = 0
    even = 0
    num_dict = {}

    if str(num).isdigit():
        for i in str(num):
            if int(i) % 2 == 1:
                odd += 1
            elif int(i) == 0:
                even += 1
            else:
                even += 1
        num_dict['odd'] = odd
        num_dict['even'] = even
        return num_dict

    else:
        print "False"


print parse_number(34567)
print parse_number(100)
print parse_number("word")
