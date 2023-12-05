import random
sayi=random.randint(1,6)
tahmin=int(input("tahminini gir:"))
skor=0
while True:
    if sayi==tahmin:
        print("kazandınız. skorunuz:",skor)
        break
    else:
        skor+=1
        print("olmadı. skor:",skor)
        tahmin=int(input("tahminini gir:"))
