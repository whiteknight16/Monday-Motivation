import smtplib
import datetime as dt
import random
my_mail="youremail"
password="your app password"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail,password=password)
    if (dt.datetime().weekday()==1):
        with open("./quotes.txt") as quote:
            quotes=quote.readlines()
            quotes=[i.split('\n', 1)[0] for i in quotes]
            connection.sendmail(from_addr=my_mail,to_addrs="reciver_address",msg=f"Subject:Monday Motivation\n\n{random.choice(quotes)}")
