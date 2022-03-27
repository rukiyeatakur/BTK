#kendisine gönderilen kullanıcı adı ve şisfreyi kontrol ederek
#sonucunda True ya da False gönderen fonk python kodu
#kullanıcıadı:admin,şifre:123456 olmalı

def check(username,password):
    if username == 'admin' and password == '123456':
        kontrol = True
    else:
        kontrol = False
    return kontrol

kullanici_adi = input("Kullanıcı adı giriniz :")
parola = input("Parola adı giriniz :")
kontrol = check(kullanici_adi,parola)
if kontrol == True:
    print("Giriş başarılı")
else:
    print("Giriş yapılamadı")
