kelime=input("kelimeyi gir:")
t_kelime=kelime[::-1]
print(kelime,"kelimesinin tersi",t_kelime)
if kelime==t_kelime:
    print(kelime,"kelimesi, palindrom bir kelimedir.")
else:
    print("girdiğiniz kelime palindrom bir kelime değildir.")
