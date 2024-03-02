from MyModule import *
#4-------------------------------------------------------------------------------------------------------------------
while True:
    try:    
        wan = int(input("Хотите проверить свои знания английского?(1-Да, 2-Нет): "))
        if wan == 1:
            wan = True
            break
        else: 
            wan = False
            break
    except:
        print("Вы ввели неправильное значение")

if wan:
    cor_answ, questions = knowledge_control()
    percent = (cor_answ / questions) * 100
    print(f"Вы ответили правильно на {percent} процентов ответов")
    


#1-------------------------------------------------------------------------------------------------------------------
cont = True
while True:
    try:
        u_word = str(input("Введите слово, которое вы хотите перевести: "))
        break
    except ValueError:
        print("Вы ввели неверное значение")
                
v, urs_word = Word_Translation(u_word)

print(f"Ваше слово {urs_word} переводиться как {v}") if v != 0 else print("Ваше слово отсутствует у нас в словаре")
wan = int(input("Хотите добавить перевод?(1-Да, 2-Нет):"))


#2-------------------------------------------------------------------------------------------------------------------
if wan == 1:
    lang = int(input("Введите язык первого слова(1-English/2-Russian): "))
    word = input("Введите слово: ")
    translation = input("Введите перевод: ")
    word_insertation(lang, word, translation)
    print("Ваш перевод добавлен")
    cont = False

    
#3-------------------------------------------------------------------------------------------------------------------
if cont:  
    while True:
        try:    
            CorOrIncor = int(input("Вы считаете перевод корректным, или хотите внести коррективы?(1-Да, 2-Нет): "))
            if CorOrIncor == 1:
                want = True
                break
            else:
                want = False
                break
        except:
            print("Вы ввели неправильные значения")
        
    if want:
        dictionary_correction(u_word, input("Введите правильный перевод: "))
        

