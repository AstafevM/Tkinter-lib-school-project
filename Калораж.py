import tkinter as tk
import tkinter.ttk as ttk

genders = ['Ж', 'М']

lifestyles = ['сидячий', 'усл.активный', 'активный', 'спортив.', 'верх.без.планка']

def calculation():
    age = int(InputEntryAge.get())
    gender = InputEntryGender.get()
    height = float(InputEntryHeight.get())
    weight = float(InputEntryWeight.get())
    fat_percent = float(InputEntryFat.get())
    not_fat_percent = 1 - (fat_percent/100)

    sleep = float(InputEntrySleep.get())
    light_activity = float(InputEntryLightActivity.get())
    light_labor = float(InputEntryLightLabor.get())
    mid_heavy_labor = float(InputEntryMidHeavLabor.get())
    heavy_phys_labor = float(InputEntryHeavPhysLabor.get())
    very_heavy_phys_labor = float(InputEntryVeryHeavPhysLabor.get())

    osnovnoy_obmen = None
    obshiy_obmen = None
    proteins = None
    fats = None

    day_activity = [sleep, light_activity, light_labor, mid_heavy_labor, heavy_phys_labor, very_heavy_phys_labor]

    lean_mass = weight * not_fat_percent
    fat_mass = weight - lean_mass
    print(lean_mass, fat_mass)


    if gender == 'М':
        osnovnoy_obmen = 66.473+(13.7516*lean_mass)+(5.0033*height)-(6.755*age)
        fats = 1.2*lean_mass*0.7
    elif gender == 'Ж':
        osnovnoy_obmen = 655.0955 + (9.5634 * lean_mass) + (1.8496 * height) - (4.6756 * age)
        fats = 1.2 * lean_mass * 1

    print(int(osnovnoy_obmen))
    rashod_otdyha = osnovnoy_obmen/24
    print(rashod_otdyha)

    if sum(day_activity) == 24:
        obshiy_obmen=sleep*rashod_otdyha+1.4*light_activity*rashod_otdyha+1.6*light_labor*rashod_otdyha+1.9*mid_heavy_labor*rashod_otdyha+2.2*heavy_phys_labor*rashod_otdyha+2.5*very_heavy_phys_labor*rashod_otdyha+4.5*fat_mass
        print(int(obshiy_obmen))

    if InputEntryLifestyle.get() == 'сидячий':
        proteins = 1.1*lean_mass*0.8
    elif InputEntryLifestyle.get() == 'усл.активный':
        proteins = 1.1*lean_mass*1.2
    elif InputEntryLifestyle.get() == 'активный':
        proteins = 1.1*lean_mass*1.8
    elif InputEntryLifestyle.get() == 'спортив.':
        proteins = 1.1*lean_mass*2
    elif InputEntryLifestyle.get() == 'верх.без.планка':
        proteins = 1.1*lean_mass*2.5

    carbohydrates = (obshiy_obmen - proteins * 4.2 - fats * 9.29) / 3.9

    OutputEntryOsnovnoyObmen.delete(0, 'end')
    OutputEntryOsnovnoyObmen.insert(0, str(int(osnovnoy_obmen)))

    OutputEntryObshiyObmen.delete(0, 'end')
    OutputEntryObshiyObmen.insert(0, str(int(obshiy_obmen)))

    OutputEntryProtein.delete(0, 'end')
    OutputEntryProtein.insert(0, str(int(proteins)))

    OutputEntryFat.delete(0, 'end')
    OutputEntryFat.insert(0, str(int(fats)))

    OutputEntryCarbohydrat.delete(0, 'end')
    OutputEntryCarbohydrat.insert(0, str(int(carbohydrates)))

win = tk.Tk()
win.geometry("396x400+350+25")
win.title('Каллораж')
win.resizable(False, False)

InputFrame = ttk.Frame(win, relief='solid', borderwidth=5, width=50, height=50)
InputFrame.pack(anchor='nw', pady=6, padx=6)

InputLabel = tk.Label(win, text='Вводные данные')
InputLabel.place(x=148, y=-5)

InputFrameButton = ttk.Button(win, text='Рассчитать', command=calculation)
InputFrameButton.pack()
InputFrameLabel = tk.Label(InputFrame, text='')

InputLabelAge = tk.Label(InputFrame, text='Возраст', pady=5)
InputEntryAge = ttk.Entry(InputFrame, width=10)
InputLabelAge.grid(row=1, column=1)
InputEntryAge.grid(row=1, column=2)

InputLabelGender = tk.Label(InputFrame, text='Пол', pady=5)
InputEntryGender = ttk.Combobox(InputFrame, width=7, values=genders)
InputLabelGender.grid(row=2, column=1)
InputEntryGender.grid(row=2, column=2)

