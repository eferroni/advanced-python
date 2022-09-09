import yagmail
from decouple import config
import pandas
from news import NewsFeed
import datetime


gmail_user = config('GMAIL_USER')
gmail_password = config('GMAIL_PASSWORD')

df = pandas.read_csv('people.csv')

email = yagmail.SMTP(user=gmail_user, password=gmail_password)

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
today = datetime.datetime.now().strftime('%Y-%m-%d')

for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today,
                         language='en').get()
    content = f"Hi {row['name']}\nThis is the body:\n{news_feed}\nThanks"

    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today",
               contents=content,
               attachments='design.txt')
