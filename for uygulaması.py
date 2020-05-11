liste = [1,2,3,4,5,6,7,8,9]
for i in liste:
    if(i%3==0):
        print(i)

    if(i%2==1):
        print(i**2)
print("toplam",sum(liste))

###############
print("yeni örnek")
country = ["aaa","bbb","ccc","ddd","eee","sadsdsdas","sdffdsvesrfe"]
for i in country:
    if (len(i) == 3):
        print(i)

###############3
print("3.örnek")
urun = [
    {'tel_ismi':'s6',"price":"450"},
    {'tel_ismi':'s7', "price":"500"}
]
toplam = 0
for i in urun:
    fiyat = int(i['price'])
    toplam += fiyat
    print(toplam)
###############while

i=0
while(i<100):
    i = i+1
    print(i)

