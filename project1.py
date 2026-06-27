import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.flo.com.tr/ayakkabi"

response = requests.get(url)
html_icerigi = response.content

soup = BeautifulSoup(html_icerigi , "html.parser")

ayakkabi = soup.find_all("div" , class_="product__name" , limit=5)

ayakkabi_isimleri =[]

for urun in ayakkabi :
    print(urun.text.strip())
    ayakkabi_isimleri.append(urun.text.strip())

print(ayakkabi_isimleri)

fiyatx = soup.find_all("div" , class_="product-pricing-one__price",limit=5)

ayakkabi_fiyatlari =[]

for fiyat in fiyatx:
    print(fiyat.text.strip())
    ayakkabi_fiyatlari.append(fiyat.text.strip())

print(ayakkabi_fiyatlari)

veri = {
    "ürünler":ayakkabi_isimleri,
    "fiyatlar":ayakkabi_fiyatlari
}

df = pd.DataFrame(veri)
print(df)