# medyan(ortanca):veriler sıraya koyulduktan sonra tam ortada kalan sayı ya da tam ortada kalan iki sayının ortalaması;
l=[]
for i in range(6):
    sayi=int(input("sayıyı gir:"))
    l.append(sayi)
l.sort()
eleman_sayisi=len(l)
if eleman_sayisi%2!=0:
    print("medyan=",l[int(eleman_sayisi/2)])
else:
    print("medyan=",(l[int(eleman_sayisi/2)]+l[int(eleman_sayisi/2-1)])/2)
