ilk = 0
kelime = "melike"

for i in kelime:
    print(f'başlangıç' ,{ilk}, ' sayısı ' ,{i} ,'harfi')
    ilk +=1


#bunu enumerate ile index value olarak belirlersek ilk kelime yazmayız

kelime2 = "asdkkf"
for i,j in enumerate(kelime2):
    print(f'sayı',{i},'harf',{j})


###########zip
list1 = ["a","b","c"]
list2 = ["25","23","12"]
print(list(zip(list1,list2)))

sayi = [i for i in range(5)]
print(sayi)