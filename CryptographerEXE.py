from tkinter import *
from tkinter import messagebox as mb


root = Tk()

root.title('Cryptographer!')
root['bg'] = '#3abf8d'
root.iconbitmap('1995724.ico') #_internal

root.geometry('550x250+600+300')
root.resizable(False, False)


eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbol = [" ", ",", ".", "!", "?"]
ru_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з',
               'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
               'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч',
               'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
en_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z']
en_morze = ['.-', '-...', '-.-.', '-..', '.', '..-.',
            '--.', '....', '..', '.---', '-.-', '.-..',
            '--', '-.', '---', '.--.', '--.-', '.-.',
            '...', '-', '..-', '...-', '.--', '-..-',
            '-.--', '--..']
en_morze_for_decoding = {'.-': 'A' or 'a', '-...': 'B' or 'b', '-.-.': 'C' or 'c', '-..': 'D' or 'd',
                         '.': 'E' or 'e', '..-.': 'F' or 'f', '--.': 'G' or 'g', '....': 'H' or 'h',
                         '..': 'I' or 'i', '.---': 'J' or 'j', '-.-': 'K' or 'k', '.-..': 'L' or 'l',
                         '--': 'M' or 'm', '-.': 'N' or 'n', '---': 'O' or 'o', '.--.': 'P' or 'p',
                         '--.-': 'Q' or 'q', '.-.': 'R' or 'r', '...': 'S' or 's', '-': 'T' or 't',
                         '..-': 'U' or 'u', '...-': 'V' or 'v', '.--': 'W' or 'w', '-..-': 'X' or 'x',
                         '-.--': 'Y' or 'y', '--..': 'Z' or 'z'}
ru_morze = ['.-', '-...', '.--', '--.', '-..', '.',
            '...-', '--..', '..', '.---', '-.-', '.-..',
            '--', '-.', '---', '.--.', '.-.', '...', '-',
            '..-', '..-.', '....', '-.-.', '---.', '----',
            '--.-', '.--.-.', '-.--', '-..-', '..-..',
            '..--', '.-.-']
ru_morze_for_decoding = {'.-': 'А' or 'а', '-...': 'Б' or 'б', '.--': 'В' or 'в', '--.': 'Г' or 'г',
                         '-..': 'Д' or 'д', '.': 'Е' or 'е', '...-': 'Ж' or 'ж', '--..': 'З' or 'з',
                         '..': 'И' or 'и', '.---': 'Й' or 'й', '-.-': 'К' or 'к', '.-..': 'Л' or 'л',
                         '--': 'М' or 'м', '-.': 'Н' or 'н', '---': 'О' or 'о', '.--.': 'П' or 'п',
                         '.-.': 'Р' or 'р', '...': 'С' or 'с', '-': 'Т' or 'т', '..-': 'У' or 'у',
                         '..-.': 'Ф' or 'ф', '....': 'Х' or 'х', '-.-.': 'Ц' or 'ц', '---.': 'Ч' or 'ч',
                         '----': 'Ш' or 'ш', '--.-': 'Щ' or 'щ', '.--.-.': 'Ъ' or 'ъ', '-.--': 'Ы' or 'ы',
                         '-..-': 'Ь' or 'ь', '..-..': 'Э' or 'э', '..--': 'Ю' or 'ю', '.-.-': 'Я' or 'я'}

global lagage
global code_decode
global fraze
global label

#-------------------------------------------------------------------------------

def pas():
    pass

def quit_game():
    answer = mb.askyesno('Quit', 'Do you want to quit?')
    if answer:
        root.destroy()

def replace_morz(l, fraza):
    itog = ''
    if l == 0:
        moch = 32
    if l == 1:
        moch = 26
    for i in range(len(fraza)):
        if fraza[i].isalpha():
            for j in range(moch):
                if moch == 32:
                    if fraza[i] == rus_upper_alphabet[j] or fraza[i] == rus_lower_alphabet[j]:
                        itog += ru_morze[(j + len(ru_morze)) % moch] + ' '
                        break
                if moch == 26:
                    if fraza[i] == eng_upper_alphabet[j] or fraza[i] == eng_lower_alphabet[j]:
                        itog += en_morze[(j + len(en_morze)) % moch] + ' '
                        break
        else:
            itog += fraza[i]
    s.configure(text = itog)

def decode_morz(lan, fraza):
    words = fraza.split('  ')
    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_letters = []
        if lan == 0:
            morse_dict = ru_morze_for_decoding
        else:
            morse_dict = en_morze_for_decoding
        for letter in letters:
            try:
                decoded_letter = morse_dict.get(letter, '')
                decoded_letters.append(decoded_letter)
            except KeyError:
                mb.showerror(title = "Ошибка",
                             message = "Язык не распознан!")
        decoded_word = ''.join(decoded_letters)
        decoded_words.append(decoded_word)
    s.configure(text = ' '.join(decoded_words).strip())

def start_replace():
    frz = str(string.get())
    lan = radio_btn_en_ru.get()
    coding = radio_btn_code_decode.get()
    if coding == 0:
        replace_morz(lan, frz)
    elif coding == 1:
        decode_morz(lan, frz)

