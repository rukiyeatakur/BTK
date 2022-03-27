#dikdörtgenin alanını ve çevresini hesaplayan 2 ayrı
#fonk.yazınız.Kullanıcıdan aldığınız değere göre
#alanı ve çevreyi ekrana yazdırınız.
def cevre(kısa,uzun):
    return(kısa+uzun)*2

def cevre(kısa, uzun):
    return (kısa * uzun)

kısakenar=int(input("kısa kenarı giriniz:"))
uzunkenar=int(input("uzun kenarı giriniz:"))
print("dikdörtgenin çevresi:",cevre(kısakenar,uzunkenar))
print("dikdörtgenin alanı:",alan(kısakenar,uzunkenar))
