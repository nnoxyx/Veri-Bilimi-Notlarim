import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

"""

x = np.linspace(0,2,100)

plt.plot(x,x,label="linear",color="red")
plt.plot(x,x**2,label="quadric",color="yellow")
plt.plot(x,x**3,label="cubic",color="green")

plt.xlabel("x label")
plt.ylabel("y label")

plt.title("Basic grafic")

plt.legend()
plt.show()


"""



"""
fig,axs =  plt.subplots(3)

x = np.linspace(0,2,100)
axs[0].plot(x, x,label="linear",color="green")
axs[0].set_title("linear")
axs[0].legend()
axs[1].plot(x, x**2,label="quadric",color="blue")
plt.title("b")
axs[2].plot(x, x**3,label="cubic",color="red")
plt.title("c")


plt.legend()
plt.show()


"""


#figure oluşturma


"""
x = np.linspace(-10,9,20)

y = x**3
z = x**2

"""

"""
figure = plt.figure()

axes = figure.add_axes([0.05,0.1,0.4,0.6])
axes.plot(x,y,label="cubic",color='red')
axes.set_xlabel("x1")
axes.set_ylabel("y1")
axes.set_title("cube")
plt.legend("axes") #axes.legend() olarak kullanılır 


axes2= figure.add_axes([0.55,0.1,0.4,0.6])
axes2.plot(x,z,label="quadric",color='g')
axes2.set_xlabel("x2")
axes2.set_ylabel("z1")
axes2.set_title("square")
plt.legend("axes2")  #axes2.legend() olarak kullanılır
"""

"""
figure = plt.figure()

axes = figure.add_axes([0,0,1,1])
axes.plot(x,y,label="square")
axes.plot(x,z,label="cube")
axes.legend(loc=1 )
"""

"""
fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(4,4))

axes[0].plot(x,y,'y')
axes[0].set_title("cube")
axes[1].plot(x,z,'g')
axes[1].set_title("square")

plt.tight_layout()
fig.savefig("figure1.png")



plt.show()

"""

#grafik türleri

yil = [2011,2012,2013,2014,2015]

oyuncu1=[12,15,20,19,16]
oyuncu2=[10,14,17,16,23]
oyuncu3=[18,10,19,15,25]

# Stack plot
"""
plt.plot([],[],color="y",label="oyuncu1")
plt.plot([],[],color="g",label="oyuncu2")
plt.plot([],[],color="b",label="oyuncu3")

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=["y","g","b"])
plt.title("yillara göre atılan goller")
plt.xlabel("yıllar")
plt.ylabel("goller")

plt.legend()
plt.show()


"""

#pie grafik
"""
goal_types = "Penaltı","Kaleye Atılan Şut" , "Serbest Vuruş" 

goals=[5,39,10]
colors=["y","r","b"]

plt.pie(goals,labels=goal_types,colors=colors,shadow= True ,
explode=(0.05,0.05,0.05),autopct="%1.1f%%")

plt.show()
"""

#bar grafik


"""
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="bmw",width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[30,60,50,90,40],label="audi",width=.5)
plt.bar([0.5,1.5,2.5,3.5,4.5],[10,90,40,20,30],label="honda",width=.5)

plt.legend()
plt.xlabel("gün")
plt.ylabel("alınan mesafe")
plt.title("araç bilgileri")
plt.show()
"""

#histogram grafik

"""
yaslar = [22,55,66,34,43,2,3,76,37,89,64,102,100,23,67,34,86,98,68,99,87,69,49,110,120,115]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)
plt.xlabel("yas_gruplari")
plt.ylabel("kişi sayisi")
plt.title("histogram grafik")


plt.show()

"""


# ileri seviye komutlar


"""
#spines kenar çizgileri ayarlamakta kullanılır
#set_position ekseni nereye konulacağını belirler
x = np.linspace(-5,5,100)
y = x**3

fig, ax = plt.subplots(figsize=(8,6))

ax.plot(x,y,color="b", lw=2,label="cubic")

ax.spines["right"].set_color("none")#sağ ve üst çizgileri kaldırma
ax.spines["top"].set_color("none")

ax.spines["left"].set_position(("data",0))#sol ve alt çizgilerini yerini ayarlama
ax.spines["bottom"].set_position(("data",0))

ax.xaxis.set_ticks_position("bottom")#bunlar sayıların nerede görüneceğini belirler
ax.yaxis.set_ticks_position("left")

# Izgara ekleme
ax.grid(True, linestyle=":",alpha=0.6)


ax.legend
plt.show()

"""
# Annotation

x = np.linspace(0, 10, 200)
y = np.sin(x) * np.exp(-x/5)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, lw=2, color='b', label='Sinyal Verisi')

#basit metin ekleme
ax.text(0.95,0.05,"Gizli Veri Notu",
        transform=ax.transAxes,
        fontsize=10,color="gray",
        ha="right", va="bottom",alpha=0.5)

#gelişmiş annonation

ax.annotate("yerel maksimum",
            xy=(1.3, 0.75),  # Okun işaret edeceği veri noktası
            xytext=(3,0.9),  # Metnin duracağı yer
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
            fontsize=12,
            fontweight='bold')

# 3. LaTeX ile Formül Ekleme
ax.set_title(r"Fonksiyon Analizi: $f(x) = \sin(x) \cdot e^{-x/5}$", fontsize=14)

# Estetik dokunuşlar
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylim(-1, 1.2)
ax.grid(axis='y', linestyle='--', alpha=0.3)

plt.show()