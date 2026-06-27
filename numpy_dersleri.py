import numpy as np

# Manuel bir liste oluşturup diziye çevirelim
liste = [1, 2, 3, 4, 5]
dizi = np.array(liste)

print("Dizi:", dizi)
print("Tipi:", type(dizi)) # <class 'numpy.ndarray'> olduğunu göreceksin

liste2 = [5 , 2 ,3,4]
dizi2 = np.array(liste2)
print(dizi2)

#Dtype 
#En Sık Kullanılanlar:

#int32 / int64: Tam sayılar.

#float32 / float64: Ondalıklı sayılar (Yapay zekada genelde 32 tercih edilir).

#uint8: 0-255 arası tam sayılar (Görüntü işleme ve renkler için standarttır).


#reshape methodu 


dizi3 = np.reshape(liste2,(2,2))
print(dizi3)

dizi4 = np.array(liste2).reshape(2,2)
print(dizi4)

#eğer satırı verip sütünü kendisinin doldurmasını istersek sütün kısmına -1 yazmamız yeterlidir
dizi4 = np.array(liste2).reshape(1,-1)
print(f"dizi4 = {dizi4}" )

#sifirlar 
sifirmatris = np.zeros((2,2))
print(sifirmatris)

#birler 
birler = np.ones((5,5))
print(birler)

#Küçük bir ipucu: np.ones kullandığında varsayılan olarak float64 tipinde oluşturur.
#Eğer piksellerle uğraşacaksan np.ones((10,10), dtype='uint8') demeyi unutma, yoksa her "1" sayısı bellekte devasa yer kaplar!
#full 
full = np.full((3,2),12)
print(full)

#Uint8 kullanımı

# 5x5 boyutunda tamamen siyah (0) bir resim oluşturalım
# dtype='uint8' demezsek boşuna bellekte yer kaplarız
resim = np.zeros((5, 5), dtype='uint8')

# Tam ortadaki pikseli beyaz (255) yapalım
resim[2, 2] = 255
resim[2,1]= 200
resim[1,2]= 200
resim[2,3]= 200
resim[3,2]= 200

print(resim)

#np.arrange 

#np.arange(başlangıç , bitiş(dahil değil) , artış miktarı) şeklinde kullanılır
dizi5 = np.arange(4,10,)
print(dizi5)

#Python'daki range()den Farkı Ne?
#işte burası çok önemli! Standart Python range() fonksiyonuyla yapamadığın ama
#np.arange() ile yapabildiğin en büyük şey ondalıklı (float) adım kullanmaktır.


# Standart range() ile bunu yapamazsın, hata verir:
dizi_ondalik = np.arange(0, 1, 0.1)
# Çıktı: [0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

#np.linspace

#bu komut verilen bir aralığı verilen sayı kadar eşit parçaya ayırmaya yarar
#np.array(başlangıç, bitiş, adet) şeklinde çalışır
dizi = np.linspace(0, 10, 5)
# Çıktı: [ 0. ,  2.5,  5. ,  7.5, 10. ]
#DİKKAT
#burada çıktıya bakılınca bitiş sayısının dahil olduğu gmrülüyor

#eğer son sayını dahil olmasını istemiyorsa "endpoint" kullanarak çıkarabiliriz
dizi = np.linspace(0, 10, 5, endpoint=False)
# Çıktı: [0., 2., 4., 6., 8.]

dizi6 = np.linspace(0,10,4)
print(dizi6)

#birim matris (np.eye)

birim = np.eye(3)
#içerisine yazılan sayı matrisin kaça kaçlık oldupunu belirler
# Çıktı:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

dizi7 = np.eye(5,2 ,2 )
print(dizi7)

#köşegen matris np.diag

#bu metodun 2 farklı kullanmı vardır

#1 koşegen matris oluşturma 
#içine bir liste verirsen o listeyi köşegene koyar ve geri kalanları sıfır yapar

liste3 = (1,2,3,4)
dizi8 = np.diag(liste3)
print(dizi8)

#2. köşegeni çekmek
#eğer içerisine bir matris verirsen bunu köşegenini alıp sana çıktı olarak geri veriri

