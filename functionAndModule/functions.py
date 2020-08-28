from data import month_days

# return true if leap year other wise return false
def isLeapYear(year):
    # return year % 4 and (year % 100 != 0 or year % 400 == 0)
    if (year % 4) == 0:  
        if (year % 100) == 0:  
            if (year % 400) == 0:  
                return True  
            else:  
                return False  
        else:  
            return True  
    else:  
        return False

# return days in this year
def daysInMonth(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and isLeapYear(year):
        return 29
    return month_days[month]

# give data(list) and searc item
def findIndex(searchData, target):
    for value in range(len(searchData)):
        if searchData[value].lower() == target.lower():
            return value
    return 'Not Found!'

# print student info
def getStudentInfo(*args, **kwargs):
    print(args)
    print(kwargs)