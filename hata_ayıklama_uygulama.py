#kullanıcıdan sayı isteyen
#sayı girmediğinde tekrar tekrar sayı girmesini isteyen,
#sayı girdiğinde de ekrana sayının karesinin yazdıran program

while True:
   try:
     sayi = int(input("bir sayı giriniz"))

   except ValueError:
         print("sadece sayılaru kabul etmekteyim")
   print("karesi:", sayi * sayi)
 