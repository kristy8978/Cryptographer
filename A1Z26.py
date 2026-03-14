from tkinter import *
from tkinter import messagebox as mb


ru_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з',
               'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
               'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч',
               'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
en_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z']
symbol = [" ", ",", ".", "!", "?"]


global lagage
global code_decode
global fraze
global label


def coding(lan, code, string):
    global label
    global symbol

    res = ''

    if code == 0:
        if lan == 0:
            for i in string:
                if i == ' ':
                    res = res[:-1] + ' '
                else:
                    if i not in symbol:
                        res += str(ru_alphabet.index(i)) + '-'
                    else:
                        res += i
        else:
            for i in string:
                if i == ' ':
                    res = res[:-1] + ' '
                else:
                    if i not in symbol:
                        res += str(en_alphabet.index(i)) + '-'
                    else:
                        res += i
    else:
        string1 = string.split(' ')

        if lan == 0:
            for i in string1:
                j = i.split("-")
                temp = ''
                for k in j:
                    if k not in symbol:
                        if len(j) - 1 == len(temp):
                            temp += ru_alphabet[int(k)]
                            temp += ' '
                        else:
                            temp += ru_alphabet[int(k)]
                    else:
                        temp += ' ' + k
                res += temp
        else:
            for i in string1:
                j = i.split("-")
                temp = ''
                for k in j:
                    if k not in symbol:
                        if len(j) - 1 == len(temp):
                            temp += en_alphabet[int(k)]
                            temp += ' '
                        else:
                            temp += en_alphabet[int(k)]
                    else:
                        temp += k
                res += temp
    label.configure(text = res.title())

def run():
    global lagage
    global code_decode
    global fraze

    lan1 = lagage.get()
    code_or_decode = code_decode.get()
    string2 = fraze.get().lower()
    coding(lan1, code_or_decode, string2)

def a1z26_run():
    root = Toplevel()

    root.resizable(False, False)
    root.geometry("600x300+600+300")

    root["bg"] = '#3abf8d'
    root.iconbitmap("1995724.ico")
    root.title("Шифр A1Z26")


    global label
    global lagage
    global code_decode
    global fraze

    st = StringVar(value = 'Введите строку!')
    lagage = IntVar(value = 0)
    code_decode = IntVar(value = 0)


    Label(root,
          text = "Шифр A1Z26",
          bg = '#3abf8d',
          font = ("Console", 20, 'bold')).place(x = 220, y = 10)

    Radiobutton(root,
                text = 'Русский',
                bg = '#3abf8d',
                selectcolor = 'lime',
                value = 0,
                variable = lagage).place(x = 150, y = 80)

    Radiobutton(root,
                text = 'Английский',
                bg = '#3abf8d',
                selectcolor = 'lime',
                value = 1,
                variable = lagage).place(x = 150, y = 120)

    Radiobutton(root,
                text = 'Зашифровать',
                bg = '#3abf8d',
                selectcolor = 'lime',
                value = 0,
                variable = code_decode).place(x = 300, y = 80)

    Radiobutton(root,
                text = 'Дешифровать',
                bg = '#3abf8d',
                selectcolor = 'lime',
                value = 1,
                variable = code_decode).place(x = 300, y = 120)

    Button(root,
           text = "Начать",
           bg = '#3abf8d',
           font = ("Console", 10),
           command = run).place(x = 450, y = 200)

    fraze = Entry(root,
                  textvariable = st,
                  width = 25,
                  bg = 'lime')
    fraze.place(x = 400, y = 150)

    label = Label(root,
                  text = '',
                  bg = '#3abf8d')
    label.place(x = 200, y = 190)
