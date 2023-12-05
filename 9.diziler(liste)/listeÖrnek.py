# kullanıcı tarafından girilen 5 adet sayıyı a listesine aktarıp, yazdırmak;
a=[]
for i in range(5):
    sayi=int(input("sayıyı girin:"))
    a.append(sayi)
for i in range(5):
    print(a[i])
