
# # 1 ---------------------------------------------------------------------------------------------------------

def arithmetic(a: float, b: float, t: str) -> any:
    """Lihtne kalkulaator.
    + - liitmine
    - - lahutamine
    * - okrrutamine
    / - jagamine
    :param float a: arv
    :param float d: arv
    :param atr t: atitmeetiline tehing
    :rtype: var Maaramata tuup(float or str)
    """
    if t in ["+","-","*","/"]:
        if b == 0 and t == "/":
            vastus = "DIV/0"
        else:
            vastus = eval(str(a)+ t + str(b))
    else:
        vastus = "Tundmatu tehe"
        
    return vastus

# v = arithmetic(float(input("Arv1")), float(input("Arv2")), input("trhing"))
# print(f"Vastus = {v}")


# # 2 ---------------------------------------------------------------------------------------------------------

def is_year_leap(year: float) -> bool:
    """Liigaasta leidmine
    Tagastab True, kui liigaasta ja False kui on tavaline aasta.
    :param int aasta: aasta number
    :rtype: bool tagastab loogilises formadis tulemus
    """
    
    if year % 4 == 0:
        return True 
    else:
        return False
    
# v = is_year_leap(int(input("Введите год: ")))
    
# if v:
#     print("Год высокосный")
# else:
#     print("Год не высокостный")
    

# 3 ---------------------------------------------------------------------------------------------------------

def square(side):
    per = side * 4
    S = side * side
    diag = side *(2**(1/2))
    return(side, per, S, diag)
    
# side, per, S, diag = square(int(input("Введите сторону квадрата: ")))
# print(f"Периметр квадрата со стороной {side} = {per}")   
# print(f"Площадь квадрата со стороной {side} = {S}")
# print(f"Дмагональ квадрата со стороной {side} = {diag}")


# # 4 ---------------------------------------------------------------------------------------------------------

def season(a, month):
    if month == 1 or month == 2 or month == 12:
        print(f"{month}-ый месяц - это зима")
    if month == 3 or month == 4 or month == 5:
        print(f"{month}-ый месяц - это весна")
    if month == 6 or month == 7 or month == 8:
        print(f"{month}-ый месяц - это лето")
    if month == 9 or month == 10 or month == 11:
        print(f"{month}-ый месяц - это осень")

# season(int(input("Введите какой сейчас месяц(1-12): ")))

# # 5 ---------------------------------------------------------------------------------------------------------

def bank(a, years):
    for x in range(years):
        a = a + a * 0.1
    print(f"За {years} лет вы заработали {round(a, 2)} Евро")
        
# bank(int(input("Сколько вы хотите вложить: ")), int(input(f"Введите на сколько лет хотиите вложить свои деньги: ")))

# # 6 ---------------------------------------------------------------------------------------------------------

def is_prime(num) -> bool:
    for x in range(2, num - 1):
        if num % x == 0:
            return (False, num)
        else:
            return (True, num)
    
# v, num = is_prime(int(input("Введите число от 1 до 1000: ")))
# if v == True:
#     print(f"Ваше чилсо({num}) - простое")
# else:
#     print(f"Ваше чилсо({num}) не являеться простым") !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
# # 7 ---------------------------------------------------------------------------------------------------------

# def date(day, month, year):
    
#     if day in range(1,31) and month in [1,3,5,7,8,10,12]:
#         v = True
#     elif day in range(1,29) and month == 2 and is_year_leap(year):
#         v = True
#     elif day in range(1,30) and month in [2,4,6,9,11]:
#         v = True
#     else:
#         v = False
#     return v

# v = date(int(input("Введите день(1-31): ", )), int(input("Введите месяц(1-12): ", )), int(input("Введите год: ", )))
# if v:
#     print("Выша дата реальна")
# else:
#     print("Выша дата не реальна")

# # 8 ---------------------------------------------------------------------------------------------------------

def XOR_CIPHR():
    pass
def XOR_UNCIPHR():
    pass


while True:
    while True: 
        try:
            des = int(input("Вы хотите зашифровать текст или разшифровать?(1-Да, 2-Нет): "))
            break
        except:
            print("Вы ввели неправильное значение")
    if des == 1 or des == 2:
        break
    else:
        print("Вы ввели неправильное значение")

if des == 1:
    print("Вас приветствует програма шифрования текста")
elif des == 2:
    print("Вас приветствует програма дешифрования текста")