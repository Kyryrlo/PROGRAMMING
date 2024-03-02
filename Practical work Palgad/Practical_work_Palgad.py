from Funktsioonid import *

#1 ------------------------------------------------------------------------------------------------------------------

palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A","B","C","D","E"] 

# while True:
#     print("Lisamine? Да - 1: ")
#     v = int(input())
#     if v == 1:
#         k = int(input("Сколько имен хотите добавить?: "))
#         inimesed, palgad = Lisamine(inimesed, palgad, k)
#         for i in range(len(palgad)):
#             print(inimesed[i], "saab katte", palgad[i])
#     else:
#         break
            
#2 ------------------------------------------------------------------------------------------------------------------

# for i in range(len(palgad)):
#     print(inimesed[i], "saab katte", palgad[i])
# while True:
#     print("Хотите удалить кого-то? Да - 1: ")
#     v = int(input())
#     if v == 1:
#         k = int(input("Данные о скольких людях хотите удалить?: "))
#         who = input("Кого хотите удалить, напишите его имя: ")
#         Kustuta(who, inimesed, palgad)
#         for i in range(len(palgad)):
#             print(inimesed[i], "saab katte", palgad[i])
#     else:
#         break

#3 ------------------------------------------------------------------------------------------------------------------

while True:
    wan = int(input("Хотите найти самые большие зарплаты? 1-Да: "))
    if wan == 1:
        break

if palgad and inimesed:
    p, i = Biggest_sallary(palgad, inimesed)
    print(f"Самая большая зарплата у {i} и составляет {p} евро соответственно.")
else:
    print("Список зарплат или имен пуст. Невозможно найти максимальные значения.")
