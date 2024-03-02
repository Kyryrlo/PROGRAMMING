from math import *
from random import *

print("Добро пожаловать в программу проверки знаний по математике")

while True:
    try:
        dif = int(input("Выбери сложность(1-Easy/2-Medium/3-Hard): "))
        break
    except:
        pass

print(f"Выбрана сложность {dif}")

while True:
    try:
        q_quest = int(input("Введите количество вопросов: "))
        break
    except:
        pass

print("Ответьте на {} вопроса(ов)".format(q_quest))
diff = [["+", "-"], ["+", "-", "/", "*"], ["+", "-", "/", "*", "**"]]

if 1 <= dif <= 3:
    operations = diff[dif - 1]
else:
    print("Вы ввели неправильное значение уровня сложности")
    exit()

cor_answer = 0

if dif == 1:
    for x in range(q_quest):
        oper = choice(operations)
        num1 = randint(-10, 10)
        num2 = randint(-10, 10)
        print(f"Решите пример: {num1} {oper} {num2}")
        while True:
            try:
                answ = int(input("Введите свой ответ: "))
                break
            except:
                pass

        if oper == "+":
            cor_answ = num1 + num2
        elif oper == "-":
            cor_answ = num1 - num2

        print("Правильно!") if cor_answ == answ else print("Неправильно")
        cor_answer += 1 if cor_answ == answ else 0

if dif == 2:
    for x in range(q_quest):
        oper = choice(operations)
        num1 = randint(-10, 50)
        num2 = randint(-10, 50)
        if oper == "/":
            num1 = randint(0, 50)
            num2 = randint(0, 50)
        print(f"Решите пример: {num1} {oper} {num2}")
        while True:
            try:
                answ = int(input("Введите свой ответ: "))
                break
            except:
                pass

        if oper == "+":
            cor_answ = num1 + num2
        elif oper == "-":
            cor_answ = num1 - num2
        elif oper == "/":
            cor_answ = num1 / num2
        elif oper == "*":
            cor_answ = num1 * num2

        print("Правильно!") if cor_answ == answ else print("Неправильно")
        cor_answer += 1 if cor_answ == answ else 0

if dif == 3:
    for x in range(q_quest):
        oper = choice(operations)
        oper1 = choice(operations)
        num1 = randint(1, 100)
        num2 = randint(1, 75)
        num3 = randint(1, 50)
        if oper == "**":
            num1 = randint(1, 10)
            num2 = randint(1, 20)
            num3 = randint(2, 4)
        if oper1 == "**":
            num1 = randint(1, 10)
            num2 = randint(1, 20)
            num3 = randint(2, 4)
        if oper == "/":
            num1 = randint(1, 100)
            num2 = randint(1, 50)
            num3 = randint(1, 75)
        if oper1 == "/":
            num1 = randint(1, 100)
            num2 = randint(1, 50)
            num3 = randint(1, 75)
        print(f"Решите пример: ({num1} {oper} {num2}) {oper1} {num3}")
        while True:
            try:
                answ = int(input("Введите свой ответ: "))
                break
            except:
                pass

        if oper == "+":
            cor_answ = num1 + num2
            if oper1 == "+":
                cor_answ += num3
            elif oper1 == "-":
                cor_answ -= num3
            elif oper1 == "/":
                cor_answ /= num3
            elif oper1 == "*":
                cor_answ *= num3
            elif oper1 == "**":
                cor_answ **= num3

        elif oper == "-":
            cor_answ = num1 - num2
            if oper1 == "+":
                cor_answ += num3
            elif oper1 == "-":
                cor_answ -= num3
            elif oper1 == "/":
                cor_answ /= num3
            elif oper1 == "*":
                cor_answ *= num3
            elif oper1 == "**":
                cor_answ **= num3

        elif oper == "/":
            cor_answ = num1 / num2
            if oper1 == "+":
                cor_answ += num3
            elif oper1 == "-":
                cor_answ -= num3
            elif oper1 == "/":
                cor_answ /= num3
            elif oper1 == "*":
                cor_answ *= num3
            elif oper1 == "**":
                cor_answ **= num3

        elif oper == "*":
            cor_answ = num1 * num2
            if oper1 == "+":
                cor_answ += num3
            elif oper1 == "-":
                cor_answ -= num3
            elif oper1 == "/":
                cor_answ /= num3
            elif oper1 == "*":
                cor_answ *= num3
            elif oper1 == "**":
                cor_answ **= num3

        elif oper == "**":
            cor_answ = num1 ** num2
            if oper1 == "+":
                cor_answ += num3
            elif oper1 == "-":
                cor_answ -= num3
            elif oper1 == "/":
                cor_answ /= num3
            elif oper1 == "*":
                cor_answ *= num3
            elif oper1 == "**":
                cor_answ **= num3

        print("Правильно!") if cor_answ == answ else print("Неправильно")
        cor_answer += 1 if cor_answ == answ else 0

percent = (cor_answer / q_quest) * 100

if percent < 60:
    print("Hinne 2")
elif 60 <= percent < 75:
    print("Hinne 3")
elif 75 <= percent < 90:
    print("Hinne 4")
else:
    print("Hinne 5")

print(f"Вы получили {percent}% правильных ответов")








