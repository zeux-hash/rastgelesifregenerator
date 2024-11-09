import random

degiskenler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


uzunluk = int(input("Parola Uzunluğunu Gir : "))
sifre = ""
for i in range(uzunluk):
    sifre += random.choice(degiskenler)

print("Parolanız :",sifre)

