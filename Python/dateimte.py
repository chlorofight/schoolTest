import datetime
from datetime import date

currentdate = date.today()
dateborn = input('please enter date of birth m-d-y')
dateborndate = datetime.datetime.strptime(dateborn, '%m/%d/%Y')
daystoo = currentdate - dateborndate
print(daystoo)

