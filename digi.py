import time
while True:
    saat=time.strftime("%H:%M:%S"),time.localtime()
    print(saat,end="\r")
    time.sleep(1)