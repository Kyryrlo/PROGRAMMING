

# text = input("Введите текст: ") # text -> ["t","e","x","t"]
# text_list = list(text)
# k = len(text_list)
# if text.isdigit():
#     for t in range(k):
#         num = int(text_list[t])
#         text_list.pop(t)
#         text_list.insert(t,num)
    
#         summa = 0
#     for e in text_list:
#         summa +=e
#     print("Summa: ", summa)
# print(text_list)
# e = input("Element: ") # str
# try:
#     if e.isalpha():
#         indeks = text_list.index(e)
#     else:
#         indeks = text_list.index(int(e))
#     print("Element: {0} on {1} positsionil".format(e,indeks + 1))
# except: 
#     print("Element puudub")



# # # Практическая самостоятельная работа «Списки». 

#1
# vokaali = ["a", "e", "u", "y", "i", "o",]
# v = 0
# k = 0
# while True:
#     tekst = input("Sisesta sona voi lause: ") #.lower
#     if tekst.isdiget():
#         break
#     else:
#         tekst_l = list(tekst)
#         for e in tekst_l:
#             if e.lower() in vokaali:
#                 v += 1
#             else:
#                 k += 1
#     print("Vokaali:", v)
#     print("Konsosnti:", k)


l=[11,1,1,1,1,1,1,2,3,4,1,2,33]
l_set = set(l)
print(l_set)
