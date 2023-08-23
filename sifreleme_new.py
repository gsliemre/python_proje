from tkinter import *
from tkinter import messagebox
import base64
# Fn to encrypt the message
def encode(key, clear):
                enc = []
                for i in range(len(clear)):
                    key_c = key[i % len(key)]
                    enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
                    enc.append(enc_c)
                return base64.urlsafe_b64encode("".join(enc))

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)



def kaydet_sifrele():
    title=baslık1_enter.get()
    mesaj=baslik2_enter.get("1.0",END)
    gizli_mesj=başlık3_enter.get()


    if len(baslık1_enter.get())== 0 or len(baslık2_enter.get("1.0",END)) == 0:
        messagebox.showerror(title="boş olmaz",message="lütfen ilgili alanLARI doldurunuz")
    else:
            şireleme=encode(başlık3,baslik2_enter)
            try:
       
                with open("Untitled-1.txt" ,"a") as file:
                  file.write(f"\n{baslık1_enter}\n{şireleme}")
            except FileNotFoundError:
                 with open("Untitled.txt" ,"w") as file:
                            file.write(f"\n{baslık1_enter}\n{şireleme}")
            finally:
                   baslık1_enter.delete(0,END)
                   baslik2_enter.delete("1.0",END)
                   başlık3_enter.delete(0,END)

           
            
                    








#ARAYÜZ
pencere=Tk()
pencere.config(padx=40,pady=40)
FONT="calibri",15,"normal"
pencere.title("gizli mesajlaşma")
baslık1=Label(text="bir başlık girin",font=FONT)
baslık1.pack()
baslık1_enter=Entry(width=15)
baslık1_enter.pack()
baslik2=Label(text="Mesajınızı girin",font=FONT)
baslik2.pack()
baslik2_enter=Text(width=30,height=10)
baslik2_enter.pack()
başlık3=Label(text="anahtar kelimeyi giriniz",font=FONT)
başlık3.pack()
başlık3_enter= Entry(width=35)
başlık3_enter.pack()
kayıdet_sifrele=Button(text="kaydet/şifrele",font=FONT,command=encode)
kayıdet_sifrele.pack()
sifre_cöz=Button(text="ŞİFREYİ ÇÖZ",font=FONT,command=decode)
sifre_cöz.pack()



pencere.mainloop()

