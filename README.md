# BirthdayImessage
These scripts will imessage friends and family on their birthdays (Mac only)

Make sure you are sharing your imessage contacts with your computer.

Replace all instance of {relevant filepath} in the file birthdayList.py with the relavent filepath, and add any birthdays you desire to the script to the dictionary in birthdayList.py. The relevant filepath for done.txt is wherever you want to put it on your computer. An example birthday is given.

Replace {Your Personal Contact} with the name of your own imessage contact name in the birthday.sh file.

Use Cron Jobs to run the script. You can edit Cron Jobs with the terminal command:
```
crontab -e
```
Add the following line:
```
0 * * * * {path to python3} {relevant filepath}/birthdayList.py
```
