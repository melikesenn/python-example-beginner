"""
dosya açma ve oluşturma için open() fonksiyonu kullanılır
open(ddsyaadı,dosyaya erişme işleminde yapılacaklar )
a: dosya konumda yoksa ekler
w: dosyayı konuma yazap
x: oluşturur varsa hata verir
r: okuma yoksa hata verir
"""

# dosya açma  okuma ve yazma

sonuc = open("yeni.txt", "w", encoding="utf-8") #dosya açar
sonuc.write("melii") # dosyaya yazar
print(sonuc)

#print(sonuc.read()) dosya okur
sonuc.close()


