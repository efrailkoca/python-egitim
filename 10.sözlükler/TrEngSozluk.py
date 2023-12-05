gun=(input("türkçe gün adı:"))
TrEng={"pazartesi":"monday","salı":"tuesday","çarşamba":"wednesday","perşembe":"thursday","cuma":"friday","cumartesi":"saturday","pazar":"sunday"}
if gun not in TrEng:
    print("bu kelime sölükte yok")
else:
    print(TrEng.get(gun))
