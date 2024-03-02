#1 ------------------------------------------------------------------------------------------------------------------

def Lisamine(i: list, p: list, k: int):
    """Andmete lisamine listidesse
    Tagastab listud
    :parametr list i: Inimesta nimekiri
    :parametr list p: Palkage loetelu
    :parametr int k: Inimeste kogus
    :rtype: list, list
    """
    for x in range(k):
        nimi = input("Введите имя: ")
        palk = int(input("Введите зарплату: "))
        i.append(nimi)
        p.append(palk)
    return i, p

#2 ------------------------------------------------------------------------------------------------------------------

def Kustuta(who, i, p):
    """
    """
    if who in i:
        who_ind = i.index(who)
        i.pop(who_ind)
        p.pop(who_ind)
#3 ------------------------------------------------------------------------------------------------------------------

def Biggest_sallary(p: list,i : list):
    p_list = p.copy()
    i_list = i.copy()
    max_p_list = []
    max_i_list = []
    
    while True:
        max_p = max(p_list)
        ind_max_p = p_list.index(max_p)
        max_p_list.append(max_p)
        max_i_list.append(i_list[ind_max_p])
        p_list.pop(ind_max_p)
        i_list.pop(ind_max_p)
        if max_p == max_p_list[-1]:
            pass
        else:
            break
    return max_p_list, max_i_list



    