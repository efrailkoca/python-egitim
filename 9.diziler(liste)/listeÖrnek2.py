# kullanıcıdan alınan değerlerin max-min 'ini bulup toplıycaz ve tüm değerlerin aritmetik ortalamasını bulucaz;
l=[]
for i in range(5):
    sayi=int(input("sayıyı girin:"))
    l.append(sayi)
print("max ve min değerlerin toplamı=",max(l)+min(l))
toplam=0
for i in range(5):
    toplam=toplam+l[i]
print("ortalama=",toplam/len(l))
