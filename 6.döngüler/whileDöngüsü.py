# sıfırdan farklı olduğu sürece girilen sayıların karesini alan program
sayi=1
print("döngüden çıkmak için 0'bas, devam etmek için herhangi bir rakama bas")
while (sayi!=0):
    sayi=int(input("sayı:"))
    print(sayi**2)
    sayi=int(input("devam mı tamam mı?"))
