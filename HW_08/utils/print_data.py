# -*- coding: utf-8 -*-

from fixer.validation import base_validations


def print_dict_rates(obj):
    """
    :param obj(dict):
    :return None:
    """
    if not obj == None:
        for i in obj:
            if isinstance(obj[i], dict):
                print "{}:".format(i)
                for j in obj[i]:
                    print "\t{}: {}".format(j, obj[i][j])
            else:
                print "{}: {}".format(i, obj[i])


def print_dict_rates_by_period(data):
    """
    :param data(generator):
    :return None:
    """
    # for i in data:
    #     print_dict_rates(i)

    l = []
    for obj in data:
        l.append(obj.get('rates'))
    rates = zip(l[0], l[0].values(), l[1].values(), l[2].values())
    for i in rates:
        for j in i:
            print "{}\t".format(j),
        print


def exchange(amount, rates, to):
    """
    :param amount(int):
    :param rates(dict):
    :param to(str):
    :return (float):
    """

    # if not base_validations(to):
    #     return

    if not isinstance(amount, int):
        print "Сума введена некоректно"
        return

    rate = rates.get('rates').get(to)
    if rate:
       return amount * rate
