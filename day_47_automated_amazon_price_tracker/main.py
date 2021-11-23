"""
Automated amazon price tracker.
"""

import lxml
import smtplib
import requests

from bs4 import BeautifulSoup


# get the html page of the product
PRODUCT_URL = "https://www.amazon.in/Google-Pixel-Black-128GB-Storage/dp/B08CFSZLQ4/ref=sr_1_1?keywords=pixel&qid=1637643911&qsid=259-5096711-2734632&sr=8-1&sres=B08CFSZLQ4%2CB08H8X23ZB%2CB07K2JSCX5%2CB08H8Y7W47%2CB07K46215Z%2CB08H85VZNX%2CB092TGMKXN%2CB07L3SV833%2CB09K57BX2N%2CB09KBH177X%2CB07K5GLZ8J%2CB086C82QM8%2CB09FH2HDW9%2CB08XJBPCTR%2CB0884H12PN%2CB09HJZPFDD&srpt=CELLULAR_PHONE"

HEADERS = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0",
}

response = requests.get(PRODUCT_URL, headers=HEADERS).text

# prepare the soup and extract the price as float value.
soup = BeautifulSoup(response, "lxml")
price_span_tag = soup.find("span", id="priceblock_ourprice")
price_text = price_span_tag.get_text().split("₹")[1]
price = float(price_text.replace(",", ""))

# send an email alert if the price is below the present value.
SMTP_HOST = "smtp.gmail.com"
SENDER = "dhilipsabari1997@gmail.com"
SENDER_PWD = "blahblahblah"


def send_mail(email, mail_body):
    with smtplib.SMTP(SMTP_HOST) as connection:
        connection.starttls()
        connection.login(user=SENDER, password=SENDER_PWD)
        connection.sendmail(
            from_addr=SENDER,
            to_addrs=email,
            msg=f"Subject: Amazon Price Alert!\n\n{mail_body}",
        )


mail_body = """Price Drop"""

if price <= 25000.00:
    send_mail("random_email@gmail.com", mail_body)
