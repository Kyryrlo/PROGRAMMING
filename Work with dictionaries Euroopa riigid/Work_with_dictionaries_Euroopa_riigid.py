from MyModule1 import *
from random import *

while True:
    try:
        v = int(input("Хотите проверить свои знания европейских стран и их столиц (1-Да,2-Нет)?: "))
        if v == 1 or v == 2:
            break
        else:
            print("Введите 1/2.")
    except:
        print("Ввели неверное значение.")

if v == 1:
    cap_list, count_list, country_cap = dictionary_reading()
    cor_answ = 0 
    answ = 0

    while True:
        rand_cap = choice(list(country_cap.keys()))
        rand_count = country_cap[rand_cap]
    
        rand = randint(1, 2)
        if rand == 1:
            question = rand_cap  
            print(f"Какой страны {question} столица?")
        else:
            question = rand_count
            print(f"Какая у {question} столица?")
        
        user_answ = input("Введите ответ (Чтобы остановить - stop):")
    
        if user_answ.lower() == "stop":  
            break
        
        user_answ = user_answ.capitalize()
        answ += 1
    
        if rand == 1 and user_answ == rand_count:
            cor_answ += 1
        elif rand == 2 and user_answ == rand_cap:
            cor_answ += 1

    percent = cor_answ / answ * 100
    print(f"Вы набрали {percent} процентов правильных ответов.")
else: 
    pass

#1,2-----------------------------------------------------------------------------------------------------------------
user_word = input("Введите название страны, или столицу: ")
user_word = user_word.capitalize()
answer = find_count_or_cap(user_word)
if answer == False:
    print(f"Извините, {user_word} отсутствует у нас в справочнике")
    want = int(input(f"Хотите добавить {user_word} в словарь (1-Да, 2-Нет): "))
    
    if want == 1:
        while True:
            try:
                user_cap = input("Введите столицу: ").strip()
                user_country = input("Введите страну: ").strip()
                if user_cap and user_country:
                    break
            except:
                print("Вы ввели неверное значение.")
                
        inserting(user_cap, user_country)
        print("Ваши данные добавлены")
    else: 
        pass


print(f"{user_word} - столица страны {answer}" if user_word in cap_list else f"{user_word} - страна со столицей {answer}")
cor_or_incor = int(input("Соответсвуют ли наши данные реальности? Хотите внести коррективы?(1-Да,2-Нет): "))
if cor_or_incor == 1:
    want1 = True
elif cor_or_incor == 2:
    want1 = False   
        

#3-------------------------------------------------------------------------------------------------------------------
if want1:
    if user_word in cap_list:
        what_to_cor = input(f"{user_word} какой страны столица?: ")
        dictionary_correction(user_word, what_to_cor)
    else:
        what_to_cor = input(f"Какая столица у страны {user_word}?: ")
        dictionary_correction(user_word, what_to_cor)