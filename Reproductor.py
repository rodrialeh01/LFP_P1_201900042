import tkinter as tk
from tkinter import Button, scrolledtext, filedialog, messagebox
from tkinter import ttk
from tkinter import *
from tkinter import font
import time
from PIL import Image, ImageTk, ImageSequence

ventana = None
btnplay = None
btnstop = None
btnpause = None
btnprevious = None
btnnext = None
cuadroInfo = None
cuadrocanciones = None
labeli = None

def mostrargif():
    global labeli
    global ventana
    img = Image.open('fondo.gif')
    labeli = Label(ventana)
    labeli.place(x=10,y=200)
    for img in ImageSequence.Iterator(img):
        img = img.resize((720,300))
        img = ImageTk.PhotoImage(img)
        labeli.config(image= img)
        ventana.update()
        time.sleep(0.01)
    ventana.after(0,mostrargif)

def VentanaReproductor(nombrelista, listac):
    #VENTANA
    global ventana
    ventana = tk.Tk()
    ventana.title('T3 Musik Reproductor de la lista ' + nombrelista)
    ventana.geometry('1000x600')
    ventana.config(bg='black')
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

    #CUADRO DE TEXTO DE LA INFORMACION DE LA CANCION
    cuadroInfo = scrolledtext.ScrolledText(ventana, bg="black", fg="white", width=100, height=10,font=("arial",10))
    cuadroInfo.place(x=10, y=10)

    #CUADRO DE TEXTO DE LAS CANCIONES CARGADAS AL REPRODUCTOR
    cuadrocanciones = scrolledtext.ScrolledText(ventana, bg="black",fg="green", width=30, height=30,font=("arial",10))
    cuadrocanciones.place(x=750, y=10)

    #IMAGEN PUESTA EN LA VENTANA:
    mostrargif()
    for i in range(len(listac)):
        print('Nombre: ' + str(listac[i].getNombre()))
        print('Artista: ' + str(listac[i].getArtista()))
        print('Ruta: ' + str(listac[i].getRuta()))
        print('Genero: ' + str(listac[i].getGenero()))
        print('Repetir: ' + str(listac[i].getRepetir()))
        print('Año: ' + str(listac[i].getAnio()))
        print()

    ventana.mainloop()