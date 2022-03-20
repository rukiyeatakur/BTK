import random
while True:
    seviye=input("bir seviye seçiniz: kolay/orta/zor/")

    if seviye=="kolay":
        uret=random.randint(1,10)
        break
    if seviye=="orta":
        uret=random.randint(1,50)
        break
    if seviye == "zor":
        uret = random.randint(1, 100)
        break
while True:
    tahmin=int(input("bir tahminde bulununuz:"))

    if tahmin<uret:
        print("sayınızı büyültün")
    elif tahmin>uret:
        print("sayınızı küçültün")
    else:
        print("tebrikler,bildiniz!")
        break