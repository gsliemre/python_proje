import requests
get_url="https://jsonplaceholder.typicode.com/todos/85"
responce=requests.get(get_url)
print(responce.json())
#put:tüm genelini değiştirme
# to_to_items85={"userId":25,"title":"kfejfeklş","completed":False}
# put_responce=requests.put(get_url,json=to_to_items85)
# print(put_responce.json())
# #patch: kısmi değiştirme yapılır
to_do_patch85={"title":"lmfşldwöfşdfşdlmfö"}
patc_responce=requests.patch(get_url,json=to_do_patch85)
print(patc_responce.json())
