
alfabe = "abcdefghijklmnopqrstuvwxyz"
anahtar = 5

mesaj = input("Şifrelenecek mesajı girin: ")
sifreli_mesaj = ""

for harf in mesaj:
    if harf in alfabe:
        index = (alfabe.index(harf) + anahtar) % len(alfabe)
        sifreli_mesaj += alfabe[index]
    else:
        sifreli_mesaj += harf

print("Şifreli mesajınız:", sifreli_mesaj)

