# -*- coding: utf-8 -*-


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


def print_dict_rates_by_period(l):
    """
    :param l(generator):
    :return None:
    """
    keys = l[0].get("rates").keys()
    for each in keys:
        print each, ": \t",
        for rates in l:
            print rates["rates"][each], "\t\t",
        print


def exchange(amount, rates, to):
    """
    :param amount(int):
    :param rates(dict):
    :param to(str):
    :return (float):
    """
    if not isinstance(amount, int):
        print "Сума введена некоректно"
        return

    rate = rates['rates'][to]
    if rate:
       return amount * rate