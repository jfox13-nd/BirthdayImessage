# BirthdayImessage
These scripts will imessage friends and family on their birthdays (Mac only)

Replace all instance of {relevant filepath} in the file birthdayList.py with the relavent filepath, and add any birthdays you desire to the script to the dictionary in birthdayList.py. The relevant filepath for done.txt is wherever you want to put it on your computer. An example birthday is given.

Use Cron Jobs to run the script. You can edit Cron Jobs with the terminal command:
```
crontab -e
```
Add the following line:
```
0 * * * * {path to python3} {relevant filepath}/birthdayList.py
```
