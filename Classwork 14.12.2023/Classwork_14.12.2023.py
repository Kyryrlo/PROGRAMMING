from ast import Num
from random import *
# Практическая самостоятельная работа «Списки». 

# # 4
# while True:
#     try:
#         index = int(input("Введите индекс: "))
#         if len(str(index)) == 5:
#             break
#     except ValueError:
#         print("Ошибка")

# print("Производим анализ...")

# indexid = ["Таллинн", "Нарва, Нарва-Йыэсуу", "Кохтла-Ярве", "Ида-Вирумаа, Ляэне-Вирумаа, Йыгевамаа", "город Тарту", "Тартуммаа, Пылвамаа, Выруммаа, Валгаммаа", "Вильяндимаа, Ярвамаа, Харьюмаа, Рапламаа", "Пярнумаа", "Ляэнемаа, Хийумаа, Сааремаа"]

# index_list = list(str(index))
# s1_indexlist = index_list[0]

# # И более изящное решение
# print("Index {0} on {1} piirkonnas".format(index,indexid[int(s1_indexlist)-1]))
  
# if int(s1_indexlist) == 1:
#     print("Ваш округ - Таллинн")
# elif int(s1_indexlist) == 2:
#     print("Нарва, Нарва-Йыэсуу")
# elif int(s1_indexlist) == 3:
#     print("Кохтла-Ярве")
# elif int(s1_indexlist) == 4:
#     print("Ида-Вирумаа, Ляэне-Вирумаа, Йыгевамаа")
# elif int(s1_indexlist) == 5:
#     print("город Тарту")
# elif int(s1_indexlist) == 6:
#     print("Тартуммаа, Пылвамаа, Выруммаа, Валгаммаа")
# elif int(s1_indexlist) == 7:
#     print("Вильяндимаа, Ярвамаа, Харьюмаа, Рапламаа")
# elif int(s1_indexlist) == 8:
#     print("Пярнумаа")
# elif int(s1_indexlist) == 8:
#     print("Ляэнемаа, Хийумаа, Сааремаа")



# #5
# kokku = randint(2,20)
# num_list = []
# for i in range(kokku):
#     num_list.append(randint(-100,100))

# print(num_list)
# print()

# while True:
#     try:
#         kogus = int(input("Введите cколько пар поменять местами: "))
#         if kogus <= kokku/2:
#             break
#     except ValueError:
#         print("Неправильное значение")
        

# for i in range(0, kogus, 1):
#     X_tmp = num_list[i]
#     print(str(i), " ", str(num_list[i])," ", str(num_list[(len(num_list)-i)-1]), "\n")
#     print(X_tmp, "\n")
    
#     num_list[i] = num_list[(len(num_list)-i)-1]
#     num_list[(len(num_list)-i)-1] = X_tmp
# print("\n",num_list)



# # 6
# kokku = randint(2,20)
# print("kokku jarjedis on: ", kokku, "elementi")

# num_list = []
# for i in range(kokku):
#     num_list.append(round(random()*1000, 2))
# print(num_list)

# max_ = max(num_list)
# n = num_list.index(max_)

# print("\t", max_, "pisitsioonil", n + 1)

# num_list.pop(n)
# max_ = max_ / len(num_list)
# num_list.insert(n, max_)

# print(num_list)


# # 7
# numeric = randint(2, 20)
# numeric_list = []
# for i in range(numeric):
#     numeric_list.append(randint(-1000, 1000))
# print(numeric_list)
# print()
# print("Len of numeric_list" + str(len(numeric_list)))
# for i in range(0,numeric,1):
#     numeric_list[i] = abs(numeric_list[i])  

# !!!!!!



# 7.1
kokku = randint(2,20)
num_list = []
for i in range(kokku):
    num_list.append(randint(-100,100))
print("\tOriginaal: ")
print(num_list)
for element in num_list:
    if element < 0:
        n = num_list.index(element)
        num_list[n] = abs(element)

print("\tAbsoluut Vartused: ")
print(num_list)
num_list.sort()
print("\tKasvav jarjend: ")
print(num_list)
num_list.reverse()
print("\tKahanev jarjend: ")
print(num_list)

# 8