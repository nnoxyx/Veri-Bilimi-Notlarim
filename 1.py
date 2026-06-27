import numpy as np
import matplotlib.pyplot as plt

# 1. Matrisi oluştur (Senin kodun)
resim = np.zeros((5, 5), dtype='uint8')

# Tam ortadaki pikseli beyaz (255) yapalım
resim[2, 2] = 255
# Komşularını gri (200) yapalım
resim[2, 1] = 200
resim[1, 2] = 200
resim[2, 3] = 200
resim[3, 2] = 200

# Kodunun çıktısını kontrol et (İsteğe bağlı)
# print(resim)

# 2. Görselleştirme Kısmı
# plt.imshow() fonksiyonu diziyi resim olarak yorumlar.
# cmap='gray' parametresi, tek kanallı bu diziyi siyah-beyaz olarak gösterir.
# 0 = Siyah, 255 = Beyaz, aradakiler Gri tonlarıdır.
plt.imshow(resim, cmap='gray', vmin=0, vmax=255)

# Ek özellikleri ekleyelim (Daha anlaşılır olması için)
plt.title("5x5 Matrisin Görsel Hali")
plt.colorbar() # Hangi rengin hangi değere denk geldiğini gösteren bar
plt.axis('on')  # Eksenleri ve piksel numaralarını göster

# Resmi ekranda göster
plt.show()