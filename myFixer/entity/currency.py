import fixer.validation_check as validation


class Currency(object):
    def __init__(self, date, base, rates):
        self.date = date
        self.base = base
        self.rates = rates

    def __repr__(self):
        return "{}({})".format(self.base, self.date)

    def __str__(self):
        template = "base: {}\n".format(self.base)
        template += "date: {}\n".format(self.date)
        template += "rates:"
        for key in self.rates:
            template += "\t{}: {}\n".format(key, self.rates[key])
        return template

    def print_in_cols(self, *others):
        if not isinstance(others, tuple) or others.count(self) == 0:
            return
        for other in others:
            if not isinstance(other, Currency):
                return
        # split data by week
        weeks = [others[i:i + 7] for i in range(0, others.__len__(), 7)]
        template = ""
        for week in weeks:
            template += "base: {}".format(self.base)
            template += "\ndate: "
            for rate in week:
                template += "{:<10}\t".format(rate.date)
            template += "\nrates:\n"
            keys = self.rates.keys()
            for key in keys:
                template += " {}: ".format(key)
                for rate in week:
                    template += "{:<10}\t".format(rate.rates[key])
                template += "\n"
        return template

    def exchange(self, amount, to):
        if not isinstance(amount, int):
            return
        if not validation.base_validations(to):
            return
        rate = self.rates[to]
        return "{} {} = {} {}".format(amount, self.base, amount * rate, to)

    def difference(self, *others):
        if not isinstance(others, tuple):
            return
        for other in others:
            if not isinstance(other, Currency):
                return
        if len(others) == 1:
            if not self.base == other.base:
                return
            template = "base: {}\n".format(self.base)
            template += "date: {}\t{}\n".format(self.date, other.date)
            template += "rates:{}difference:\n".format('\t' * 7)
            for key in self.rates:
                template += " {}: {:<10}\t{:<10}\t{}\n".format(key,
                                                               self.rates[key],
                                                               other.rates[key],
                                                               other.rates[key] - self.rates[key])
            return template
        elif len(others) > 1:
            if others.count(self) == 0:
                return
            template = ""
            template += "base: {:<10}\t".format(self.base)
            template += "\ndate: "
            for i in range(1, len(others)):
                template += "{:<10}\t".format(others[i].date)
            template += "\ndifferences:\n"
            keys = self.rates.keys()
            for key in keys:
                template += " {}: ".format(key)
                for i in range(1, len(others)):
                    template += "{:<10}\t".format(round(others[i].rates[key] - others[i-1].rates[key], 5))
                template += "\n"
            return template
        else:
            return

    def day_of_min_rate(self, to, *data):
        if not validation.base_validations(to):
            return
        if not isinstance(data, tuple):
            return
        for other in data:
            if not isinstance(other, Currency):
                return
        rates = [(rate.rates[to], rate.date) for rate in data]
        minValue = min(rates, key=lambda t: t[0])
        return "{}: {}".format(minValue[1], minValue[0])