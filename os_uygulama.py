import os
try:

    os.mkdir("elma") #klasör oluşur
except FileExistsError:
    print("ayni isimde bir klasör var!!!")
