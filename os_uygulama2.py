import os
while True:
   print("1-klasör oluştur")
   print("2-klasör sil")
   secim=input("seçiminiz:")
   if secim=="1":
       ad=input("klasör adı giriniz:")
       for i in range(1, 11):
            os.mkdir(ad + str(i))
   elif secim=="2":
        ad=input("silinecek klasör adı giriniz")
        for i in range(1, 11):
            os.rmdir()(ad + str(i))

