import tkinter.ttk as ttk
import tkinter as tk
import random
import sys

print('ЛКМ - открыть кнопку\nПКМ - поставить флажок')

def run():
    class ModdedButton(tk.Button):
        def __init__(self, master, row, column, number=0, *args, **kwargs):
            super().__init__(master, *args, **kwargs)
            self.row = row
            self.column = column
            self.number = number
            self.is_bomb = False
            self.count_bomb = 0
            self.master = master
            self.open = False

    class Game:
        ID = None
        timer = -1
        flags = 40
        colors_for = {1: '#0083FF', 2: '#32FF00', 3: '#FF0000', 4: '#AE00FF', 5: '#FFAE00', 6: '#FF0078', 0: '#E2E8E2'}
        def __init__(self):
            self.all_buttons = []
            for row in range(1, 19):
                row_all_buttons = []
                for column in range(1, 17):
                    self.button = ModdedButton(Game.frame, height=1, width=2, row=row, column=column, bg='#B0B9AF')
                    self.button.configure(command=lambda bttn=self.button: self.clicking(bttn))
                    self.button.bind('<Button-3>', self.put_flag)
                    self.button.grid(row=row, column=column)
                    row_all_buttons.append(self.button)
                self.all_buttons.append(row_all_buttons)

        def put_flag(self, event):
            current = event.widget
            if current['state'] == 'normal':
                if not self.flags == 0:
                    self.flags -= 1
                    self.flag_label.configure(text=f'Флажки: {self.flags}')
                    current.config(state = 'disabled', text = '⚑', disabledforeground = 'red')
            elif current['text'] == '⚑':
                self.flags += 1
                self.flag_label.configure(text=f'Флажки: {self.flags}')
                current.config(text = '', state = 'normal')

        def print_buttons(self):
            btn_with_bomb = 0
            clean_btn = 0
            for row in range(1, 17):
                row_list = []
                for col in range(1, 15):
                    butt = self.all_buttons[row][col]
                    if butt.is_bomb:
                        btn_with_bomb += 1
                        butt = '*'
                    else:
                        clean_btn += 1
                        butt = str(butt.count_bomb)
                    row_list.append(butt)
                print(''.join(row_list))
            print('\n')

        @staticmethod
        def bombs_cords():
            s = [i for i in range(1, 225)]
            random.shuffle(s)
            return s[:40]

        def insert_bombs(self):
            bomb_indexes = self.bombs_cords()
            count = 1
            for ROW in range(1, 17):
                for COLUMN in range(1, 15):
                    btn = self.all_buttons[ROW][COLUMN]
                    btn.number = count
                    if btn.number in bomb_indexes:
                        btn.is_bomb = True
                    count += 1

        def count_bomb(self):
            for ROW in range(1, 17):
                for COLUMN in range(1, 15):
                    btn = self.all_buttons[ROW][COLUMN]
                    count_bomb = 0
                    if not btn.is_bomb:
                        for row_dx in -1, 0, 1:
                            for col_dx in -1, 0, 1:
                                neighbour = self.all_buttons[ROW + row_dx][COLUMN + col_dx]
                                if neighbour.is_bomb:
                                    count_bomb += 1
                    btn.count_bomb = count_bomb

        def clicking(self, clicked_button: ModdedButton):
            if clicked_button.is_bomb:
                self.win.after_cancel(self.ID)
                clicked_button.open = True
                clicked_button.configure(text='*', background='red', disabledforeground='black')
                for i in self.all_buttons:
                    for bttn in i:
                        bttn.configure(state='disabled')
                        if bttn.is_bomb:
                            bttn.configure(text='*', background='red', disabledforeground='black')
            else:
                clicked_button.open = True
                self.bfs(clicked_button)
            self.winning()

        def bfs(self, button: ModdedButton):
            queue = [button]
            while queue:
                current = queue.pop()
                color = current.count_bomb
                current.config(text=current.count_bomb, state='disabled', bg='#E2E8E2', font=('Arial Black', 8), disabledforeground=Game.colors_for[color], relief='flat', borderwidth=1)
                current.open = True
                if current.count_bomb==0:
                    row, col = current.row, current.column
                    for row_sear in -1, 0, 1:
                        for col_sear in -1, 0, 1:
                            next_btn = self.all_buttons[(row-1) + row_sear][(col-1) + col_sear]
                            if (next_btn.open==False) and (2<=next_btn.row<=17) and (2<=next_btn.column<=15) and (next_btn not in queue) and (not next_btn.is_bomb) and (not next_btn['text'] == '⚑'):
                                queue.append(next_btn)

        def stopwatch(self):
            self.ID = self.win.after(1000, self.stopwatch)
            self.timer += 1
            self.time_label.configure(text=f'Время: {self.timer}')

        def winning(self):
            cnt = 0
            for row in self.all_buttons:
                for btn in row:
                    if btn.open:
                        cnt += 1
            if cnt == 184:
                self.win.after_cancel(self.ID)
                for r in self.all_buttons:
                    for c in r:
                        if c.is_bomb:
                            c.config(bg='green', text='')
                        else:
                            c.configure(activebackground='green', text='gg')
                        c.configure(state = 'disabled')

        win = tk.Tk()
        win.geometry('337x533+450+50')
        win.configure(bg='white')
        win.resizable(False, False)
        win.title('Сапёр')

        frame = ttk.Frame()
        frame.place(x=-23, y=93)

        rebot = ttk.Button(win, width=6, text='↻', command=lambda: Game.win.destroy())
        rebot.place(x=0, y=0)

        exit = ttk.Button(win, width=7, text='выход', command=lambda: sys.exit())
        exit.place(x=286, y=0)

        frame2 = ttk.Frame()
        frame2.place(x=0, y=25)
        tk.Label(frame2, height=6, width=50, pady=-5).pack()
        time_label = tk.Label(frame2, height=1, width=10, font=('Comic Sans MS', 14))
        time_label.place(x=25, y=28)

        flag_label = tk.Label(frame2, height=1, width=10, text='Флажки: 40', font=('Comic Sans MS', 14))
        flag_label.place(x=180, y=28)

        def start(self):
            self.insert_bombs()
            self.count_bomb()
            self.print_buttons()
            self.stopwatch()
            self.win.mainloop()

    Game().start()

while True:
    run()