elveda = lambda : print("görüşmek üzere")

'''
def dolar(TL):
    return(TL/18)

dolar=lambda TL: TL/18 dolar:fonksiyonun adı | TL:fonksiyonun parametresi | TL/18:fonksiyonun işlemi
'''

# yukarıdaki ikisi de aynı şey

# uzun yol;
'''
def dolar(TL):
    return(TL/18)
print(dolar(1000))
'''

# kısa yol;
'''
dolar=lambda TL: TL/18
print(dolar(1000))
'''

#def dolar(TL):
#    return(TL/18)

dolar=lambda TL: TL/18

TL=int(input("TL gir:"))
print(TL,"Türk Lirası=",dolar(TL),"Dolar")
