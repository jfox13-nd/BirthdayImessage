# BirthdayImessage
Will imessage friends and family on their birthdays (Mac only)

Replace all instance of {relevant filepath} with the relavent filepath, and add any birthdays you desire to the script to the dictionary in birthdayList.py. An example birthday is given.

Use Cron Jobs to run the script. You can edit Cron Jobs with the terminal command:
  crontab -e
Add the following text
  0 * * * * {path to python3} {relevant filepath}/birthdayList.py
