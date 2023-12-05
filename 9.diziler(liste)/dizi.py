'''
liste=["furkan","efrail",123456789,"baba"]
print(liste[2])
no=liste[2]
print(no)
print(liste[-1])
'''
# listedeki elemanın indis sayısını öğrenme;
liste=[1,2,3,"a","2","ali"]
print(liste.index(2))
print(liste.index("2"))

# liste dilimleme string bölmede olduğu gibi oluyor.
l=[1,2,3,4,5,6,7,8,9]
print(l[2:])    # 2. indis ve sonrasını yazdır.
print(l[:3])    # 3. indise kadar yazdır.(3. indis hariç)
print(l[::-1])  # diziyi ters çevirir.
print(l[::2])   # elemanları 2'şer atlayarak yazdırır.
print(l[::-2])  # elemanları 2'şer atlayarak tersten yazdırır.

