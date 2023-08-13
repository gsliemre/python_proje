

   
import datetime

# Şu anki zamanı alma
suanki_zaman = datetime.datetime.now()

# Tarih ve saat bilgilerini ayrı ayrı almak
def zaman():

    yil = suanki_zaman.year
    ay = suanki_zaman.month
    gun = suanki_zaman.day
    saat = suanki_zaman.hour
    dakika = suanki_zaman.minute
    saniye = suanki_zaman.second

# Formatlı olarak zamanı yazdırma
    print(f"Şu anki zaman: {gun}/{ay}/{yil} {saat}:{dakika}:{saniye}")
zaman()

