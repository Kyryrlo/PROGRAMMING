from Funktsioonid import *

#1 ------------------------------------------------------------------------------------------------------------------

palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A","B","C","D","E"] 

# while True:
#     print("Lisamine? �� - 1: ")
#     v = int(input())
#     if v == 1:
#         k = int(input("������� ���� ������ ��������?: "))
#         inimesed, palgad = Lisamine(inimesed, palgad, k)
#         for i in range(len(palgad)):
#             print(inimesed[i], "saab katte", palgad[i])
#     else:
#         break
            
#2 ------------------------------------------------------------------------------------------------------------------

# for i in range(len(palgad)):
#     print(inimesed[i], "saab katte", palgad[i])
# while True:
#     print("������ ������� ����-��? �� - 1: ")
#     v = int(input())
#     if v == 1:
#         k = int(input("������ � �������� ����� ������ �������?: "))
#         who = input("���� ������ �������, �������� ��� ���: ")
#         Kustuta(who, inimesed, palgad)
#         for i in range(len(palgad)):
#             print(inimesed[i], "saab katte", palgad[i])
#     else:
#         break

#3 ------------------------------------------------------------------------------------------------------------------

while True:
    wan = int(input("������ ����� ����� ������� ��������? 1-��: "))
    if wan == 1:
        break

if palgad and inimesed:
    p, i = Biggest_sallary(palgad, inimesed)
    print(f"����� ������� �������� � {i} � ���������� {p} ���� ��������������.")
else:
    print("������ ������� ��� ���� ����. ���������� ����� ������������ ��������.")
