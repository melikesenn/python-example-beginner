not1 = int(input("1. notunuzu giriniz"))
not2 = int(input("2. notunuzu giriniz"))
sözlü = int(input("sözlü notunuzu giriniz"))

ortalama = not1*0.3+not2*0.5+sözlü*0.2

if(ortalama>45 and ortalama <54):
    print("DD")
elif(ortalama>55 and ortalama <70):
    print("CC")
elif (ortalama >= 70 and ortalama < 85):
    print("bb")
elif (ortalama >= 85 and ortalama < 100):
    print("CC")
else:
    print("kaldınız")


