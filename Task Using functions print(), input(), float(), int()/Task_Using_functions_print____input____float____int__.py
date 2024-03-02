from math import *

from random import *

from token import *

# print("tere tulemast")
# kool=input("mis koolis sa kaid?: ") #str kool
# kursus=int(input("mis kursus?")) #int kursus
# print("Tere tulemast kooli" +kool+"!/nOle hea "+str(kursus)+".kursuseopilaseks")
# print("Tere tulemast kooli",kool,"!/nOle hea",kursus,".kursuse opilaseks!")
# print("Tere tulemastkooli "+kool.upper()+"!\nOle hea "+str(kursus)+".kursuse opilaseks!") #Kool+"TTHK"
# print ("Tere tulrmast kooli",kool.lower(),"!\nOle hea",kursus,".kursuse opiaseks!")#kool=tthk
# print(type(kool))
# print(type(kursus))


# arv1=float(input("Arv 1: "))
# arv2=float(input("Arv 2: "))
# print(arv1*arv2)
# print(arv1+arv2)
# print(arv1-arv2)
# print(arv1/arv2)
# print("{0} + {1}={2}".fomat(arv1,arv2,arv1+arv2))#summa
# print("{0} - {1}={2}".fomat(arv1,arv2,arv1-arv2))#lahutamine
# print("{0} * {1}={2}".fomat(arv1,arv2,arv1*arv2))#korritus
# print("{0} / {1}={2}".fomat(arv1,arv2,arv1/arv2))#jagamine
# print("{0} ** {1}={2}".fomat(arv1,arv2,arv1**arv2))#astendamine
# print("{0} astmes {1} jaak {2}".fomat(arv1,arv2,arv1+arv2))#jagamisjaak
# print("{0} ja {1} jagamise tais osa {2}".fomat(arv1,arv2,arv1+arv2))


#       #Ulesanne "Funktsioonide print(), input(), float(), int(), kusutamine"

# # 1
# print("Tere,maailm!")
# nimi=input("MIs on sinu nimi?")
# print("Tere maailm!",nimi, "tervistan sind!")
# vanus=int(input("Kui vana sa oled?"))
# print("Tere maailm! Tervistan sind!",nimi,"Sa olede",vanus, "astad vana.")

# #2
# age = 18                    # int

# name = "Яак"                # str

# leanth = 16,5               # float

# if_goes_to_school = True    # bool  # if_goes_to_school != False

# print(type(age))
# print(type(name))
# print(type(leanth))
# print(type(if_goes_to_school))



# # 3
# kommide_arv=int(input("Laual olevate kommide arv: "))
# print("laua peal on" + str(kommide_arv))
# mitu=int(input("Mitu kommi sa soovid suua: "))
# kommide_arv-=mitu
# print("Nuud laua peal on ",kommide_arv)


# # 4
# P = float(input("Vvedite okruznost dereva: "))
# D = P / pi
# print("Diametr raven:", str(D))


# # 5
# a=float(input("Esimene kateet: "))
# b=float(input("Teine kateet: "))
# d=sqrt(a**2+b**2)
# d1=hypot(a,b)
# print("d=",d)
# print("d1=",d1)


# # 6
# try:
#     aeg=float(input("Mitu tundi kulus soiduks?: ")) 
#     teepikkus=float(input("Mitu kilkmeetrit soitsid: "))
#     kiirus=teepikkus/aeg
#     print("Sinu kiirus oli " + str(kiirus) + " km/hr")
# except: 
#     print("Andmetuubi Viga!")
# kiirus=aeg/teepikkus

# # 7
# a1 = randint(1, 10)
# a2 = randint(1, 10)
# a3 = randint(1, 10)
# a4 = randint(1, 10)
# a5 = randint(1, 10)
# average = (a1 + a2 + a3 + a4 + a5) / 5
# print("Arvude {} {} {} {} ja {} aritmeetiline keskmine on {}".format(a1, a2, a3, a4, a5, average))

# # 8
# print("  @..@")
# print(" (----)")
# print("( \__/ )")
# print(" ^^ "" ^^")


# # 9
# a=randint(1,20)
# b=randint(1,10)
# c=randint(1,15)
# P=a+b+c
# print(P)

# # 10
# Costpizza = 12.90
# Percentoftips = 0.1 
# Tipssumm = Costpizza * Percentoftips
# Fullprice = Costpizza + Tipssumm
# Summperperson = Fullprice / 2
# print("Everyone_must_pay",str(Summperperson), "euro.")


