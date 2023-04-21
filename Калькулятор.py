from tkinter import *

def clean():
    entry1.delete(0, END)


def all_clean():
    entry1.delete(0, END)
    entry2.delete(0, END)

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

entry1 = Entry(win, width=45, justify='right', bg='black', fg='white')
entry1.pack()

entry2 = Entry(win, width=45, justify='right', bg='black', fg='white')
entry2.pack()

Button(win, height=5, width=8, text='0', command=lambda: entry1.insert(1110, '0')).place(x=66, y=499)
Button(win, height=5, width=8, text='1', command=lambda: entry1.insert(1110, '1')).place(x=0, y=413)
Button(win, height=5, width=8, text='2', command=lambda: entry1.insert(1110, '2')).place(x=66, y=413)
Button(win, height=5, width=8, text='3', command=lambda: entry1.insert(1110, '3')).place(x=132, y=413)
Button(win, height=5, width=8, text='4', command=lambda: entry1.insert(1110, '4')).place(x=0, y=327)
Button(win, height=5, width=8, text='5', command=lambda: entry1.insert(1110, '5')).place(x=66, y=327)
Button(win, height=5, width=8, text='6', command=lambda: entry1.insert(1110, '6')).place(x=132, y=327)
Button(win, height=5, width=8, text='7', command=lambda: entry1.insert(1110, '7')).place(x=0, y=241)
Button(win, height=5, width=8, text='8', command=lambda: entry1.insert(1110, '8')).place(x=66, y=241)
Button(win, height=5, width=8, text='9', command=lambda: entry1.insert(1110, '9')).place(x=132, y=241)

Button(win, height=5, width=8, text='+', bg='orange', activebackground='orange', command=lambda: entry1.insert(10000, '+')).place(x=198, y=413)
Button(win, height=5, width=8, text='-', bg='orange', activebackground='orange', command=lambda: entry1.insert(10000, '-')).place(x=198, y=327)
Button(win, height=5, width=8, text='/', bg='orange', activebackground='orange', command=lambda: entry1.insert(10000, '/')).place(x=198, y=241)
Button(win, height=5, width=8, text='*', bg='orange', activebackground='orange', command=lambda: entry1.insert(10000, '*')).place(x=198, y=155)

Button(win, height=5, width=8, text='.', command=lambda: entry1.insert(10000, '.')).place(x=0, y=155)
Button(win, height=5, width=8, text='(', command=lambda: entry1.insert(10000, '(')).place(x=66, y=155)
Button(win, height=5, width=8, text=')', command=lambda: entry1.insert(10000, ')')).place(x=132, y=155)

Button(win, height=5, width=8, text='C', bg='red', activebackground='red', command=clean).place(x=0, y=499)
Button(win, height=5, width=8, text='AC', bg='red', activebackground='red', command=all_clean).place(x=132, y=499)
Button(win, height=5, width=8, text='=', bg='blue', activebackground='blue', command=result).place(x=198, y=499)

win.mainloop()
