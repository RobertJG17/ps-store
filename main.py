from flask import Flask
from bs4 import BeautifulSoup
from requests import request


app = Flask(__name__)

res = request(url="https://store.playstation.com/en-us/category/35027334-375e-423b-b500-0d4d85eff784/1",
              method="GET")

soup = BeautifulSoup(res.text, parser="lxml", features="lxml")
print(len(soup))
print(soup)
cells = soup.find_all("div", attrs={"class": "ems-sdk-product-tile"})

for cell in cells:
    print(cell)


@app.route('/')
def index():
    return 'yeet'


if __name__ == '__main__':
    app.run()
