k={1,"hg","*",325}      # küme oluşturma
kume=set("abcd1234")    # küme oluşturma
print(k)
print(kume)
print(type(k))
print(type(kume))
k1={1,2,3,4,5}
k2={1,3,6,7,8}
print(k1|k2)            # bileşim kümesi
print(k1&k2)            # kesişim kümesi
print(k1-k2)            # fark kümesi
print(k2-k1)            # yani, k2'de olup k1'de olmayan elemanlar
