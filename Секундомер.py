import tkinter as tk
from datetime import datetime

second = 0
ident = ''

def start():
    global second, ident
    ident = stopwatch_label.after(1000, start)
    start_btn.pack_forget()
    stop_btn.pack(side="right", padx=25)
    second += 1
    stopwatch_label.configure(text=datetime.fromtimestamp(second).strftime("%M:%S"))

def stop():
    stopwatch_label.after_cancel(ident)
    stop_btn.pack_forget()
    reset_btn.pack(anchor='ne', padx=20, pady=10)
    cont_btn.pack(anchor='se', padx=20, pady=10)

def reset():
    global second
    second = 0
    stopwatch_label.configure(text='00:00')
    reset_btn.pack_forget()
    cont_btn.pack_forget()
    start_btn.pack(side="right", padx=25)

def contin():
    cont_btn.pack_forget()
    reset_btn.pack_forget()
    stop_btn.pack(side="right", padx=25)
    start()

win = tk.Tk()
win.title('Секундомер')
win.geometry("400x200")
win.resizable(False, False)

stopwatch_label = tk.Label(win, height=1, width=7, font=('Times New Roman', 35), text='00:00')
stopwatch_label.pack(side="left", padx=20)

start_btn = tk.Button(win, width=10, height=3, text='Старт', font=('Times New Roman', 17), command=start)
start_btn.pack(side="right", padx=25)

stop_btn = tk.Button(win, width=10, height=3, text='Стоп', font=('Times New Roman', 17), command=stop)

reset_btn = tk.Button(win, width=10, height=2, text='Сбросить', font=('Times New Roman', 17), command=reset)

cont_btn = tk.Button(win, width=10, height=2, text='Продолжить', font=('Times New Roman', 17), command=contin)

win.mainloop()
