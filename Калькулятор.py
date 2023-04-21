from tkinter import *


def insert0():
    entry1.insert(1110, '0')


def insert1():
    entry1.insert(1110, '1')


def insert2():
    entry1.insert(1110, '2')


def insert3():
    entry1.insert(1110, '3')


def insert4():
    entry1.insert(1110, '4')


def insert5():
    entry1.insert(1110, '5')


def insert6():
    entry1.insert(1110, '6')


def insert7():
    entry1.insert(1110, '7')


def insert8():
    entry1.insert(1110, '8')


def insert9():
    entry1.insert(1110, '9')


def insert_div():
    entry1.insert(1110, '/')


def insert_mul():
    entry1.insert(10000, '*')


def insert_pls():
    entry1.insert(10000, '+')


def insert_min():
    entry1.insert(1000, '-')


def insert_dot():
    entry1.insert(1000, '.')


def clean():
    entry1.delete(0, END)


def all_clean():
    entry1.delete(0, END)
    entry2.delete(0, END)


def insert_rbrack():
    entry1.insert(1110, ')')


def insert_lbrack():
    entry1.insert(1110, '(')


def result():
    if '/0' in entry1.get() and not'/0.' in entry1.get():
        entry2.delete(0, END)
        entry2.insert(0, 'ОШИБКА: деление на ноль')
    else:
        entry2.delete(0, END)
        entry2.insert(0, str(eval(entry1.get())))


win = Tk()
win.title('Калькулятор')
win.geometry("265x585")
win.resizable(False, False)
win.config(bg='black')
win.iconphoto(False, PhotoImage(file='калькулятор.png'))

entry1 = Entry(win, width=45, justify='right', bg='black', fg='white')
entry1.pack()

entry2 = Entry(win, width=45, justify='right', bg='black', fg='white')
entry2.pack()

Button(win, height=5, width=8, text='0', command=insert0).place(x=66, y=499)
Button(win, height=5, width=8, text='1', command=insert1).place(x=0, y=413)
Button(win, height=5, width=8, text='2', command=insert2).place(x=66, y=413)
Button(win, height=5, width=8, text='3', command=insert3).place(x=132, y=413)
Button(win, height=5, width=8, text='4', command=insert4).place(x=0, y=327)
Button(win, height=5, width=8, text='5', command=insert5).place(x=66, y=327)
Button(win, height=5, width=8, text='6', command=insert6).place(x=132, y=327)
Button(win, height=5, width=8, text='7', command=insert7).place(x=0, y=241)
Button(win, height=5, width=8, text='8', command=insert8).place(x=66, y=241)
Button(win, height=5, width=8, text='9', command=insert9).place(x=132, y=241)

Button(win, height=5, width=8, text='=', bg='blue', activebackground='blue', command=result).place(x=198, y=499)

Button(win, height=5, width=8, text='+', bg='orange', activebackground='orange', command=insert_pls).place(x=198, y=413)
Button(win, height=5, width=8, text='-', bg='orange', activebackground='orange', command=insert_min).place(x=198, y=327)
Button(win, height=5, width=8, text='/', bg='orange', activebackground='orange', command=insert_div).place(x=198, y=241)
Button(win, height=5, width=8, text='*', bg='orange', activebackground='orange', command=insert_mul).place(x=198, y=155)

Button(win, height=5, width=8, text='.', command=insert_dot).place(x=0, y=155)
Button(win, height=5, width=8, text='(', command=insert_lbrack).place(x=66, y=155)
Button(win, height=5, width=8, text=')', command=insert_rbrack).place(x=132, y=155)

Button(win, height=5, width=8, text='C', bg='red', activebackground='red', command=clean).place(x=0, y=499)
Button(win, height=5, width=8, text='AC', bg='red', activebackground='red', command=all_clean).place(x=132, y=499)

win.mainloop()
