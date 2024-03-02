from math import *

print("Tere! Olen sinu uus sõber - Python!" )
print()
nimi = input("Введите своё имя: ")
print()
print("У тебя красивое имя,", nimi)
print()

while 0 == 0:
    try:
        answer = int(input("Ты скажешь мне свой идекс массы тела?(1-Да,0-Нет): "))
        if answer in (0,1):
            break
    except ValueError:
        pass
    

if answer == 1:
    while 0 ==0:
        try:
            pikkus = int(input("Введите свой рост(В сантиметрах): ")) 
            if pikkus < 270 and pikkus > 30:
                break
            else:
                print("Вы указаали неверный вес ")
        except ValueError:
            pass
    print()


    while 0 == 0:
        try: 
            mass = int(input("Введите свой весс(Килограммы): "))
            if mass < 1000 and mass > 17:
                break
            else:
                print("Вы указаали неаерный вес ")
        except ValueError:
            pass
    print()

    indeks = mass / (0.01 * pikkus) ** 2
    print(nimi + "! Sinu keha indeks on: " + str(round(indeks, 1)))
    print()
    
    if indeks < 16:
        print("Нездоровый недостаточный вес")
    if indeks >= 16 and indeks < 19:
        print("Низкий вес")
    elif indeks >= 19 and indeks < 25:
        print("Нормальный вес")
    elif indeks >= 25 and indeks < 30:
        print("Избыточной вес")
    elif indeks >= 30 and indeks < 35:
        print("Ожирение")
    elif indeks >= 35 and indeks < 40:
        print("Тяжёлое ожирение")
    elif indeks >40:
        print("Угрожающее здоровью ожирение")
    print()
    print("Tervisele ohtlik alakaal   < 16")
    print("Alakaal	                   16 - 19")
    print("Normaalkaal	           19 - 25")
    print("Ülekaal	                   25 - 30")
    print("Rasvumine	           30 - 35")
    print("Tugev rasvumine            35 - 40")
    print("Tervisele ohtlik rasvumine > 40")
else:
    print("Очень жаль! Это очень полезная информация!")
    print()

print()
print("До встречи, " + nimi + "! Твой навсегда, Python!" )