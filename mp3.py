
from pydub import AudioSegment

mp3_dosyasi = AudioSegment.from_mp3("Tarkan Geççek.mp3")
sure = len(mp3_dosyasi) / 1000  # saniye cinsinden dosya süresi

print("Dosya süresi:", sure, "saniye")

