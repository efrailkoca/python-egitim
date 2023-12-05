'''
liste=["ali","can","miray","zeynep"]
print(liste)
print("ali"in liste)
liste2=[1,2,3,4,5]
print(liste2)
liste3="python"
print(liste3)
'''
# restoran örneği;
masaNo=0
liste=["ali","can","miray","zeynep"]
liste2=["efrail","furkan"]
isim=input("isminiz nedir?")
if isim=="ali":
    masaNo=5
if isim=="can":
    masaNo=7
if isim=="miray":
    masaNo=2
if isim=="zeynep":
    masaNo=10
if isim in liste:
    print("rezervasyonunuz var.\nmasa numaranız:",masaNo)
elif isim in liste2:
    print("rezervasyonunuz bugün değil.")
elif isim not in liste and isim not in liste2:
    print("rezervasyonunuz yok.")
