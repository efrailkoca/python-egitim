l1=[1,2,3,4]
l2=[5,6,7,8]
l3=l1+l2
print(l3)
print(l1+l2)
l1.extend(l2)   # l2 listesini l1 listesine ekler.
print(l1)
l2.extend(l1)   # yeni l1'i l2'ye ekledik.
print(l2)
