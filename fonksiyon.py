def selam(name='user'):
    return 'hello' + name

yeni1 = selam()
yeni = selam('melike')

print(yeni,yeni1)


##############sınırsız eleman almak istersek fonksiyona

def sinirsiz(*params): #tek * (args)da liste olur çift ** da dictionary olur (**kwargs)
    return sum((params))

aa = sinirsiz(1,2,3,4)
print(aa)

def user(**args):
    for key,value in args.items():
        print('{} is {}'.format(key,value))

user(name="meli",age = 22, city = "ist")