class Currency(object):
    """docstring for Currency"""
    def __init__(self, date, base, rates):
        self.date = date
        self.base = base
        self.rates = rates
    def __repr__(self):
        return "<{} {}>".format(self.base, self.date)

    def __str__(self):
        template = "{} {}\n".format(self.base, self.date)
        count = 0
        for key in self.rates:
            template += "{}: {}".format(key, self.rates[key])
            if not count % 6:
                template += "\n"
            else:
                template += "\t"
            count += 1
        return template
    def __sub__(self, other):
        result = {}
        for key in self.rates:
            result[key] = self.rates[key] - other.rates[key]
        return result
    def sub(self, other):
        result = {}
        for key in self.rates:
            result[key] = self.rates[key] - other.rates[key]
        return result
    
   