def print_dict(obj):
    for key in obj:
        if isinstance(obj[key], dict): # type(obj[key]) == 'dict':
            print key, ":"
            for j in obj[key]:
                print "\t{}: {}".format(j,  obj[key][j])
        else:
             print "{}:{}".format(key, obj[key])


#a = get_rates_by_date("2009-03-03")
#print a
#print_dict(a)