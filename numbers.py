#Lets play with numbers
from datetime2 import Date

name = "Jade"

age = 24

actual_age = 24.2

print(name , age)

print(type(name))

print(type(age))

print(type(actual_age))

#figure out age


year_born = 1998
this_year = 2022
todays_date = Date.today().gregorian


print(this_year - year_born)