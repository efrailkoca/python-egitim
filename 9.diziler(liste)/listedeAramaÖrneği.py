'''
l=[1,2,3,4,5,6,7,8]
print(1 in l)
print(1 not in l)
print(9 in l)
print(10 not in l)
'''
# belirli bir liste içerisinde kullanıcıdan alınan değer var mı yok mu karşılaştırma programı;
l=[12,23,45,56,78,89]
sayi=int(input("sayıyı girin:"))
if sayi in l:
    indis=l.index(sayi)
    print("sayı şu indiste ->",indis)
else:
    print("aranan sayı bulunamadı.")
