import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.johnlewis.com/john-lewis-partners-brooks-side-dining-chairs-set-of-2/antique-brown/p3189169")
soup = BeautifulSoup(r.content, "html.parser")
element = soup.find("p", {"class": "price price--large"})

amount = element.text.strip()
price = float(amount[1:])
print(f"The price of the chair is {amount}") 
if price < 300:
    print("You can buy the chair")
else:
    print("Do not buy the chair")