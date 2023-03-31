import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

URL = "https://www.amazon.com/Schwinn-Discover-Hybrid-Bicycle-womens/dp/B0030UESQY/ref=sr_1_3?keywords=bike&sr=8-3&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-GB,en;q=0.8"
}

response = requests.get(url=URL, headers=headers)
data = response.content
soup = BeautifulSoup(data, 'lxml')
# checks the price of the product
price_soup = soup.find(name="span", class_="a-size-mini olpMessageWrapper")
price = float(price_soup.get_text(strip=True).split("$")[1])

# if the price is lower or equal to what we can afford, it sends an email as a notification
if price <= 200:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        my_email = "myemail@gmail.com"
        password = os.environ.get("PASSWORD")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            msg=f"Subject: Bike on Sale!\n\nHey,\n\nThe bike is currently at the low price of ${price}. Buy now!")
