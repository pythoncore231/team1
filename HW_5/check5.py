# def date_validations(date):
#     """
#     :param date(str):
#     :return True or False (if error):
#     """

#     if not isinstance(date, str):
#         print "Input date must be type string"
#         return False

#     parts = date.split('-')
#     if not len(parts) == 3:
#         print "Entered date must have format YYYY-DD-MM"
#         return False

#     num = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
#     for part in parts:
#         for i in part:
#             if not i in num:
#                 print "Entered date include incorrect symbols"
#                 return False

#     year = int(parts[0])
#     if year < 1999:
#         print "Incorrect year input"
#         return False

#     month = int(parts[1])
#     if not month in range(0, 12):
#         print "Incorrect month input"
#         return False

#     day = int(parts[2])
#     leapYear = year % 4 == 0 and not (year % 100) == 0 or year % 400 == 0
#     if day < 0 or not (month in (1, 3, 5, 7, 8, 10, 12) and day <= 31 or \
#                                     month in (4, 6, 9, 11) and day <= 30 or \
#                                     leapYear and month == 2 and day <= 29 or \
#                                     not leapYear and month == 2 and day <= 28):
#         print "Incorrect day input"
#         return False

#     return True

# print date_validations("2017-03-20")
a = "1999-12-14"
if not isinstance(a, str):
    print "it must be type (str)"
    


parts = a.split('-')
if not len(parts) == 3:
    print "the date must be in format YYYY-DD-MM"
else:
    "correct"

num = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
for part in parts:
    for i in part:
        if not i in num:
             print "Entered date include incorrect symbols"
                
year = int(parts[0])
if year < 1999:
    print "Incorrect year input"
        

month = int(parts[1])
if not month in range(0, 13):
    print "Incorrect month input"
        
day = int(parts[2])
leapYear = year % 4 == 0 and not (year % 100) == 0 or year % 400 == 0
if day < 0 or not (month in (1, 3, 5, 7, 8, 10, 12) and day <= 31 or \
                                    month in (4, 6, 9, 11) and day <= 30 or \
                                    leapYear and month == 2 and day <= 29 or \
                                    not leapYear and month == 2 and day <= 28):
    print "Incorrect day input"
        

bases = ('EUR', 'SD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',
              'HF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AD', 'CHF', 'KRW',
              'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RB', 'INR', 'MXN',
              'CZK', 'BRL', 'PLN', 'PHP', 'ZAR', 'USD')

for base in bases:
    if not base in bases:
        print "Incorrect valute input"
    else:
        print "Correct"