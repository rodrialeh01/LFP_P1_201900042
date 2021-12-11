import tkinter as tk
from tkinter import Button, scrolledtext, filedialog, messagebox
from tkinter import ttk
from tkinter import *
from tkinter import font

ventana = None
btnplay = None
btnstop = None
btnpause = None
btnprevious = None
btnnext = None


def VentanaReproductor():
    #VENTANA
    global ventana
    ventana = tk.Tk()
    ventana.title('T3 Musik Reproductor')
    ventana.geometry('1000x600')
    ventana.config(bg='gray')
    ventana.iconbitmap('icono.ico')
    ventana.resizable(0,0)

    #BOTON PLAY
    btnplay = Button(ventana,text='Play',fg='white',bg='#1B0A49',font='arial 15', height=2, width=15)
    btnplay.place(x=10,y=520)

    #BOTON STOP
    btnstop = Button(ventana,text='Stop',fg='white',bg='#1B0A49',font='arial 15', height=2, width=15)
    btnstop.place(x=210,y=520)

    #BOTON PAUSA
    btnpause = Button(ventana,text='Pause',fg='white',bg='#1B0A49',font='arial 15', height=2, width=15)
    btnpause.place(x=410,y=520)

    #BOTON PREVIOUS
    btnprevious = Button(ventana,text='Previous',fg='white',bg='#1B0A49',font='arial 15', height=2, width=15)
    btnprevious.place(x=610,y=520)

    #BOTON NEXT
    btnnext = Button(ventana,text='Next',fg='white',bg='#1B0A49',font='arial 15', height=2, width=15)
    btnnext.place(x=810,y=520)

    ventana.mainloop()