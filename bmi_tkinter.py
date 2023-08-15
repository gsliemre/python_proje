
import tkinter as tk

def hesaplama():
    kilo = float(giriş2.get())
    boy = float(giriş3.get())
    if boy == 0 or kilo == 0:
        sonuc_eti.config(text="Kilo ve boy boş bırakılamaz")
    else:
        try:
            bmi = kilo / ((boy/100) ** 2)
            sonuc = netice_yazdır(bmi)
            sonuc_eti.config(text=sonuc)
        except:
            sonuc_eti.config(text="Sadece sayı giriniz")

def netice_yazdır(bmi):
    sonuc = f"BMI sonucunuz: {round(bmi, 2)}, "
    if 18.5 < bmi <= 25:
        sonuc += "normal kilolu"
    elif 25 < bmi <= 30:
        sonuc += "fazla kilolu"
    elif 30 < bmi <= 35:
        sonuc += "şişmanlık sınıfı 1"
    elif 35 < bmi <= 40:
        sonuc += "şişmanlık sınıfı 2"
    else:
        sonuc += "şişmanlık sınıfı 3"
    return sonuc

win = tk.Tk()
win.title("BMI Uygulaması: Yetişkin ve Çocuklar İçin")
win.config(padx=30, pady=30)

başlık2 = tk.Label(text="Kilonuzu giriniz")
başlık2.pack()
giriş2 = tk.Entry(width=30)
giriş2.pack()

başlık3 = tk.Label(text="Boyunuzu giriniz")
başlık3.pack()
giriş3 = tk.Entry(width=30)
giriş3.pack()

sonuc_eti = tk.Label()
sonuc_eti.pack()

hesap_butonu = tk.Button(text="BMI Hesapla", command=hesaplama)
hesap_butonu.pack()

win.mainloop()

