import threading
import requests
import time
# def a1(urls):
#     st=time.time()
#     json_dizi=[]
#     for i in urls:
#         json_dizi.append(requests.get(i).json())
#     et=time.time()
#     süre=et-st
#     print("işlem süresi",süre,"saniye sürdü")
#     return json_dizi
# urls=["https://postman-echo.com/delay/3"]*2
# a1(urls)

class ThreadingDownloader(threading.Thread):
    json_array = []
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url)
        self.json_array.append(response.json())
        return self.json_array

def get_data_threading(urls):
    st = time.time()
    threads = []
    for url in urls:
        t = ThreadingDownloader(url)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        print(t)
    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
urls = ['https://postman-echo.com/delay/3'] * 10