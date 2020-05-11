import random

sayi = random.randint(0,100)
hak = 5
print(sayi)

while hak>0:
    hak -= 1
    tahmin = int(input("sayiyi tahmin ediniz"))

    if (sayi == tahmin):
        print("tebrikler doğru bildiniz")

    elif(sayi > tahmin):
        print("yukarı")

    elif(sayi<tahmin):
        print("aşağı")
    else:
        print("bir daha deneyin")
        print(hak)

    if (hak == 0):
        print("üzgünüm hakkınız bitti")
        break


