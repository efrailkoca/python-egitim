# adam asmaca oyunu
# belirli kelimeler olucak, biz harf tahmin ederek bu kelimeyi bulmaya çalışıcaz
# her yanlış harf bildiğimizde adamın bir uzvu çizilecek, adam tamamen çizildiğinde kaybedicez
import random
liste=["python","print","random","while","choice",]
kelime=random.choice(liste)
adam=['''
    +----+
    0    |
   /|\\  |
   / \\  |
        ___''','''
    +----+
    0    |
   /|\\  |
   /     |
        ___''','''
    +----+
    0    |
   /|\\  |
         |
        ___''','''
    +----+
    0    |
   /|    |
         |
        ___''','''
    +----+
    0    |
    |    |
         |
        ___''','''
    +----+
    0    |
         |
         |
        ___''','''
    +----+
         |
         |
         |
        ___''']
dogruHarf=[]
yanlısHarf=[]
hak=len(adam)

while hak>0:
    out=""
    for h in kelime:
        if h in dogruHarf:
            out+=h
        else:
            out+="_"
    if out==kelime:
        break
    print("kelime:",out)
    print(adam[hak-1])
    girHarf=input()
    if girHarf in dogruHarf or girHarf in yanlısHarf:
        print(girHarf,"zaten girildi")
    elif girHarf in kelime:
        print("doğru harf")
        dogruHarf.append(girHarf)
    else:
        print("yanlış harf")
        hak-=1
        yanlısHarf.append(girHarf)
if hak!=0:
    print("tebrikler. kelime:",kelime)
else:
    print("kaybettiniz. kelime:",kelime,"idi")
    
