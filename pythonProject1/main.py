import requests
import json
#get istekleri
# user_input=input("enter id :")
#
# get_url = f"https://jsonplaceholder.typicode.com/todos/{user_input}"
#
# get_responce=requests.get(get_url)
# print((get_responce.json()))

#post
to_do_items={"userId": 15, "title": "hey ne yapıyorsunuz bakauyıö", "completed": False}
post_url="https://jsonplaceholder.typicode.com/todos"
headers={"Content-Type": "aplications/json"}
post_responce=requests.post(post_url,data=json.dumps(to_do_items),headers=headers)
print((post_responce.json()))
