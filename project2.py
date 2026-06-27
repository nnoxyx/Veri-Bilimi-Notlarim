from bs4 import BeautifulSoup
import pandas as pd
import requests
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

kimlik = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


url = "https://www.direnc.net/yeni-urunler"

response = requests.get(url, headers=kimlik)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi , "html.parser")

ürünx = soup.find_all("a" , class_="col col-12 productDescription" , limit=5)

ürün_isimler =[]

for i in ürünx:
    print(i.text.replace(" ","-"))
    ürün_isimler.append(i.text.replace(" ","-"))

# print(ürün_isimler)

# fiyatx = soup.find_all("span",class_="currentPrice", limit=5)

# fiyatlar =[]

# for a in fiyatx:
    # print(a.text.strip())
    # fiyatlar.append(a.text.strip())

# print(fiyatlar)

# veri = {
#    "ürün" : ürün_isimler,
#    "fiyat" : fiyatlar
#}

# df= pd.DataFrame(veri)

# print(df)


# Siteden çektiğini veya elinde olan ürünlerin listesi
# urun_listesi = ['nike', 'nokia', 'new balance', 'adidas', 'nike air max']

# Otomatik tamamlama aracımızı oluşturuyoruz
# ignore_case=True sayesinde büyük/küçük harf duyarlılığını kaldırıyoruz (Nike = nike)
tamamlayici = WordCompleter(ürün_isimler, ignore_case=True)

print("Aramak istediğiniz ürünü yazmaya başlayın (Klavyedeki yön tuşlarıyla seçip Enter'a basabilirsiniz):")

# Standart input() yerine prompt() kullanıyoruz
secilen_urun = prompt('Ürün adı: ', completer=tamamlayici)

print(f"\n{secilen_urun} ürününü seçtiniz!")
print("Şimdi fiyat ve stok bilgileri hazırlanıyor , lütfen bekleyiniz...")

# Buradan sonra BeautifulSoup kodlarını çalıştırıp seçilen_urun değişkenini kullanarak 
# ilgili sayfanın linkine gidebilir veya detayları çekebilirsin.

urun_link_etiketi = soup.find("a" , title= secilen_urun )

if urun_link_etiketi:
    # Ürünü bulduk! Şimdi o 'a' etiketinin içindeki yönlendirme linkini (href) alıyoruz
    urun_detay_linki = urun_link_etiketi.get("href")

    # Bazen siteler linkleri eksik verir (örn: /nike-ayakkabi). 
    # Eğer öyleyse başına sitenin ana adresini eklemek gerekir:
    urun_detay_linki = "https://www.direnc.net" + urun_detay_linki

    print(f"Ürün bulundu! Detay sayfasına gidiliyor: {urun_detay_linki}")

    # 2. Aşama: Bulduğumuz o yeni linke gidip ürünün içine giriyoruz
    detay_sayfasi = requests.get(urun_detay_linki, headers=kimlik)
    detay_soup = BeautifulSoup(detay_sayfasi.content, "html.parser")
    
    # Artık ürünün kendi sayfasındayız. Fiyatı veya diğer bilgileri çekebiliriz.
    try:
        fiyat = detay_soup.find("span", class_="product-price-tl").text.strip()
        print(f"{secilen_urun.capitalize()} ürününün fiyatı: {fiyat}")
    except AttributeError:
        print("Ürün sayfasına gidildi ama fiyat etiketi bulunamadı.")

else:
    print("Bu isimde bir ürün sayfada bulunamadı.")