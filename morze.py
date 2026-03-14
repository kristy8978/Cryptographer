from tkinter import *
from tkinter import messagebox as mb


eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
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
#-------------------------------------------------------------------------------
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
                pass
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
#-------------------------------------------------------------------------------
