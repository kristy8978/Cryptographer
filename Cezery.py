from tkinter import *
from tkinter import messagebox as mb


eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbol = [" ", ",", ".", "!", "?"]


#-------------------------------------------------------------------------------
def shifr(chifr, n, l, fraza):
    itog = ''
    if l == 0:
        moch = 32
    if l == 1:
        moch = 26
    if chifr == 1:
        n = -n
    for i in range(len(fraza)):
        if fraza[i].isalpha():
            if fraza[i] == fraza[i].upper():
                for j in range(moch):
                    if moch == 32:
                        if fraza[i] == rus_upper_alphabet[j]:
                            itog += rus_upper_alphabet[(j + n) % moch]
                            break
                    if moch == 26:
                        if fraza[i] == eng_upper_alphabet[j]:
                            itog += eng_upper_alphabet[(j + n) % moch]
                            break
            elif fraza[i] == fraza[i].lower():
                for j in range (moch):
                    if moch == 32:
                        if fraza[i] == rus_lower_alphabet[j]:
                           itog += rus_lower_alphabet[(j + n) % moch]
                           break
                    if moch == 26:
                        if fraza[i] == eng_lower_alphabet[j]:
                           itog += eng_lower_alphabet[(j + n) % moch]
                           break
        else:
            itog += fraza[i]
    label.configure(text = itog)

def start_code():
    code = radio_btn_code_decode.get()
    steps = int(step.get())
    ru_en = radio_btn_en_ru.get()
    fraz = str(string.get())
    shifr(code, steps, ru_en, fraz)

def crun():
    new_window = Toplevel()
    
    new_window.title('Шифр цезаря!')
    
    new_window.geometry('600x300+600+300')
    new_window.resizable(False, False)
    
    new_window.iconbitmap('1995724.ico')
    new_window['bg'] = '#3abf8d'

    global radio_btn_en_ru
    global radio_btn_code_decode
    global step
    global string
    global label
    
    radio_btn_code_decode = IntVar(value = 0)
    radio_btn_en_ru = IntVar(value = 0)
    txt = StringVar(value = 'Введите шаг перемещения!')
    txt1 = StringVar(value = 'Введите фразу!')
    
    Label(new_window,
          text = "Шифр цезаря!",
          bg = '#3abf8d',
          font = ('Console', 15, 'bold')).pack(pady = 20)

    Radiobutton(new_window,
                text = 'Зашифровать',
                value = 0,
                variable = radio_btn_code_decode,
                bg = '#3abf8d',
                selectcolor = 'lime').place(x = 100, y = 100)

    Radiobutton(new_window,
                text = 'Дешифровать',
                value = 1,
                variable = radio_btn_code_decode,
                bg = '#3abf8d',
                selectcolor = 'lime').place(x = 100, y = 130)

    Radiobutton(new_window,
                text = 'Русский',
                value = 0,
                variable = radio_btn_en_ru,
                bg = '#3abf8d',
                selectcolor = 'lime').place(x = 230, y = 100)

    Radiobutton(new_window,
                text = 'Английский',
                value = 1,
                variable = radio_btn_en_ru,
                bg = '#3abf8d',
                selectcolor = 'lime').place(x = 230, y = 130)
    
    step = Entry(new_window,
                 width = 30,
                 bg = 'lime',
                 textvariable = txt)

    step.place(x = 370, y = 100)

    string = Entry(new_window,
                 width = 30,
                 bg = 'lime',
                 textvariable = txt1)

    string.place(x = 370, y = 130)

    Button(new_window,
           text = 'Начать',
           bg = '#3abf8d',
           command = start_code).place(x = 370, y = 200)

    label = Label(new_window,
                  bg = '#3abf8d',
                  text = '')

    label.place(x = 150, y = 200)
#-------------------------------------------------------------------------------
