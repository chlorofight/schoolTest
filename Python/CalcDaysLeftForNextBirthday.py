import datetime

birth = datetime.date(1980, 5, 23)
print("Birth: ", birth)

today = datetime.date.today()
print("Today: ", today)

if(
    today.month == birth.month
    and today.day >= birth.day
    or today.month > birth.month
):
    nextBirthdayYear = today.year + 1
else:
    nextBirthdayYear = today.year

nextBirthday = datetime.date(
    nextBirthdayYear, birth.month, birth.day
)

print("Next birthday: ", nextBirthday)

diff = nextBirthday - today

print("Days left for next birthday: ", diff.days)