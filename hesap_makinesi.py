
sayı1 = int(input("Bir sayı girin: "))
sayı2 = int(input("Bir sayı girin: "))

print("Toplama işlemi için '1'")
print("Çıkarma işlemi için '2'")
print("Çarpma işlemi için '3'")
print("Bölme işlemi için '4'")
seçim = int(input("Hangi işlemi yapmak istiyorsunuz? "))
try:
    
        if seçim == 1:
                
          print("sonuç :",sayı1+sayı2)
        

    
        if seçim == 2:
            print("sonuc:",sayı2-sayı1)

   
        if seçim == 3:
            
            print("sonuç:",sayı1*sayı2)

   
        if seçim == 4:
            
            print("sonuç:",sayı2/sayı1)
except:
        print ("Geçerli bir seçim yapınız.")