def morze_run():
    new_root = Toplevel()
    
    new_root.title('Азбука морзе!')
    new_root['bg'] = '#14c887'
    new_root.iconbitmap('1995724.ico')
    
    new_root.geometry('600x300+600+300')
    new_root.resizable(False, False)

    global radio_btn_en_ru
    global radio_btn_code_decode
    global string
    global s
    global singl1
    
    radio_btn_en_ru = IntVar(value = 0)
    radio_btn_code_decode = IntVar(value = 0)

    Label(new_root,
          bg = '#14c887',
          text = 'Азбука морзе!',
          font = ('Console', 15, 'bold')).place(x = 220, y = 10)

    Radiobutton(new_root,
                text = 'Зашифровать',
                value = 0,
                variable = radio_btn_code_decode,
                bg = '#14c887',
                selectcolor = 'lime').place(x = 100, y = 100)

    Radiobutton(new_root,
                text = 'Дешифровать',
                value = 1,
                variable = radio_btn_code_decode,
                bg = '#14c887',
                selectcolor = 'lime').place(x = 100, y = 130)

    Radiobutton(new_root,
                text = 'Русский',
                value = 0,
                variable = radio_btn_en_ru,
                bg = '#14c887',
                selectcolor = 'lime').place(x = 230, y = 100)

    Radiobutton(new_root,
                text = 'Английский',
                value = 1,
                variable = radio_btn_en_ru,
                bg = '#14c887',
                selectcolor = 'lime').place(x = 230, y = 130)

    singl = StringVar(value = 'Введите фразу!')

    string = Entry(new_root,
                   bg = 'lime',
                   textvariable = singl)

    string.place(x = 350, y = 115)

    Button(new_root,
           bg = '#14c887',
           text = 'Начать',
           command = start_replace).place(x = 350, y = 200)

    s = Label(new_root,
              text = '',
              bg = '#14c887',
              font = ('Console', 10))

    s.place(x = 100, y = 200)

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
    label1.configure(text = itog)

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
    global label1
    
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

    label1 = Label(new_window,
                   bg = '#3abf8d',
                   text = '')

    label1.place(x = 150, y = 200)

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
                        try:
                            res += str(ru_alphabet.index(i)) + '-'
                        except ValueError:
                            mb.showerror(title = "Ошибка",
                                         message = f"Неизвесный символ {i}!")
                            break
                    else:
                        try:
                            res += i
                        except ValueError:
                            mb.showerror(title = "Ошибка",
                                         message = f"Неизвесный символ {i}!")
                            break
        else:
            for i in string:
                if i == ' ':
                    res = res[:-1] + ' '
                else:
                    if i not in symbol:
                        try:
                            res += str(en_alphabet.index(i)) + '-'
                        except ValueError:
                            mb.showerror(title = "Ошибка",
                                         message = f"Неизвесный символ {i}!")
                            break
                    else:
                        try:
                            res += i
                        except ValueError:
                            mb.showerror(title = "Ошибка",
                                         message = f"Неизвесный символ {i}!")
                            break
    else:
        string1 = string.split(' ')

        if lan == 0:
            for i in string1:
                j = i.split("-")
                temp = ''
                for k in j:
                    if k not in symbol:
                        if len(j) - 1 == len(temp):
                            try:
                                temp += ru_alphabet[int(k)]
                            except ValueError:
                                mb.showerror(title = "Ошибка",
                                             message = f"Невозможно перевести символ {i} в число!")
                                break
                            temp += ' '
                        else:
                            try:
                                temp += ru_alphabet[int(k)]
                            except ValueError:
                                mb.showerror(title = "Ошибка",
                                             message = f"Невозможно перевести символ {i} в число!")
                                break
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
                            try:
                                temp += en_alphabet[int(k)]
                            except ValueError:
                                mb.showerror(title = "Ошибка",
                                             message = f"Невозможно перевести символ {i} в число!")
                                break
                            temp += ' '
                        else:
                            try:
                                temp += en_alphabet[int(k)]
                            except ValueError:
                                mb.showerror(title = "Ошибка",
                                             message = f"Невозможно перевести символ {i} в число!")
                                break
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
#-------------------------------------------------------------------------------




Label(root,
      text = 'Каким шифром вы воспользуетесь?',
      bg = '#3abf8d',
      fg = 'black',
      font = ('Console', 15, 'bold')).pack(anchor = N, pady = 10)

Button(root,
       text = 'Цезаря',
       bg = '#3abf8d',
       fg = 'black',
       font = ('Console', 10),
       command = crun).place(anchor = W, x = 80, y = 80)

Button(root,
       text = 'Морзе',
       bg = '#3abf8d',
       font = ('Console', 10),
       command = morze_run).place(anchor = W, x = 150, y = 80)

Button(root,
       text = 'Шифр A1Z26',
       bg = '#3abf8d',
       font = ('Console', 10),
       command = a1z26_run).place(anchor = W, x = 215, y = 80)

Button(root,
       text = 'Выход',
       bg = '#3abf8d',
       font = ('Console', 10),
       command = quit_game).place(anchor = W, x = 480, y = 220)


root.mainloop()
