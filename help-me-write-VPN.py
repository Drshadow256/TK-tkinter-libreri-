from tkinter import *
import os
from time import sleep
w = Tk()
w.title('VPN')
w.resizable(0, 0)
w.geometry('900x900')
w.config(bg='black')



def mo():

    sleep(7)
    lm = Label(w,text='       ',fg='white',bg='black',font='calibri 20')
    lm.place(x=390, y=700)

#اینجا نمی دانم باید چه کار کرد ولی شما می توانید از پوسته ای که من ساختم  برای خودتان استفاده کنید
#برای بار اول کلیک شد mo اجرا شود
#if  ???????:
#    i == mo 
#دوباره کلیک شد mo2اجرا شود
#else :
#    i == mo2

Label(w,text='welcom',bg='black',fg='white',font='calibri 50').pack()


Label(w,text='Click the button below to connect.',bg='black',fg='white',font='calibri 20').pack()


cb = Button(w,text='conect',bd='80',bg='black',fg='white',font='calibri 100',command=mo)
cb.place(x=160, y=200)

lm = Label(w,text='Not connected',fg='white',bg='black',font='calibri 20')
lm.place(x=390, y=700)

Label(w,text='progamer : masod shayegh (09300696438)',fg='white',bg='black').pack(side='bottom', fill='x', pady=10)
w.mainloop()
