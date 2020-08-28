from functions import isLeapYear, daysInMonth, findIndex, getStudentInfo
from data import cities, studentCourses, aboutStudent

myYear = 2012
myMounth = 9
myCity = 'Baku'

resultLeapYear = isLeapYear(myYear)
print(f"is my year is Leap year: {resultLeapYear}")

resultDaysInMounth = daysInMonth(myYear, myMounth)
print(f"in my mounth have {resultDaysInMounth} days")

resulMyCityIndex = findIndex(cities, myCity)
print(f"My city index is: {resulMyCityIndex}")

# without * and ** print in same line
getStudentInfo(*studentCourses, **aboutStudent)



