from random import *

#--------------------------------------------------------------------------------------------------------------------
def files_in_lists():
    with open("eng.txt", 'r') as e:
        e_list = [line.strip().lower() for line in e]    
    with open("rus.txt", 'r') as r:
        r_list = [line.strip().lower() for line in r]
        
    return e_list, r_list
        
#1--------------------------------------------------------------------------------------------------------------------
def Word_Translation(u_word):
    v = 0
    e_list, r_list = files_in_lists()
    
    if u_word.lower() in e_list:
    
        e_ind = e_list.index(u_word)
        v = r_list[e_ind]
        c = 1
        
    if u_word.lower() in r_list:
    
        r_ind = r_list.index(u_word)
        v = e_list[e_ind]
        C = 1
        
    return v, u_word


#2-------------------------------------------------------------------------------------------------------------------
def word_insertation(lang, word, translation):
    e_list, r_list = files_in_lists()

    if lang == 1:
        e_list.append(word)
        r_list.append(translation)
    if lang == 2:
        r_list.append(word)
        e_list.append(translation)
    
    elist = []
    rlist = []
    for el in e_list:
        a = el.lower()
        elist.append(a)
    for el in r_list:
        a = el.lower()
        rlist.append(a)
    
    e_list = "\n".join(elist)
    r_list = "\n".join(rlist)
    print(r_list + "\n" + "\n" + e_list)
        
    with open("eng.txt", "w") as e:
        e.write(e_list)
    with open("rus.txt", "w") as r:
        r.write(r_list)

    
#3--------------------------------------------------------------------------------------------------------------------
def dictionary_correction(word, cor_word):
    e_list, r_list = files_in_lists()
    
    if word in r_list:
        word_ind = r_list.index(word)
        e_list.pop(word_ind)
        e_list.insert(word_ind, cor_word)
    elif word in e_list:
        word_ind = e_list.index(word)
        r_list.pop(word_ind)
        r_list.insert(word_ind, cor_word)
        
    elist = []
    rlist = []
    for el in e_list:
        a = el.lower()
        elist.append(a)
    for el in r_list:
        a = el.lower()
        rlist.append(a)
    
    e_list = "\n".join(elist)
    r_list = "\n".join(rlist)
    print(r_list + "\n" + "\n" + e_list)
        
    with open("eng.txt", "w") as e:
        e.write(e_list)
    with open("rus.txt", "w") as r:
        r.write(r_list)
    print("Ваш, исправленный, перевод записан")


#4-------------------------------------------------------------------------------------------------------------------
def knowledge_control():
    cor_answ = 0
    questions = 0
    e_list, r_list = files_in_lists()

    while True:    
        v = randint(1,2)
        num = randint(0, len(e_list) - 1)

        if v == 1:
            user_answ = input(f"Введите перевод для {r_list[num]} (Для того чтобы прекратить - введите stop): ")
            if user_answ.lower() == "stop":
                break
            elif user_answ == e_list[num]:
                questions += 1
                cor_answ += 1
                print("Молодец, правильно! ")
            else: 
                questions += 1
                print("Неправильно")
        elif v == 2:
            user_answ = input(f"Введите перевод для {e_list[num]} (Для того чтобы прекратить - введите stop): ")
            if user_answ.lower() == "stop":
                break
            elif user_answ == r_list[num]:
                questions += 1
                cor_answ += 1
                print("Молодец, правильно! ")
            else: 
                questions += 1
                print("Неправильно")
                
    return cor_answ, questions
    percent = (cor_answ / questions) * 100
    print(f"Вы ответили правильно на {percent} процентов ответов")

