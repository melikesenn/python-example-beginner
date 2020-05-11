def kackez(kelime ="kelime yok"):
    kac = int(input("kaç kez yazılacak"))
    i = 0
    while(i<kac):
        print(f' ', i ,' ',kelime,'.')
        i += 1

ss = kackez("aa")


def sinirsiz(*args):
    print(args)

xx = sinirsiz(1,2,3,4)
print(type(xx))
print(xx)