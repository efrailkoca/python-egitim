import random
liste=["taş","kağıt","makas"]
print("oyundan çıkmak için 0'a bas")
while True:
    pc=random.choice(liste)     # bilgisayarın seçimi
    player=input("taş, kağıt, makas / seç birini:").capitalize()  # player seçimi. capitalize() amaç -> büyük küçük girilmesi önemli değil.
    if player=="0":
        break
    else:
        print("pc:",pc)
        print("player:",player)
        if (pc=="taş" and player=="kağıt") or (pc=="kağıt" and player=="makas") or (pc=="makas" and player=="taş"):
            print("kazandınız")
        elif (pc=="taş" and player=="makas") or (pc=="kağıt" and player=="taş") or (pc=="makas" and player=="kağıt"):
            print("kaybettin")
        else:
            print("berabere")
