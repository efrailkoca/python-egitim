# range(0,5) => 0'dan 5'e kadar yazdırır.
# range(6) => 0'dan 6'ya kadar yazdırır.
# range(11,5) => 11'den 5'e kadar yazdırır.
# range(1,10,2) => 1'den 10'a kadar 2'şer artırarak yazdırır.
# range(15,3,-4) => 15'ten 3'e kadar 4'er azaltarak yazdırır.

# kullanımı;
for a in range(0,5):
    print(a,)
print()

# uzun yolu;
for f in [0,1,2,3,4]:
    print(f)
print()

for b in range(6):
    print(b)
print()

for c in range(11,5):
    print(c)
print()

for d in range(1,10,2):
    print(d)
print()

for e in range(15,3,-4): # değer koşul değerine eşit olduğunda döngünün dışına çıkar.
    print(e)
print()

print(list(range(0,5))) # range aralığını yazdırmak.
