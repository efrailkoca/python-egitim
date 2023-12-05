'''
a=""
s=0
for x in "btkakademi":
    if s==7:
        a=x
    s+=1
print(a)
'''

a=""
s=0
indis=int(input("hangi indisi istiyorsunuz:"))
for x in "btkakademi":
    if s==indis:
        a=x
    s+=1
print(a)
