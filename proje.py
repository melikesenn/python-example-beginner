liste = ["1","2","3","400","5a","5"]
for i in liste:

    try:
        print(int(i))
    except ValueError:
        continue

while True:
    print("çıkmak için q'ya basın")
    sayi = input("bir sayi giriniz")

    if (sayi == "q"):
        print("artık çıkıyorsun")
    try:
        sayii = int(sayi)

    except ValueError:

            break

