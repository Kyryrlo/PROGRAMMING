from math import *

#1 
print("Hello Kyrylo chernykh") 


# #2
# R = 3+8/(4 - 2)*4
# print(R)

# Re = 3+(8/(4 - 2))*4
# print(Re)
# # При тестировании не заметно никакой разницы


# #2.1
# R = float(input("Input radius: "))
# D = R * 2
# S_square = D * D
# P_square = D * 2
# S_circle = pi * R**2
# P_circle = 2 * pi * R
# print("Square square:",S_square)
# print("Square perimetr:", P_square)
# print("Circle square:",S_circle)
# print("Circle perimetr:", P_circle)


# #2.2
# R_Earth = 6378
# P_Earth = 2 * pi * R_Earth
# Diametr_2Euro = 25.75 #Milimetri
# Diametr_2Euro/= 1000000 # Perevod v km
# Amount_of_2euro = R_Earth / Diametr_2Euro
# print("Neded amount 2 euro monets to fil ekvcator perimetr:", str(Amount_of_2euro))


# #3
# #Не смог перевести задание


# #4
# print("Rong see sõitis tsuhh tsuhh tsuhh, piilupart oli rongijuht. Rattad tegid rat tat taa, rat tat taa ja tat tat taa. Aga seal rongi peal, kas sa tead, kes olid seal?")
# v = input("Вам нравиться текст?(Да/Нет)Ж ")
# if v.lower == "Нет":
#     A = input("Введите свой текст: ")
#     print(A)
# else: 
#     print("Замечательно!")



# #5
# A = int(input("Please, input first square side(cm): "))
# B = int(input("Please, input second square side(cm): "))
# print("Square pirimetr:", str((A + B) * 2))
# print("Square square", str(A * B))


# #6
# Petrol = float(input("Please input quantity of used petrol(Liters): "))
# Distanse = float(input("Please input traveled distanse(Kilometers): "))

# Averege_per_100km = (Petrol / Distanse) * 100
# print("Averege petrol usage per 100 kilometers", str(Averege_per_100km))


# #7
# Speed_kmh = 29.9
# Speed_kmm = Speed_kmh / 60

# distance_in_km = Speed_kmm // 1  # Получаем только целую часть для километров
# distance_in_meters = (Speed_kmm - distance_in_km) * 1000  # Получаем метры

# if distance_in_km >= 1:
#     print("Traveled distance:", round(distance_in_km, 3), "kilometers")
# else:
#     print("Traveled distance:", round(distance_in_meters), "meters")


# #8
# Minutes = int(input("Input minutes: "))
# Hours = Minutes // 60
# Minutes1 = Minutes % 60
# hours = str(Hours) if Hours >= 10 else "0" + str(Hours)
# minutes1 = str(Minutes1) if Minutes1 >= 10 else "0" + str(Minutes1)
# print(str(hours) + ":" + str(minutes1))
