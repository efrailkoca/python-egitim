'''
# stack;
l=[]
l.append(4)
l.append(29)
l.append(7)
l.append(658)
print(l)
l.pop()
print(l)
l.pop()
print(l)

print()

# queue;
a=[]
a.append(4)
a.append(29)
a.append(7)
a.append(214)
print(a)
l.pop(0)
print(a)
'''
l=[]
while True:
    isim=input("isim giriniz:")
    l.append(isim)
    if isim=="sıradaki":
        print(l.pop(0))
    if isim=="bitti":
        break
