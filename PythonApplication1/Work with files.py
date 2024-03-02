def Loe_failist(fail: str) ->list:
    jarjend = []
    f = open(fail, 'r', encoding = "utf-8")
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend


def Kirjuta_failisse(fail: str, jarjend: list):
    f = open(fail,'w', encoding = "utf-8")
    for item in jarjend:
        f.write(item+'\n')
    f.close()


Paevad = Loe_failist('Paevad.txt')    
print(Paevad)



list_ = []
for i in range(5):
    nimi = input(str(i+1) + "Введите имя: ")
    list_.append(nimi)
Kirjuta_failisse("Nimed.txt", list_)
    
with open("Nimed.txt", "r") as f:
    print(f.read())