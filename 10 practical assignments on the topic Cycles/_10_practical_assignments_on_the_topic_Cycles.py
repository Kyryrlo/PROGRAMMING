from math import*

from random import*

# # #10 Exercices

# #1
# t = 0
# for x in range(1,16):
#     A = float(input("Input number: "))
#     if A % 1 == 0:
#         t += 1

# print(t)

# # 2
# summa=0
# A=int(input("Input A: "))
# for x in range(1,A+1,1):
#     summa+=x
#     print("Summa: {0}".format(summa))


# # 3
# p = 1
# Lause = ""
# for x in range(8):
#     A = float(input("{0}. Шаг\nВведите число: ".format(x + 1)))
#     if A > 0:
#         p *= A
#         Lause += str(int(A)) + "*"

# print(Lause[:-1], "=", int(p))


#4
# x = 10
# for x in range(10,21):
#     summ = x * x
#     print(summ)

# # 5 
# while 0 == 0:
#     try:
#         start = int(input("С какого числа начнём складывать?: "))
#         break
#     except ValueError:
#         pass
# while 0 == 0:
#     try:
#         finish = int(input("До какого числа будем складывать?: "))
#         break
#     except ValueError:
#         pass

# start1 = start    
# summ = 0
# for start in range(start, finish + 1):
#     if start < 0:
#         summ += start

# print("Сумма всех отрицательных чисел от", str(start1), "до", str(finish), "равна:", str(summ))
    

#6
# Neg = ""
# Nuli = ""
# Poz = ""
# Q = int(input("Сколько чисел введёте?: "))
# if Q > 0:
#     for Q in range(1,Q + 1):
#         A = int(input("Введите число: "))
#         if A < 0:
#             Neg = Neg + str(A) + ","
#         elif A == 0:
#             Nuli = Nuli + str(A) + ","
#         elif A > 0:
#             Poz = Poz + str(A) + ","
#         else:
#             print("Это не число")
#     print("Отрицательных:",str(Neg[:-1])) 
#     print("Нулей:",str(Nuli[:-1])), 
#     print("Положительных:", str(Poz[:-1]))
# else:
#     print("Нельзя ввести количество чисел меньше нуля")




# #12
# n = randint(2,10)
# m = randint(1,10)
# summa = 0
# print("Chislo kosilok: ", n)
# print("Первая проработала: ", m, "часа")
# for t in range(n - 1):
#     m = (m/6) * 7
#     summa += m
# print("Kokku misinad tootasid", summa, "tn")


# #13
# Q = 0
# Summ = 0
# for x in range(100, 1001):
#     if x % 7 == 0:
#         Q +=1
#         Summ += x
# print("Количество чисел кратных 7: " + str(Q)) 
# print("Cумма чисел кратных 7: " + str(Summ))


# #14
# P = 1
# N = int(input("Введите число произведения от 1 до него хотите найти :"))
# for N in range(1, N+1):
#     P *= N
# print("Произведение от 1 до введёного вами числа =", P)


#15
for x in range(10):
    for y in range(10):
        print(y, end="")
    print()
    
for x in range(1, 10):
    for y in range(1, 10):
        if y == x:
            print(y, end="")
        else:
            print(0, end="")
    print()

# #29
# for i in range(9):
#     for x in range(9):
#         if x==0 or i==x:
#             print("x",end="")
#         else:
#             print("0",end="")
#     print() 
