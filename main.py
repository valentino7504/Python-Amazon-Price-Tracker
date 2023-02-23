from bs4 import BeautifulSoup
import requests
import smtplib

my_email = YOUR_EMAIL
my_password = YOUR_PASSWORD

laptop_stand_url = "https://www.amazon.com/Lapdesk-Storage-Sitting-Portable-Foldable/dp/B09Q98835Z/ref=sr_1_3_sspa?crid=26P1YG9WX6YPD"
amazon_request_headers = {
    "User-Agent": YOUR_USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}
response = requests.get(laptop_stand_url, headers=amazon_request_headers)
soup = BeautifulSoup(response.text, "lxml")
price = float(soup.select_one("span.a-offscreen").text[1:])
product_name = soup.select_one("span#productTitle").text.strip()
threshold_value = 35

if price < threshold_value:
    connection = smtplib.SMTP_SSL("smtp.gmail.com", port = 465)
    connection.login(user=my_email, password = my_password)
    connection.sendmail(from_addr=my_email, to_addrs= my_email, msg=f'Subject: PRICE DROP ALERT\n\nThe price of "{product_name}" has dropped below ${threshold_value}. Go pay up nowwwwwwww')
