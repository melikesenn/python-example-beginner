sayilar = [1,2,3,4,5,6,7,8,9]
i = 0

while (i < len(sayilar)):
    i +=1
    print(i)
##################3333
sayi1 = int(input("1.sayiyi giriniz"))
sayi2= int(input("2.sayiyi giriniz"))


while(sayi1 <sayi2):
    print(sayi1)
    sayi1 = sayi1 +1
    if (sayi1 == sayi2):
        print(sayi2)
        break

print("işlem sonu")

##### RANGE KULLANIMI

for i in range(5,9,2):
    print("i{0}".format(i))



