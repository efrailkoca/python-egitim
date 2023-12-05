s={"bir":1,"iki":2,"üç":3,"dört":4}     # "bir" => anahtar(key), 1 => değer(value)
print(s.get("bir","yok"))      # "yok" => eğer anahtar kelimenin karşılığı yok ise yok mesajını göstericek.
print(s.get("beş","yok"))
print(s.pop("üç"))
print(s)
print(s.keys())
print(s.values())
print(s["iki"])
print(s.items())
