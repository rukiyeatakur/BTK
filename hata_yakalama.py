try:
    sayi=int(input("bir sayı giriniz"))
    sayi2=int(input("bir sayı griniz"))
    print("bölüm:",sayi/sayi2)
except ValueError:
    print("lütfen sayı gir harf girme!")
except ZeroDivisionError:
    print("0'a bölme yapılamaz")
except SyntaxError:
    print("yazım hatan var")
except NameError:
    print("böyle bir değişken yok")
except:
    print("genel hata oluştu")
print("program buradan çalışmasına devam eder")

