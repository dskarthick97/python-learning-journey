import smtplib
import datetime as dt
from random import choice

my_email = "karthicksabari1997@gmail.com"
password = ""
    
now = dt.datetime.now()
if now.weekday() == 3:
    with open("quotes.txt") as quotes_text_file:
        quotes = quotes_text_file.readlines()
        quote  = choice(quotes)

    # In order for the below code snippet to work, security settings of the sender should be modified
    # 1. MFA - Off
    # 2. Low app security - Off
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, to_addrs="dhilipsabari1997@gmail.com", 
            msg=f"Subject: Thursday Motivation\n\n{quote}"
        )
