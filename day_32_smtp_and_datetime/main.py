""" Birthday email sender """

import os
import smtplib
import datetime as dt
from random import choice

import pandas as pd

PATH       = "./letter_templates"
SMTP_HOST  = "smtp.gmail.com"
SENDER     = "dhilipsabari1997@gmail.com"
SENDER_PWD = "blahblahblah"


def replace_name(file, word_to_replace, replace_with):
    with open(file) as letter:
        contents = letter.read()
        return contents.replace(word_to_replace, replace_with)


def send_mail(email, mail_body):
    with smtplib.SMTP(SMTP_HOST) as connection:
        connection.starttls()
        connection.login(user=SENDER, password=SENDER_PWD)
        connection.sendmail(
            from_addr=SENDER, to_addrs=email,
            msg=f"Subject: Birthday Wishes\n\n{mail_body}"
        )


now   = dt.datetime.now()
month = now.month
day   = now.day

contents = pd.read_csv("birthdays.csv")
for index, row in contents.iterrows():
    birth_month = int(row.month)
    birth_day   = int(row.day)
    if f"{month}-{day}" == f"{birth_month}-{birth_day}":
        file = choice(os.listdir(PATH))
        path = f"{PATH}/{file}"
        modified_letter = replace_name(path, "[NAME]", row.full_name)
        send_mail(row.email, modified_letter)
