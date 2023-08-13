
# anket_sorulari = ['En sevdiğiniz renk nedir?', 'Hangi sporu tercih edersiniz?', 'En sevdiğiniz yemek hangisidir?','gs nasıl']
# anket_cevaplari = []

# for soru in anket_sorulari:
#     cevap = input(soru + ": ")
#     anket_cevaplari.append(cevap)

# print("Anket sonucu:")
# for i in range(len(anket_sorulari)):
#     print(anket_sorulari[i] + ": " + anket_cevaplari[i])
my_list=["red","yellow","83","sk"]
new_list=[]
for i in my_list:
    answer=input(i +"")
    new_list.append(answer)
print("tercihler :")
for c in range(len(my_list)):
    print(my_list[c]+ ":"+new_list[c])
    
