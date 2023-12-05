# her gelen hastanın tc'sini alıp kuyruğa ekliycez;
# eğer listede tc varsa muayene sırasını öğrenecek,
# eğer yoksa sıranın sonuna geçecek
# eğer tc'ye 0 girilirse sıra hemen o hastanın olsun
l=[]
while True:
    TC=int(input("dört haneli TC girin:"))
    if TC in l:
        i=l.index(TC)
        print("muayebe sırası:",i+1)
    elif TC==0:
        print(l[0],"TC numaralı hasta içeri giriniz.")
        l.pop(0)
    else:
        l.append(TC)
        print(TC,"TC numaralı hasta sıraya alındı.")
        
