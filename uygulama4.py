#

puan=int(input("dönem sonu puanınızı giriniz"))

if puan>=85:
    print("tebrikler takdir aldınız")
elif puan>70 and puan<84:
    print("tebrikler teşekkür aldınız")
else:
    print("belge alamadınız")
