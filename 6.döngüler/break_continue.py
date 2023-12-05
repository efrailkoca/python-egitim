# break;
print("döngüden çıkmak için 0 girin.")
while True:
    sayi=int(input("sayıyı girin:"))
    print("karesi:",sayi**2)
    if sayi==0:
        break # döngüden çık komutu

# continue;
# yedi ve katları hariç 0'dan 100'e kadar sayıları yazdıran program
sayi=1
while (sayi!=100):
    if sayi%7==0:
        sayi+=1
        continue
    print(sayi)
    sayi+=1
print()

# for döngüsü ile;
for x in range(100):
    if x%7==0:
        continue
    print(x)
