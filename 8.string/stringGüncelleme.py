s="python"
print(s[:])

print(s[3:])     # 3. indise kadar yazdırmamak anlamına gelir.
print(s[:3])     # 3. indis ve sonrasını yazdırmamak anlamına gelir.
print(s[1:5])    # 1->1. indise kadar yazdırma demek. 5->5. indisi yazdırma demek.
print(s[1::2])   # 1. indise kadar yazdırma, sonra 2 indis atlayarak yazdır demek.
print(s[1:6:3])  # 1. indisten başlayıp 6. indise kadar 3'er 3'er atlamak demek.
print(s[::-1])   # python'ın tersten yazılmış hali.

print()

s2=s[:3]+"t"+s[4:]
print(s2)

print()

# from python to piton;
s3=s[:1]+"i"+s[2::2]+s[5:]
print(s3)

print()

# adres güncelleme;
adres="sultangazi-istanbul"     # yeni adres kadıköy
adres2="kadıköy"+adres[10:]
print(adres2)
adres3=adres.replace("sultangazi","kadıköy")
print(adres3)
