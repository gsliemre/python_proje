import tkinter
from turtle import clear

import pyowm
from tkinter import *
root = Tk()
#penceeyi yapalım

root.title("Hava NASIL")
root.configure(background = "#a1dbcd")
root.geometry("500x480")
#pencerde olacak başlıkları yazalım.Tüm değişiklikleri yapabilirsiniz renk gibi.

label = Label(root, text = "Weather Script", fg = '#a1dbcd', bg = '#383a39')     #Bu başlık etiketi
label1 = Label(root, text = "Şehri girin :", fg = 'black', bg = '#a1dbcd')
label2 = Label(root, text = "Sıcaklık :", fg = 'black', bg = '#a1dbcd')
label3 = Label(root, text = "Nem :",fg = 'black', bg = '#a1dbcd')
label4 = Label(root, text = "Description  :",  fg = 'black', bg = '#a1dbcd')
#veri alınacak kutuları yapalım
şehir = Entry(root)
sıcaklık = Entry(root)
nem= Entry(root)
desc_f = Entry(root)

# butonları ekleyelim

b1 = tkinter.Button(root, text = "Hava nasıl!", bg = '#383a39',fg = '#a1dbcd', command = omw)# hatayı çözemedim
b2 = Button(root, text = "Clear", bg = '#383a39', fg = '#a1dbcd', command = clear)

# wigetların koordinatlarını ayalıyalım

label.grid(row = 0, column = 2)
label1.grid(row = 2, column = 2)
label2.grid(row = 5, column = 2)
label3.grid(row = 7, column = 2)
label4.grid(row = 9, column = 2)

şehir.grid(row = 3, column = 2, ipadx ="180")
sıcaklık.grid(row = 6, column = 2, ipadx ="180")
nem.grid(row = 8, column = 2, ipadx ="180")
desc_f.grid(row = 10, column = 2, ipadx ="180")

b1.grid(row = 4, column = 2)
b2.grid(row = 11, column = 2)

#Tkinter penceremizin tasarımı bu noktada yapalım
#Şimdi OpenWeatherMap API'sinden hava durumu verilerini çıkarma mantığını yazmamız gerekiyor.

def omw() :
    api_key = "9ec33f7de30acef4fbb71a4fe26a0096  "    #kendi api keyinizi girin
    owm_obj=pyowm.OWM(api_key)
# get komuuyla şehirleri alalım
    şehir_ismi = şehir.get()
    obs_obj = owm_obj.weather_at_place(şehir_ismi)

# Tüm güncel hava durumu bilgilerini almak için hava durumu nesnesini oluşturalım
    weather = obs_obj.get_weather()
    temp = weather.get_temperature('celsius')["temp"]
    humidity = weather.get_humidity()
    description = weather.get_detailed_status()

    #Elde ettiğimiz değerleri ilgili metin alanlarına eklememiz gerekiyor.

    sıcaklık.insert(15, str(temp) + " Celcius ")
    nem.insert(15, str(humidity) + " %")
    desc_f.insert(10, str(description))

# Her çalıştırmadan sonra metin kutularını temizlemek için temizleme işlevini yazmamız gerekli
#  Aksi halde çıktı önceki çıktıya eklenmiş olarak gelir.

def clear() :
    şehir.delete(0, END)
    sıcaklık.delete(0, END)
    nem.delete(0, END)
    desc_f.delete(0, END)
    
root.mainloop()
