class Person:
    #pass içi boşsa sonra yazılacaksa pass kullam
    address= "bilgi yok"


    def __init__(self,name,year): #init fonksiyonu oluşturulan her fonksiyon için çalıştırılır
        self.name=name
        self.year=year
        print("çalıştım")
insan1 = Person('meli',1997)
print(f'isim',insan1.name,'yıl',insan1.year,'adresi',insan1.address)