from tkinter import *

w = Tk()
w.geometry('')
w.config(bg='black')
w.title('غلط')
def write():
    Label(w,text='غلط کردم',bg='black',fg='white',font='calibri 30').pack()

Button(w,text='دکمه غلط کردن',bd=70,font='calibri 100',bg='black',fg='white',command=write).pack()

w.mainloop()
