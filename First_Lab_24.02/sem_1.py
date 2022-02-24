from random import *
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

def clicked():
    
    active = 0
    active += int(textInputCash.get())
    active += int(textInputOS.get())
    active += int(textInputRS.get())
    active += int(textInputDZ.get())
    active += int(textInputGoods.get())
    textViewActive.configure(text=f'Актив = {active}') 



    passive = 0
    passive += int(textInputKZ.get())
    passive += int(textInputProfit.get())
    passive += int(textInputYK.get())
    passive += int(textInputRK.get())
    textViewPassive.configure(text=f'Пассив = {passive}') 

    if active == passive:
        messagebox.showinfo('Заголовок', 'Балан соблюден')
    else:
        messagebox.showinfo('Заголовок', 'Балан не соблюден')









window = Tk() # creating of window 

window.geometry('1000x600')

window.title("Добро пожаловать в приложение ABOBA")



# comboCash = Combobox(window)  
# comboCash['values'] = (1, 2, 3, 4, 5)  
# comboCash.current(2) 
# comboCash.grid(column=0, row=0)



# numCash = comboCash.get()
# CashCounter = 2
# for i in range (int(numCash)):
    
#     textInputCash = (Entry(window,width=10)) #              input for Cash
#     textInputCash.grid(column = 0, row = CashCounter) #     widget display with grid
#     textInputCash.index(CashCounter)
#     CashCounter += 1
# window.update()



textViewCash = Label(window, text="Касса") #    widget of textView              View Cash
textViewCash.grid(column = 0, row = 1) #        widget display with grid
textInputCash = (Entry(window,width=10)) #                                      input for Cash
textInputCash.grid(column = 0, row = 2) #       widget display with grid

textViewOS = Label(window, text="О/С") #                                widget of textView              View О/С
textViewOS.grid(column = 1, row = 1) #                                  widget display with grid
textInputOS = (Entry(window,width=10)) #                                                                input for О/С
textInputOS.grid(column = 1, row = 2) #                                 widget display with grid

textViewRS = Label(window, text="Р/С") #                                widget of textView              View Р/С
textViewRS.grid(column = 2, row = 1) #                                  widget display with grid
textInputRS = (Entry(window,width=10)) #                                                                input for Р/С
textInputRS.grid(column = 2, row = 2) #                                 widget display with grid

textViewKZ = Label(window, text="КредЗадолж") #                         widget of textView              View КЗ
textViewKZ.grid(column = 3, row = 1) #                                  widget display with grid
textInputKZ = (Entry(window,width=10)) #                                                                input for КЗ
textInputKZ.grid(column = 3, row = 2) #                                 widget display with grid

textViewDZ = Label(window, text="ДебЗадолж") #                          widget of textView              View БЗ
textViewDZ.grid(column = 4, row = 1) #                                  widget display with grid
textInputDZ = (Entry(window,width=10)) #                                                                input for БЗ
textInputDZ.grid(column = 4, row = 2) #                                 widget display with grid

textViewGoods = Label(window, text="Товары") #                          widget of textView              View Товары
textViewGoods.grid(column = 5, row = 1) #                               widget display with grid
textInputGoods = (Entry(window,width=10)) #                                                             input for Товары
textInputGoods.grid(column = 5, row = 2) #                              widget display with grid

textViewProfit = Label(window, text="Прибыль") #                        widget of textView              View Прибыль
textViewProfit.grid(column = 6, row = 1) #                              widget display with grid
textInputProfit = (Entry(window,width=10)) #                                                            input for Прибыль
textInputProfit.grid(column = 6, row = 2) #                             widget display with grid

textViewYK = Label(window, text="У/К") #                                widget of textView              View У/К
textViewYK.grid(column = 7, row = 1) #                                  widget display with grid
textInputYK = (Entry(window,width=10)) #                                                                input for У/К
textInputYK.grid(column = 7, row = 2) #                                 widget display with grid

textViewRK = Label(window, text="Р/К") #                                widget of textView              View Р/К
textViewRK.grid(column = 8, row = 1) #                                  widget display with grid
textInputRK = (Entry(window,width=10)) #                                                                input for Р/К
textInputRK.grid(column = 8, row = 2) #                                 widget display with grid







btn = Button(window, text="Подтвердить", command=clicked) # widget if button
btn.grid(column=0, row=7) # widget display with grid






textViewActive = Label(window, text="Актив") # widget of textView
textViewActive.grid(column = 0, row = 8) # widget display with grid

textViewPassive = Label(window, text="Пассив") # widget of textView
textViewPassive.grid(column = 1, row = 8) # widget display with grid






window.mainloop() # creating an app in an endless loop