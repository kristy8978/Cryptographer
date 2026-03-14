from tkinter import *
from tkinter import messagebox as mb
from Cezery import crun as cezrun
from morze import morze_run as morrun
from A1Z26 import a1z26_run as azrun


root = Tk()

root.title('Cryptographer!')
root['bg'] = '#3abf8d'
root.iconbitmap('1995724.ico') #_internal

root.geometry('550x250+600+300')
root.resizable(False, False)


def pas():
    pass

def quit_game():
    answer = mb.askyesno('Quit', 'Do you want to quit?')
    if answer:
        root.destroy()


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
       command = cezrun).place(anchor = W, x = 80, y = 80)

Button(root,
       text = 'Морзе',
       bg = '#3abf8d',
       font = ('Console', 10),
       command = morrun).place(anchor = W, x = 150, y = 80)

Button(root,
       text = 'Шифр A1Z26',
       bg = '#3abf8d',
       font = ('Console', 10),
       command = azrun).place(anchor = W, x = 215, y = 80)

Button(root,
       text = 'Выход',
       bg = '#3abf8d',
       font = ('Console', 10),
       command = quit_game).place(anchor = W, x = 480, y = 220)


root.mainloop()
