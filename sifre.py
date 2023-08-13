
# import random
# import string

# def sifre_olustur(uzunluk):
#     harfler = string.ascii_letters + string.digits + string.punctuation
#     sifre = ''.join(random.choice(harfler) for i in range(uzunluk))
#     return sifre

# uzunluk = int(input("Şifre uzunluğunu girin: "))
# sifre = sifre_olustur(uzunluk)
# print("Oluşturulan şifre:", sifre)

import random
karakterler = "fsjhgkçufycbzghhgbj75463,0/-91"

def şifre(uzunluk):
    oluşturulan_şifre = ""
    
    for i in range(uzunluk):
        oluşturulan_şifre += random.choice(karakterler)
        
    return oluşturulan_şifre

uzunluk = int(input("Şifre uzunluğunu girin: "))
şifre_oluştur = şifre(uzunluk)
print("Oluşturulan şifre:", şifre_oluştur)

