# 10 soruluk test 1-10 arasında olan sayıları kullanıcaz ve iki sayının çarpımını sorucaz
# doğru sayısı > 8 -> pekiyi | > 6 -> iyi | > 4 -> orta | <= 4 -> zayıf
import random
dogru=0
for i in range(10):
    sayi1=random.randint(1,10)
    sayi2=random.randint(1,10)
    d_cevap=sayi1*sayi2
    print("soru",i+1,":",sayi1,"*",sayi2)
    cevap=int(input("cevabın:"))
    if cevap==d_cevap:
        print("cevap doğru")
        dogru+=1
    else:
        print("yanlış cevap!")
        print("asıl cevap :",d_cevap)
if dogru>8:
    print("pek iyi")
elif dogru>6 and dogru<=8:
    print("iyi")
elif dogru>4 and dogru<=6:
    print("orta")
else:
    print("zayıf")
