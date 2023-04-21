from tkinter import *
import random

running = True

def run():
    pictures = ['''
            +---+
                    |
                    |
                    |
                    |
                    |
             =========''', '''
            +---+
            |       |
                    |
                    |
                    |
                    |
             =========''', '''
            +---+
            |       |
           O      |
                    |
                    |
                    |
             =========''', '''
            +---+
            |       |
           O      |
            |       |
                    |
                    |
             =========''', '''
            +---+
            |       |
           O      |
          /|       |
                    |
                    |
             =========''', '''
            +---+
            |       |
            O      |
           /|\     |
                     |
                     |
             =========''', '''
            +---+
            |       |
            O      |
           /|\     |
           /        |
                    |
             =========''', '''
            +---+
            |       |
            O      |
           /|\      |
           / \      |
                     |
             =========''']
    picture_index = 0
    random_word = ('муравей', 'бабуин', 'барсук', 'медведь', 'бобр', 'верблюд', 'кошка', 'моллюск', 'кобра', 'пума',
                   'койот', 'ворона', 'олень', 'собака', 'осёл', 'утка', 'орёл', 'хорёк', 'лиса', 'лягушка', 'питон',
                   'кролик', 'баран', 'крыса', 'носорог', 'лосось', 'акула', 'змея',
                   'паук', 'аист', 'лебедь', 'тигр', 'жаба', 'форель', 'индейка', 'черепаха', 'ласка',
                   'кит', 'волк', 'вомбат', 'зебра')
    letters = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

    def reboot():
        win.destroy()

    def exit():
        global running
        running = False
        win.destroy()

    def game_start():
        secret_word = random.choice(random_word)
        print(secret_word)
        blanks = '*' * len(secret_word)
        entry1.delete(0, END)
        entry1.insert(0, blanks)
        return list(secret_word), blanks, secret_word

    def reply():
        nonlocal pictures
        nonlocal picture_index
        guess = entry2.get()
        index = -1
        if (guess == '') or (guess == ' ') or (len(guess) > 1) or (guess not in letters):
            entry2.delete(0, END)
        elif guess in entry3.get():
            entry2.delete(0, END)
            entry2.insert(0, f'буква "{guess}" уже была')
        else:
            if guess in return_list_secret_word:
                entry3.insert(0, f'{guess}(✓)  ')
                for i in return_list_secret_word:
                    index += 1
                    if guess == i:
                        entry1.delete(index)
                        entry1.insert(index, i)
                        entry2.delete(0, END)
                        if entry1.get() == return_secret_word:
                            entry2.delete(0, END)
                            entry2.insert(0, 'победа (☞⌐▀͡ ͜ʖ͡▀ )☞')
            else:
                entry3.insert(0, f'{guess}(✗)  ')
                picture_index += 1
                entry2.delete(0, END)
                Label(win, height=7, width=20, text=f'{pictures[picture_index]}').grid(row=3, column=1, columnspan=4, sticky='we')
                if picture_index == 7:
                    entry2.delete(0, END)
                    entry2.insert(0, 'вы проиграли(')
                    entry1.delete(0, END)
                    entry1.insert(0, f'правильное слово: {return_secret_word}')

    win = Tk()
    win.geometry('505x185+500+250')
    win.title('Виселица')
    win.resizable(False, False)

    Button(win, height=1, width=5, text='↻', command=reboot).grid(row=1, column=3)
    Button(win, height=1, width=5, text='exit', command=exit).grid(row=1, column=4)
    Button(win, height=1, width=5, text='=>', command=reply).grid(row=2, column=3)

    Label(win, height=1, width=15, text='загаданное слово:').grid(row=1, column=1)
    Label(win, height=1, width=15, text='ответ:').grid(row=2, column=1)
    Label(win, height=1, width=15, text='уже использовано:').grid(row=4, column=1)
    Label(win, height=7, width=20, text=f'{pictures[0]}').grid(row=3, column=1, columnspan=4, sticky='we')

    entry1 = Entry(win, width=50)
    entry2 = Entry(win, width=50)
    entry3 = Entry(win, width=50)

    entry1.grid(row=1, column=2)
    entry2.grid(row=2, column=2)
    entry3.grid(row=4, column=2)

    return_list_secret_word, return_blanks, return_secret_word = game_start()

    win.mainloop()

while running:
    run()
