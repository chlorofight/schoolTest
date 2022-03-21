import datetime
from datetime import date

currentdate = date.today()

dateborn = input('please enter date of birth MM/DD/YY')
dateborndate = (datetime.datetime,(dateborn,'%m/%d/%Y')

birthday = date(dateborn.year,dateborn.month,dateborndate.day)
print('this is the year your birthday will fall on') ,int(birthday), int(dateborndate)

timeToBirth = birthday - dateborn

print(timeToBirth)