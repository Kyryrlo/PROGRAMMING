
# def Lisamine(i: list, p: list, k: int):
#     """Andmete lisamine listidesse
#     Tagastab listud
#     :parametr list i: Inimesta nimekiri
#     :parametr list p: Palkage loetelu
#     :parametr int k: Inimeste kogus
#     :rtype: list, list
#     """
#     for x in range(k):
#         nimi = input("Введите имя: ")
#         palk = int(input("Введите зарплату: "))
#         i.append(nimi)
#         p.append(palk)
#     return i, p

# #------------------------------------------------------------------------------------------------------------------

# def Kustuta(who, i, p):
#     """
#     """
#     if who in i:
#         who_ind = i.index(who)
#         i.pop(who_ind)
#         p.pop(who_ind)
# #------------------------------------------------------------------------------------------------------------------

# def SuuriPalk(i:list, p: list):
#     """
#     """
#     nimi_list = []
#     max_ = max(p)
#     a = 0
#     for palk in p:
#         if palk == max_:
#             ind = p.index(max_)
#             nimi = i[ind]
#             a += 1
#             nimi_list.append(nimi)
#     return max_, nimi_list
    
# #------------------------------------------------------------------------------------------------------------------

# def SuuriPalk(i:list, p: list):
#     """
#     """
#     nimi_list = []
#     min_ = max(p)
#     a = 0
#     for palk in p:
#         if palk == min_:
#             ind = p.index(min_)
#             nimi = i[ind]
#             a += 1
#             nimi_list.append(nimi)
#     return min_, nimi_list
# #------------------------------------------------------------------------------------------------------------------

# def Sort(i: list, p: list, a: int):
#     """
#     """
#     N = len(i)
#     if a == 1:
#         for n in range(0, N):
#             for m in range(n, N):
#                 if p[n] < p[m]:
#                     kaust = p[n]
#                     p[n] = p[m]
#                     p[m] = kaust
                    
#                     kaust = i[n]
#                     i[n] = i[m]
#                     i[m] = kaust
#     else:
#         for n in range(0, N):
#             for m in range(n, N):
#                 if p[n] > p[m]:
#                     kaust = p[n]
#                     p[n] = p[m]
#                     p[m] = kaust
                    
#                     kaust = i[n]
#                     i[n] = i[m]
#                     i[m] = kaust
#     return i, p
# #------------------------------------------------------------------------------------------------------------------

# def Kustutamine(i: list, p: list):
#     """
#     """
#     nimi = input("Nimi?: ")
#     n = i.count(nimi)
#     if n > 0:
#         for x in range i:
#             if x == nimi:
#                 ind = i.index(x)
#                 i.remove(x)
#                 p.pop(ind)
#     else:
#         pass
#     return i, p