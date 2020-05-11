def kare_al(x):
    return x**2
liste = [1,2,3,4,5]

sonuc = list(map(kare_al,liste))
print(sonuc)

###LAMBDA KULLANIMI

sonuc2 = list(map(lambda yeni: yeni **2,liste))
print(sonuc2)