matris = (
[2,1,3],
[5,4,5],
[1,6,4])
dizi9 = np.diag(matris)
print(dizi9)

#üçgen matrisler np.triu , np.tril

#matrisi çaprazdan ikiye böldüğünü düşün np.triu (upper) çaprazdan üst kısmı verir np.tril (lower) alt üçgeni verir

matris = (
    [2,1,3],
    [5,4,5],
    [1,6,4])
print(np.tril(matris))
#[[2 0 0]
# [5 4 0]
# [1 6 4]]
print(np.triu(matris))
#[[2 1 3]
# [0 4 5]
# [0 0 4]]
print(np.triu(matris, k=1))#k değerinin 1 yapılması durumunda matrisin köşegeni sıfırlanır
#[[0 1 3]
# [0 0 5]
# [0 0 0]]

#np.copy
#bu bir dizinin kopyasını çıkarır ve bunun üzerinde yapılan değişiklik orjinalini etkilemez
orijinal = np.array([1, 2, 3])
kopya = np.copy(orijinal)
kopya[0] = 99  # Orijinal dizi bundan etkilenmez.
print(orijinal) #[1 2 3]
print(kopya) #[99  2  3]


#np.fromiter
#Sürekli veri üreten yapılardan (iterator) veya jeneratörlerden (generator) veri çekmek için kullanılır.

liste = (x*x for x in range(5)) # Bu bir jeneratördür
dizi10 = np.fromiter(liste, dtype=int,count=2) 
print(dizi10)# Çıktı: [0, 1, 4, 9, 16] değil [0,1]

#np.loadtxt
#Genellikle .txt veya .csv gibi, içinde karmaşık olmayan, düzgün sıralanmış sayısal verilerin olduğu dosyaları okur.
#Zorunlu Parametre: fname (Dosya adı veya yolu).

#Önemli Parametreler:

#delimiter: Verilerin neyle ayrıldığı (Virgül mü ,, boşluk mu  ?). Varsayılanı boşluktur.

#skiprows: Dosyanın başındaki kaç satırı (başlıkları) atlayacağını belirtir.

#usecols: Sadece belirli sütunları almak istersen (Örn: usecols=(0, 2) sadece 1. ve 3. sütunu alır).

#Hata Payı: Eğer dosyada eksik veri varsa (bazı hücreler boşsa) bu fonksiyon hata verir ve çalışmaz.



#np.genfromtxt() - "Akıllı" Dosya Okuma
#loadtxt'in daha gelişmiş ve "hata toleranslı" versiyonudur. Dosyada eksik veya bozuk veriler varsa bunları yönetebilir.

#Zorunlu Parametre: fname.

#Öne Çıkan Parametreler:

#missing_values: Dosyadaki hangi ifadelerin "eksik veri" kabul edileceğini belirtir.

#filling_values: Eksik olan yerlere ne yazılacağını belirler (Örn: Boş yerleri 0 ile doldur).s

#names=True: Eğer dosyanın ilk satırı sütun isimleriyse bunu belirtirsen veriye isimle ulaşabilirsin.




#np.ravel metodu
#bu metod bir matrisi alıp tek satırlı bir matrise dönüştürür
#orjinal matrisi ekliler

dizi11 = np.ravel(matris)
matris = (
[2,1,3],
[5,4,5],
[1,6,4])
print(dizi11)

#np.flatten
#bu ravel ile neredeyse aynıdır en öenmli farkı bu metod orjinal matrisi etkilemez bellekte yeni bir kopya oluşturur
#yeni kopya oluşturduğu için yavaştır

dizi12 = np.array(matris)
print(dizi12.flatten())


#np.newaxis ve np.expand_dims
print("---------------")
dizi13 = np.array([1, 2, 3]) # Şu anki şekli: (3,) -> Yani sadece 3 elemanlı bir sıra.

