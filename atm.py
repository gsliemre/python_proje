# ATM Uygulaması

# Değişkenler
bakiye = 1000

# Menü
while True:
    print("******************\nATM sistemine hoşgeldiniz\n******************")
    print("""
    İşlemler:
    1. Bakiye Sorgulama
    2. Para Yatırma
    3. Para Çekme
    Programdan 'q' tuşu ile çıkabilirsiniz.
    """)
    işlem = input("İşlemi giriniz: ")

    # İşlemleri kontrol et
    if işlem == "q":
        break
    elif işlem == "1":
        print("Bakiyeniz {} TL'dir.".format(bakiye))
    elif işlem == "2":
        miktar = int(input("Yatırmak istediğiniz tutar: "))
        bakiye += miktar
        print("Bakiyeniz {} TL'ye yükseldi.".format(bakiye))
    elif işlem == "3":
        miktar = int(input("Çekmek istediğiniz tutar: "))
        if bakiye < miktar:
            print("Yetersiz bakiye.")
        else:
            bakiye -= miktar
            print("{} TL çekildi. Yeni bakiyeniz {} TL.".format(miktar, bakiye))
    else:
        print("Geçersiz işlem.")