InputLabelHeight = tk.Label(InputFrame, text='Рост', pady=5)
InputEntryHeight = ttk.Entry(InputFrame, width=10)
InputLabelHeight.grid(row=3, column=1)
InputEntryHeight.grid(row=3, column=2)

InputLabelWeight = tk.Label(InputFrame, text='Вес', pady=5)
InputEntryWeight = ttk.Entry(InputFrame, width=10)
InputLabelWeight.grid(row=4, column=1)
InputEntryWeight.grid(row=4, column=2)

InputLabelFat = tk.Label(InputFrame, text='% жира', pady=5)
InputEntryFat = ttk.Entry(InputFrame, width=10)
InputLabelFat.grid(row=5, column=1)
InputEntryFat.grid(row=5, column=2)

InputLabelSleep = tk.Label(InputFrame, text='Сон (покой)', pady=5)
InputEntrySleep = ttk.Entry(InputFrame, width=10)
InputLabelSleep.grid(row=6, column=1)
InputEntrySleep.grid(row=6, column=2)

InputLabelLightActivity = tk.Label(InputFrame, text='Лёгкая активность\n(умств. труд)', padx=10)
InputEntryLightActivity = ttk.Entry(InputFrame, width=10)
InputLabelLightActivity.grid(row=1, column=3)
InputEntryLightActivity.grid(row=1, column=4)

InputLabelLightLabor = tk.Label(InputFrame, text='Лёгкий труд\n(водители, медсёстры)', padx=10)
InputEntryLightLabor = ttk.Entry(InputFrame, width=10)
InputLabelLightLabor.grid(row=2, column=3)
InputEntryLightLabor.grid(row=2, column=4)

InputLabelMidHeavLabor = tk.Label(InputFrame, text='Ср./тяж. труд\n(слесари, хирурги)', padx=10)
InputEntryMidHeavLabor = ttk.Entry(InputFrame, width=10)
InputLabelMidHeavLabor.grid(row=3, column=3)
InputEntryMidHeavLabor.grid(row=3, column=4)

InputLabelHeavPhysLabor = tk.Label(InputFrame, text='Тяж. физ. труд\n(строители и т.п.)', padx=10)
InputEntryHeavPhysLabor = ttk.Entry(InputFrame, width=10)
InputLabelHeavPhysLabor.grid(row=4, column=3)
InputEntryHeavPhysLabor.grid(row=4, column=4)

InputLabelVeryHeavPhysLabor = tk.Label(InputFrame, text='Особо тяж. физ. труд\n(каменщики, вальщ. леса)', padx=10)
InputEntryVeryHeavPhysLabor = ttk.Entry(InputFrame, width=10)
InputLabelVeryHeavPhysLabor.grid(row=5, column=3)
InputEntryVeryHeavPhysLabor.grid(row=5, column=4)

InputLabelLifestyle = tk.Label(InputFrame, text='Образ жизни:', pady=5)
InputEntryLifestyle = ttk.Combobox(InputFrame, width=7, values=lifestyles)
InputLabelLifestyle.grid(row=6, column=3)
InputEntryLifestyle.grid(row=6, column=4)

OutputFrame = ttk.Frame(win, width=25)
OutputFrame.pack(padx=6)

OutputLabelOsnovnoyObmen = tk.Label(OutputFrame, text='основной обмен:', pady=3)
OutputEntryOsnovnoyObmen = tk.Entry(OutputFrame, width=15)
OutputLabelOsnovnoyObmen.grid(row=1, column=1)
OutputEntryOsnovnoyObmen.grid(row=1, column=2)

OutputLabelObshiyObmen = tk.Label(OutputFrame, text='общий обмен:', pady=3)
OutputEntryObshiyObmen = tk.Entry(OutputFrame, width=15)
OutputLabelObshiyObmen.grid(row=2, column=1)
OutputEntryObshiyObmen.grid(row=2, column=2)

OutputLabelProtein = tk.Label(OutputFrame, text='белки:', pady=3)
OutputEntryProtein = tk.Entry(OutputFrame, width=15)
OutputLabelProtein.grid(row=3, column=1)
OutputEntryProtein.grid(row=3, column=2)

OutputLabelFat = tk.Label(OutputFrame, text='жиры:', pady=3)
OutputEntryFat = tk.Entry(OutputFrame, width=15)
OutputLabelFat.grid(row=4, column=1)
OutputEntryFat.grid(row=4, column=2)

OutputLabelCarbohydrat = tk.Label(OutputFrame, text='углеводы:', pady=3)
OutputEntryCarbohydrat = tk.Entry(OutputFrame, width=15)
OutputLabelCarbohydrat.grid(row=5, column=1)
OutputEntryCarbohydrat.grid(row=5, column=2)

win.mainloop()
