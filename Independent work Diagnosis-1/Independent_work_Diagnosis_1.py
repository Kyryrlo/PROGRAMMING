import tkinter as tk
import random

def wordChoice():
    with open("wordBase.txt", "r") as wB:
        wBlist = wB.read().splitlines()
        return list(random.choice(wBlist))

def keyClick(char):
    global word_state
    global labels
    if checkPressed():
        if '' in word_state:
            index = word_state.index('')
            word_state[index] = char.upper()
            labels[index].config(text=char.upper())
            resetColors()

def deletePressed():
    global word_state
    global labels
    if checkPressed():
        if any(word_state):
            index = next((i for i, x in enumerate(reversed(word_state)) if x), None)
            if index is not None:
                index = len(word_state) - index - 1
                word_state[index] = ''
                labels[index].config(text='')
                resetColors()

def checkWord():
    global word_state
    global labels
    entered_word = ''.join(word_state)
    if wordExists(entered_word):
        for i, label in enumerate(labels[:len(entered_word)]):
            char = word_state[i]
            if char == word[i]:
                label.config(bg="green")
            elif char in word:
                label.config(bg="yellow")
            else:
                label.config(bg="grey")
        resetWordState()
        nextRow()
    else:
        showErrorMessage(f"Слова '{entered_word}' не существует!")

def nextRow():
    global current_row
    current_row += 1

def wordExists(word):
    with open("wordBase.txt", "r") as wB:
        wBlist = wB.read().splitlines()
        return word.upper() in wBlist

def showErrorMessage(message):
    error_window = tk.Toplevel()
    error_window.title("Ошибка")
    error_label = tk.Label(error_window, text=message)
    error_label.pack()
    ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
    ok_button.pack()

def resetColors():
    global labels
    for label in labels:
        label.config(bg="#2A2A2A")

def resetWordState():
    global word_state
    for i in range(len(word_state)):
        word_state[i] = ''
        labels[i].config(text='')

def checkPressed():
    global word_state
    return '' in word_state

window = tk.Tk()
window.title("Wordle")
window.configure(background="#2A2A2A")

word = wordChoice()
word_state = [""] * len(word)
current_row = 0

frames = []
labels = []

for _ in range(6):
    frame = tk.Frame(window, bg="#2A2A2A")
    frame.pack()
    frames.append(frame)

    row_labels = []
    for _ in range(5):
        label = tk.Label(master=frame, text="", height=3, width=6, bg="#2A2A2A")
        label.pack(side="left")
        row_labels.append(label)
    labels.extend(row_labels)

keyboardLine1Frame = tk.Frame(window, bg="#2A2A2A")
keyboardLine1Frame.pack()
keyboardLine2Frame = tk.Frame(window, bg="#2A2A2A")
keyboardLine2Frame.pack()
keyboardLine3Frame = tk.Frame(window, bg="#2A2A2A")
keyboardLine3Frame.pack()

keyboardLine1 = ['Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ']
keyboardLine2 = ['Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', 'Э']
keyboardLine3 = ['Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю']

for char in keyboardLine1:
    keyboardButton = tk.Button(master=keyboardLine1Frame, text=char.upper(), width=8, height=3, bg="#494949", fg="white",
                               command=lambda c=char: keyClick(c))
    keyboardButton.pack(side="left")

for char in keyboardLine2:
    keyboardButton = tk.Button(master=keyboardLine2Frame, text=char.upper(), width=8, height=3, bg="#494949", fg="white",
                               command=lambda c=char: keyClick(c))
    keyboardButton.pack(side="left")
    char.upper
for char in keyboardLine3:
    keyboardButton = tk.Button(master=keyboardLine3Frame, text=char.upper(), width=8, height=3, bg="#494949", fg="white",
                               command=lambda c=char: keyClick(c))
    keyboardButton.pack(side="left")

frame4 = tk.Frame(window, bg="#494949")
frame4.pack(side="right")
deleteButton = tk.Button(master=frame4, bg="#494949", text="Backspace", height=3, width=20, fg="white", command=deletePressed)
deleteButton.pack(side="right")

frame5 = tk.Frame(window, bg="#494949")
frame5.pack(side="left")
checkButton = tk.Button(master=frame5, bg="#494949", text="Check", height=3, width=20, fg="white", command=checkWord)
checkButton.pack(side="left")

window.mainloop()
