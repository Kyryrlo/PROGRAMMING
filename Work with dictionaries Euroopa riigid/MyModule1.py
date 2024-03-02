#--------------------------------------------------------------------------------------------------------------------
def dictionary_reading():
    with open("Cap.txt", "r") as Cap:
        cap_list = Cap.read().split("\n")
    with open("Country.txt", "r") as Country:
        count_list = Country.read().split("\n")
    
    country_cap = {}
    for x, country in enumerate(count_list):
        if x < len(cap_list):
            country_cap[cap_list[x]] = country
    
    return cap_list, count_list, country_cap


#1------------------------------------------------------------------------------------------------------------------- 
def find_count_or_cap(user_word):
    cap_list, count_list, country_cap = dictionary_reading()
    for cap, country in country_cap.items():
        if user_word == cap.capitalize():
            return country.capitalize()
        elif user_word == country.capitalize():
            return cap.capitalize()
    return False
            

#2------------------------------------------------------------------------------------------------------------------- 
def inserting(user_cap, user_country):
    cap_list, count_list, country_cap = dictionary_reading()
    
    cap_list.append(user_cap)
    count_list.append(user_country)
    country_cap[user_cap] = user_country
    caplist = "\n".join(cap_list)
    countlist = "\n".join(count_list)
    with open("Cap.txt", "w") as cap, open("Country.txt", "w") as Country:
        cap.write(caplist)
        Country.write(countlist)
    
    return cap_list, count_list


#3------------------------------------------------------------------------------------------------------------------- 
def dictionary_correction(user_word, what_to_cor):
    cap_list, count_list, country_cap = dictionary_reading()
    if user_word in cap_list:
        inserting(user_word, what_to_cor)
    elif user_word in count_list:
        for key, val in country_cap.items():
            if user_word == val:
                del country_cap[key] 
                country_cap[what_to_cor] = user_word
            else:
                print("Вы не можете исправить то, чего нет в списке")
    print("Исправления записаны...")
    
        
    
