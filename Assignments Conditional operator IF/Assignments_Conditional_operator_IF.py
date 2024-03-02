from math import*

#1.a
# nimi=input("Введите имя: ")

# if nimi=="Juku":
#    vana=int(input("Введите возраст: ")) #Начинаеться 1.b
#    if vana<6:
#        print("Билет бесплатен")
#    elif vana>=6 and vana<=14:
#        print("Lastepilet")
#    elif vana>=15 and vana<=65:
#        print("täispilet")
#    elif vana>65 and vana<150:
#        print("Билет по скидке")
#    else:
#        print("Вы указали неверный возраст")
# else:
#    print("Вы не Juku")
    


#2
# nimi1 = input("Введите имя №1: ")
# nimi2 = input("Введите имя №2: ")
# print(nimi1 + ", " + nimi2 + ", вы сегодня соседи по скамейке!")



#3
# a=8
# b=4
# S=(a*b)*2
# renovation=input("Хотите провести ремонт?(Да/Нет): ")

# if renovation=="Да":
#     cost=float(input("Введите цену за квадратный метр(В евро): "))
#     if cost>0:
#         v=cost*S
#         print(v)
#     else:
#         print("Повезло вам с бесплатным ремонтом")
# else:
#     print("Вы не хотите делать ремонт.")
    


#4
# a=float(input("Введите сколько вы заплатили: "))

# if a>700 or a==700 and a>0:
#     b=a/100*30
#     c=a-b
#     print("От вас к оплате: " + str(c))
# else:
#     print("К оплате " + a)


#5
# Temp=float(input("Введите ткспературу(В градусах по цельсию): "))

# if Temp>18 and Temp<35:
#     print("Поздравляю, желательная температура в помещении в зимнее время")
# elif Temp>35:
#     print("Советуем вам понизить температуру в помещении")
# else:
#     print("Советуеться повысить температуру в помещении")


#6
# hight=int(input("Введить свой рост(В сантиметрах): "))

# if hight<25:
#     print("Вы указали неверное значение")
# elif hight<169:
#     print("Вы низкий")
# elif hight>=170 and hight<=190:
#     print("Вы среднего роста")
# elif hight>190 and hight<300:
#     print("Вы высокий") 
# elif hight>300:
#     print("Вы указали неверное значение")
# else:
#     print("Вы указали неверное значение")


#7
# hight=int(input("Введить свой рост(В сантиметрах): "))
# gender=input("Введить свой пол(Мужской/Женский): ")

# if gender=="Женский":
#     if hight<=140 and hight>20:
#         print("Вы низкая")
#     elif hight>140 and hight<168:
#         print("Вы среднего роста")
#     elif hight>=168 and hight<270:
#         print("Вы высокая")
#     else:
#         print("Вы указали неверное значение")
# elif gender=="Мужской":
#     if hight<=168 and hight>25:
#         print("Вы низкий")
#     elif hight>168 and hight<185:
#         print("Вы среднего роста")
#     elif hight>=185 and hight<300:
#         print("Вы высокий")
#     else:
#         print("Вы указали неверное значение")
        


#8


# bread = 0.7
# milk = 1
# leiba = 6.4

# want_bread = input("Хотите ли вы купить хлеб? (Да/Нет)")
# want_milk = input("Хотите ли вы купить молоко? (Да/Нет)")
# want_leiba = input("Хотите ли вы купить кондитерские изделия? (Да/Нет)")
# total_cost = 0

# if want_bread == "Да":
#     total_cost += bread
# if want_milk == "Да":
#     total_cost += milk
# if want_leiba == "Да":
#     total_cost += leiba
# if total_cost > 0:
#     print(f"Общая стоимость ваших покупок: {total_cost} евро")
# else:
#     print("Вы ничего не купили")



#9
# A=float(input("Введите первую сторону квадрата(В см): "))
# B=float(input("Введите вторую сторону квадрата(В см): "))

# if A==B:
#     print("Это квадрат!")
# else:
#     print("Это не квадрат!")


#10
# A=float(input("Введите первое число: "))
# B=float(input("Введите Второе число: "))
# C=input("Введите желаемое действие(+, -, *, /): ")

# if C=="+":
#     v=A+B
#     print(v)
# elif C=="-":
#     V=A-B
#     print(V)
# elif C=="*":
#     D=A*B
#     print(D)
# elif C=="/":
#     F=A/B
#     print(F)
# else:
#     print("Данное действие не поддрежваеться")



#11
# ------------


#12
# A=float(input("Введите цену товара(В евро): "))

# if A==10:
#     B=A-(A/100*10)
#     print("К оплате" + str(B) + "евро")
# elif A>10:
#     C= A-(A/100*20)
#     print("К оплате" + str(C) + "евро")
# elif A<0:
#     print("Вы ввели неправильное значение!")
# else:
#     print("К оплате" + str(A) + "евро")



#13
# gender=input("Введите свой пол(Мужчина/Женщина): ")

# if gender.lower()=="мужчина":
#     vana=float(input("Введите возраст: "))
#     if vana>=16 and vana<=19:
#         print("Ваша заявление будет рассмотрено")
#     else:
#         print("Извините, вы не подхолите нам по возрасту")
# elif gender.lower()=="женщина":
#     print("Извините мы ищем только мужчин")
# else:
#     print("Вы ввели некорректное значение")


#14
quantity = int(input("Введите количество людей: "))
bus = int(input("Введите количество мест в автобусе: "))

A = quantity // bus
B = quantity % bus

if B > 0:
    A += 1
    print(f"Необходимо " +str(A)+ " автобуса для перевозки всех людей.")
    print(f"В последнем автобусе будет " +str(B)+ " человек.")
else:
    print(f"Необходимо " +str(A)+ " автобуса для перевозки всех людей.")
    



