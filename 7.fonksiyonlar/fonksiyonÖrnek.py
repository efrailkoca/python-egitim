'''
def selamlama(isim):
    print("sayın",isim,"restorana hoşgeldiniz")
while True:
    ad=input("isminiz nedir?:")
    if ad=="dur":
        break
    selamlama(ad)
'''
# varsayılan değer;
def selamlama(isim="furkan"):
    print("sayın",isim,"restorana hoşgeldiniz")
