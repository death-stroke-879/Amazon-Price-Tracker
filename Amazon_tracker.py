import requests
from bs4 import BeautifulSoup
import smtplib

#ADD THE URL OF PRODUCT BELOW
URL = "https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/dp/B073Q5R6VR/ref=sr_1_1?dchild=1&keywords=macbook+air+laptop&qid=1593690723&s=computers&sr=1-1"

#ADD YOUR YOUR OWN USER AGENT "GOOGLE 'MY USER AGENT TO FIND YOURS'"
HEADERS = {"User-Agent": "YOUR UA"}
PRICE_VALUE = 60 #CHANGE THE PRICE TO YOUR DESIRED PRICE
EMAIL_ADDRESS = "youremailaddress@gmail.com"  #ADD YOUR EMAIL ID

def trackPrices():
    price = float(getPrice())
    if price > PRICE_VALUE:
        diff = int(price - PRICE_VALUE)
        print(f"Still ₹ {diff} too expensive")
    else:
        print("Cheaper! Notifying...")
        sendEmail()
    pass

def getPrice():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text().strip()[1:4]
    print(title)
    print(price)
    return price

def sendEmail():
    subject = "Amazon Price Dropped!"
    mailtext='Subject:'+subject+'\n\n'+URL

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ADDRESS, 'Your_Password') #ADD YOUR EMAIL ID AND PASSWORD HERE
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, mailtext)
    pass

if __name__ == "__main__":
    trackPrices()