# --- YÖNTEM A: np.newaxis (Daha "Pythonic" ve hızlıdır) ---
# Diziyi satır matrisi yapmak (1 satır, 3 sütun)
satir_matrisi = dizi13[np.newaxis, :] # Şekil: (1, 3)
print(satir_matrisi)
# Diziyi sütun matrisi yapmak (3 satır, 1 sütun)
sutun_matrisi = dizi13[:, np.newaxis] # Şekil: (3, 1)
print(sutun_matrisi)
# --- YÖNTEM B: np.expand_dims() (Daha okunabilirdir) ---
# axis=0 demek "En başa bir boyut ekle" demek
genis_dizi = np.expand_dims(dizi11, axis=(1)) # Şekil: (1, 3)
print(genis_dizi)


#np.squeeze
# Sadece 2. indeksteki (en sondaki) 1'i sil:
#yeni_veri = np.squeeze(resim_verisi, axis=2) 
# Sonuç Şekli: (1, 3)
#burada axis değerini -1 vererek en sondan da başlayabiliriz

#np.vstack

ust = np.array([1, 2, 3])
alt = np.array([4, 5, 6])

sonuc = np.vstack((ust, alt))
# Çıktı:
# [[1, 2, 3],
#  [4, 5, 6]] -> Şekil (2, 3) oldu.

#np.hstack

sol = np.array([[10], [20]])
sag = np.array([[30], [40]])

sonuc = np.hstack((sol, sag))
# Çıktı:
# [[10, 30],
#  [20, 40]] -> Şekil (2, 2) oldu.

#np.concatenate() (Genel Birleştirme)
#Hepsini kapsayan ana fonksiyondur. axis parametresi ile yönü sen belirlersin.

#axis=0: Dikey birleştirir (vstack gibi).

#axis=1: Yatay birleştirir (hstack gibi).
dizi14 = np.concatenate((sol , sag) , axis=1)
print(dizi14)

#np.split
notlar = np.array([[50, 60], 
                   [70, 80], 
                   [90, 100], 
                   [40, 30]])

notlar = np.split(notlar,2)
print(notlar)

#np.stack

a = np.array([1, 2])
b = np.array([3, 4])

yeni = np.stack((a, b), axis=0)
print(yeni)
# Çıktı: [[1, 2], [3, 4]] -> Artık bir matrisin var!

#matrisin transpozu 
#matrisin yanına .T eklemen yeterlidir
matris = np.array([[1, 2], 
                   [3, 4], 
                   [5, 6]]) # Şekil: (3, 2)

transpoze = matris.T
# Çıktı:
# [[1, 3, 5],
#  [2, 4, 6]] # Şekil: (2, 3)
transpoze = np.transpose(matris ,(1 ,0))
# Çıktı :
# [[1 3 5]
# [2 4 6]] 


#np.moveaxis
#bu verinin içeriğini değiştirmeden boyutların sırasını değiştirir

# Önce (3, 100, 100) bir veri uyduralım
veri = np.zeros((3, 100, 100))

# 0. boyutu (kanallar) al ve 2. (en son) sıraya taşı:
yeni_veri = np.moveaxis(veri, 0, 2)

print(yeni_veri.shape) # Çıktı: (100, 100, 3)

#Alternatif: np.swapaxes()
#Tabloda hemen yanında duran bir diğer arkadaş ise swapaxes. Bu daha basittir; sadece iki boyutun yerini birbiriyle takas eder.

# 0. ve 2. boyutun yerini birbiriyle değiştir:
yeni_veri = np.swapaxes(veri, 0, 2)
# Sonuç: (100, 100, 3)


#np add np.power
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

# Bu ikisi aynı şeyi yapar:
print(a + b)           # [11, 22, 33]
print(np.add(a, b))    # [11, 22, 33]

# Üs alma (Power)
print(np.power(a, 2))  # [100, 400, 900]


#np.mean

matris = np.array([[1, 2, 3], 
                   [4, 5, 6]])

# 1. Genel Ortalama (Tüm sayılar)
print(np.mean(matris)) # 3.5

# 2. Sütun Bazlı (Yukarıdan aşağı - axis=0)
# Her sütunun kendi ortalamasını verir.
print(np.mean(matris, axis=0)) # [2.5, 3.5, 4.5]

# 3. Satır Bazlı (Soldan sağa - axis=1)
# Her satırın kendi ortalamasını verir. Senin dediğin buydu!
print(np.mean(matris, axis=1)) # [2.0, 5.0]


