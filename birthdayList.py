import datetime
import os

people = [
    [ 'Contact Name', '2010-10-14' ],
    [ 'Next Contact', '2010-2-1']
]

today = datetime.date.today()
with open('{relevant filepath}/done.txt', 'r') as r:
    check = datetime.datetime.strptime(r.read(), "%Y-%m-%d")
    if check.month == today.month and check.day == today.day and check.year == today.year:
        exit()

for person in people:
    datee = datetime.datetime.strptime(person[1], "%Y-%m-%d")
    if datee.month == today.month and datee.day == today.day:
        os.system("{relevant filepath}/birthday.sh \'{}\'".format(person[0]) )
        with open('{relevant filepath}/done.txt', 'w') as fs:
            fs.write(today.strftime("%Y-%m-%d"))
