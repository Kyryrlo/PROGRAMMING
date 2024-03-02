from math import * 
from random import *

print("Добро пожаловать в игру Камень, Ножницы, Бумага")

while True:
    try:
        player = int(input("С кем хотите играть, с игроком или с компьютером?(1-компьютер,2-игрок): "))
        break
    except:
        print("Вы ввели неправильное значение")

if player == 1 or player == 2:
    list1 = [0, 1, 2] # 0 - Камень, 1 - Ножницы, 2 - Бумага
else:
    print("Вы ввели неправильное значение")
    exit()

# ИГРА С РОБОТОМ
if player == 1:

    user_wins = []
    comp_wins = []
    nobody_wins = []
    
    while True:
        quant = int(input("Введите сколько раундов хотите сыграть: "))
        for x in range(quant):
            comp_choose = choice(list1)
            
            while True: 
                while True:   
                    try: 
                        user_choose = int(input("Выберете 0 - Камень, 1 - Ножницы, 2 - Бумага: "))
                        break
                    except:
                        print("Вы не выбрали предмет")
                if user_choose == 0 or user_choose == 1 or user_choose == 2:
                    break
                else:
                    print("Вы не выбрали свой предмет")
            
            if user_choose == 0 and comp_choose == 1:
                print("Вы выиграли!")
                print(f"Компьтер выбрал: {comp_choose}")
                user_wins.append(1)
            elif user_choose == 1 and comp_choose == 2:
                print("Вы выиграли!")
                print(f"Компьтер выбрал: {comp_choose}")
                user_wins.append(1)
            elif user_choose == 2 and comp_choose == 0:
                print("Вы выиграли!")
                print(f"Компьтер выбрал: {comp_choose}")
                user_wins.append(1)
            elif user_choose == comp_choose:
                print("Ничья!")
                print(f"Компьтер выбрал: {comp_choose}")
                nobody_wins.append(1)
            else:
                print("Вы проиграли")
                print(f"Компьтер выбрал: {comp_choose}")
                comp_wins.append(1)             
        
        stop = input("Хотите ещё? \nЕсли да - нажмите Enter \nЕсли нет - введите (stop): ")
        if stop.lower() == "stop":
            break
    
    print(f"Вы выиграли {len(user_wins)} раз(а)")
    print(f"Компьтер выиграл {len(comp_wins)} раз(а)")
    print(f"Ничья случилась {len(nobody_wins)} раз(а)")
    

# ИГРА С ДРУГИМ ИГРОКОМ
if player == 2:
    
    user0_wins = []
    user1_wins = []
    nobody_wins = []
    
    while True:
        try: 
            quant = int(input("Введите сколько раундов хотите сыграть: "))
        except:
            print("Вы ввели неправильное значение")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Когда первый человек выбирает предмет, пользователь 2 не должен подсматривать")    
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        while True:
            for x in range(quant):
                while True:   
                    while True:    
                        try: 
                            user0_choose = int(input("Пользователь 1, Выберете 0 - Камень, 1 - Ножницы, 2 - Бумага: "))
                            break
                        except:
                            print("Вы не выбрали предмет")
                    if user0_choose == 0 or user0_choose == 1 or user0_choose == 2:
                        break
                    else:
                        print("Вы не выбрали свой предмет")
                for x in range(35):
                    print()
                while True:   
                    while True:    
                        try: 
                            user1_choose = int(input("Пользователь 2, Выберете 0 - Камень, 1 - Ножницы, 2 - Бумага: "))
                            break
                        except:
                            print("Вы не выбрали предмет")
                    if user1_choose == 0 or user1_choose == 1 or user1_choose == 2:
                        break
                    else:
                        print("Вы не выбрали свой предмет")
                        
                if user0_choose == 0 and user1_choose == 1:
                    print("Вы выиграли!")
                    print(f"Первый пользователь выбрал: {user0_choose}")
                    print(f"Второй пользователь выбрал: {user1_choose}")
                    user_wins.append(1)
                elif user0_choose == 1 and user1_choose == 2:
                    print("Вы выиграли!")
                    print(f"Первый пользователь выбрал: {user0_choose}")
                    print(f"Второй пользователь выбрал: {user1_choose}")
                    user_wins.append(1)
                elif user0_choose == 2 and user1_choose == 0:
                    print("Пользователь 1 выиграл!")
                    print(f"Первый пользователь выбрал: {user0_choose}")
                    print(f"Второй пользователь выбрал: {user1_choose}")
                    user_wins.append(1)
                elif user0_choose == user1_choose:
                    print("Ничья!")
                    print(f"Первый пользователь выбрал: {user0_choose}")
                    print(f"Второй пользователь выбрал: {user1_choose}")
                    nobody_wins.append(1)
                else:
                    print("Пользователь 2 выиграл!")
                    print(f"Первый пользователь выбрал: {user0_choose}")
                    print(f"Второй пользователь выбрал: {user1_choose}")
                    comp_wins.append(1)    
        stop = input("Хотите ещё? \nЕсли да - нажмите Enter \nЕсли нет - введите (stop): ")
        if stop.lower() == "stop":
            break
    print(f"Пользователь 1 выиграл {len(user0_wins)} раз(а)")
    print(f"Пользователь 2 выиграл {len(user1_wins)} раз(а)")
    print(f"Ничья случилась {len(nobody_wins)} раз(а)")