#. Yuvarlama ve Sınırlandırma (Clip)
#Özellikle np.clip() metoduna dikkat etmeni istiyorum. Görüntü işlemede piksellerin 0 ile 255 arasında kalmasını sağlamak için hayati önem taşır.

#np.around(): En yakın tam sayıya yuvarlar.

#np.floor(): Her zaman aşağı (tabana) yuvarlar.

#np.ceil(): Her zaman yukarı (tavana) yuvarlar.

#np.clip(dizi, min, max): Sayıları belirli bir aralığa hapseder.

dizi = np.array([10, 50, 100, 200])
# Sayıları 20 ile 80 arasına hapset:
print(np.clip(dizi, 20, 80)) 
# Çıktı: [20, 50, 80, 80] -> 10 olan 20 oldu, 100 ve 200 olanlar 80'e takıldı.




#np.where

#Kullanımı: np.where(koşul, doğruysa_ne_olsun, yanlışsa_ne_olsun)
#Örnek: Sınıftaki 50'den küçük notları "Kaldı", büyükleri "Geçti" yapmak.
notlar = np.array([40, 70, 30, 90])

# 50'den küçükse 0 yap, değilse olduğu gibi bırak (notlar)
yeni_notlar = np.where(notlar < 50, 0, notlar)
# Çıktı: [0, 70, 0, 90]




#np.isnan()  np.isinf  np.any() np.all() 

# İçinde hatalı veriler olan bir dizi oluşturalım
# np.nan -> Boş/Eksik veri
# np.inf -> Sonsuz veri (Bir sayının 0'a bölünmesi gibi)
veriler = np.array([10, np.nan, 20, np.inf, 30])


# --- np.isnan() ---
# Eksik verileri bulur.
print(np.isnan(veriler)) 
# Çıktı: [False, True, False, False, False] -> 2. eleman nan

# --- np.isinf() ---
# Sonsuz değerleri bulur.
print(np.isinf(veriler)) 
# Çıktı: [False, False, False, True, False] -> 4. eleman inf

# --- np.any() ve np.all() ---
# any: "İçeride en az bir tane True var mı?"
# all: "İçerideki HER ŞEY True mu?"
print(np.any(np.isnan(veriler))) # Çıktı: True (Evet, en az bir tane nan var)
print(np.all(veriler > 0))       # Çıktı: False (Çünkü nan ve inf sayısal karşılaştırmayı bozar)


numbers= np.array([[1,25],[66,73],[234,23]])
print(numbers[1:3,1])
np.random.seed(23)
randoms = np.random.randint(2,10,3)
print(randoms)


numbers1 = np.array([10,15,30,45,60])
numbers2 = np.arange(5,15)
numbers3 = np.arange(50,100,5)
numbers4 = np.zeros(10)
numbers5 = np.ones(10)
numbers6 = np.linspace(0,100,5) 
numbers7 = np.random.randint(10,30,5)
numbers8 = np.linspace(-1,1,10) 
numbers9 = np.random.randint(10,50,15).reshape(3,5)
numbers10 = numbers9.sum()
numbers11_1 = numbers9.max()
numbers11_2 = numbers9.min()
numbers11_3 = numbers9.mean()
numbers12 = np.where(numbers9 == np.max(numbers9))
numbers13 = np.arange(11,20)[0:2]
numbers14 = numbers13[::-1] 
numbers15 = numbers9[1]
numbers16 = numbers9[2:3]
numbers17 = numbers9[:1]
numbers18 = np.square(numbers9)
numbers19 = numbers9[(numbers9 % 2 == 0) & (numbers9 > 0) ]
print(numbers1)
print(numbers2)
print(numbers3)
print(numbers4)
print(numbers5)
print(numbers6)
print(numbers7)
print(numbers8)
print(numbers9)
print(numbers10)
print(numbers11_1)
print(numbers11_2)
print(numbers11_3)
print(numbers12)
print(numbers13)
print(numbers14)
print(numbers15)
print(numbers16)
print(numbers17)
print(numbers18)
print(numbers19)
