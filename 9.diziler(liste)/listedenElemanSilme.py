kelime="btk akademi"
l=[]
l=list(kelime)
print(l)
l.remove(" ")
print(l)
l.remove("a")   # aynı olan elemanları tekte silmez.
print(l)
l.pop(2)        # belirli indisdeki elemanı silmek için.
print(l)
l.clear()       # listedeki tüm elemanları silmek için.
print(l)
