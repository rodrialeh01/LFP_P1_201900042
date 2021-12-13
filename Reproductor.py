#---------------------------IMPORTANDO LIBRERIAS------------------------------
#tkinter
import tkinter as tk
from tkinter import Button, scrolledtext
from tkinter import ttk
from tkinter import *
from tkinter import font
import time
from tkinter import filedialog
from typing import Literal
#PIL
from PIL import Image, ImageTk, ImageSequence
#Pygame
import pygame

#-----------------------------------VARIABLES GLOBALES------------------------------
listaCanciones = []
ventana = None
btnplay = None
btnstop = None
btnpause = None
btnprevious = None
btnnext = None
cuadroInfo = None
cuadrocanciones = None
labeli = None
pygame.mixer.init()

#METODO PARA MOSTRAR EL GIF EN LA VENTANA
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

#METODO QUE MUESTRA EL LISTADO DE CANCIONES DEL REPRODUCTOR
def cuadroc(ventana):
    global listaCanciones
    global cuadrocanciones

    cuadrocanciones = Listbox(ventana, bg="black",fg="green", width=25, height=26,font=("arial",12))
    cuadrocanciones.place(x=750, y=10)

    for i in range(len(listaCanciones)):
        cuadrocanciones.insert(END,listaCanciones[i].getNombre())

#METODO PARA REPRODUCIR LA CANCION:
def reproducir():
    global cuadrocanciones
    global cuadroInfo
    cancion = cuadrocanciones.get(ACTIVE)
    #print(str(act))
    cancion = rutac(cancion)

    cuadroInfo.delete(1.0,END)
    cuadroInfo.insert(tk.INSERT, 'Nombre: ' + objcancion(cancion).getNombre() + '\nArtista: ' + objcancion(cancion).getArtista() + '\nRuta: ' + objcancion(cancion).getRuta() + '\nGenero: ' + objcancion(cancion).getGenero() + '\nAño de Lanzamiento: ' + objcancion(cancion).getAnio() + '\n\nLa canción que se esta reproduciendo actualmente se repetirá ' + objcancion(cancion).getRepetir() + ' veces')

    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play(loops=int(objcancion(cancion).getRepetir()))

#METODO PARA PARAR LA CANCION
def parar():
    global cuadrocanciones
    global cuadroInfo
    pygame.mixer.music.stop()
    cuadrocanciones.selection_clear(ACTIVE)
    cuadroInfo.delete(1.0,END)

#VARIABLE GLOBAL COMO BANDERA PARA CONTROLAR LA PAUSA
pausado = False

#METODO PARA PAUSAR LA CANCION
def pausar(p):
    global pausado
    global btnpause
    pausado = p
    if pausado == True:
        pygame.mixer.music.unpause()
        pausado = False
    else:
        pygame.mixer.music.pause()
        pausado = True

#METODO PARA PASAR A LA SIGUIENTE CANCION
def siguientec():
    global cuadrocanciones
    global cuadroInfo
    s = cuadrocanciones.curselection()
    s = s[0]+1
    cancions = cuadrocanciones.get(s)
    cancions = rutac(cancions)
    cuadroInfo.delete(1.0,END)
    cuadroInfo.insert(tk.INSERT, 'Nombre: ' + objcancion(cancions).getNombre() + '\nArtista: ' + objcancion(cancions).getArtista() + '\nRuta: ' + objcancion(cancions).getRuta() + '\nGenero: ' + objcancion(cancions).getGenero() + '\nAño de Lanzamiento: ' + objcancion(cancions).getAnio() + '\n\nLa canción que se esta reproduciendo actualmente se repetirá ' + objcancion(cancions).getRepetir() + ' veces')

    pygame.mixer.music.load(cancions)
    pygame.mixer.music.play(loops=int(objcancion(cancions).getRepetir()))

    cuadrocanciones.selection_clear(0,END)
    cuadrocanciones.activate(s)
    cuadrocanciones.selection_set(s, last=None)

#METODO PARA PASAR A LA CANCION ANTERIOR
def anteriorc():
    global cuadrocanciones
    global cuadroInfo
    a = cuadrocanciones.curselection()
    a = a[0]-1
    cancions = cuadrocanciones.get(a)
    cancions = rutac(cancions)
    cuadroInfo.delete(1.0,END)
    cuadroInfo.insert(tk.INSERT, 'Nombre: ' + objcancion(cancions).getNombre() + '\nArtista: ' + objcancion(cancions).getArtista() + '\nRuta: ' + objcancion(cancions).getRuta() + '\nGenero: ' + objcancion(cancions).getGenero() + '\nAño de Lanzamiento: ' + objcancion(cancions).getAnio() + '\n\nLa canción que se esta reproduciendo actualmente se repetirá ' + objcancion(cancions).getRepetir() + ' veces')

    pygame.mixer.music.load(cancions)
    pygame.mixer.music.play(loops=int(objcancion(cancions).getRepetir()))

    cuadrocanciones.selection_clear(0,END)
    cuadrocanciones.activate(a)
    cuadrocanciones.selection_set(a, last=None)

#METODO PARA MOSTRAR LA VENTANA DEL REPRODUCTOR
def VentanaReproductor(nombrelista, listac):
    #AÑADE LA LISTA INGRESADA A LA LISTA GLOBAL
    global listaCanciones
    for c in listac:
        listaCanciones.append(c)

    #VENTANA
    global ventana
    global cuadrocanciones
    global cuadroInfo
    global btnpause
    ventana = tk.Tk()
    ventana.title('T3 Musik - Reproduciendo la lista: ' + nombrelista)
    ventana.geometry('1000x600')
    ventana.config(bg='black')
    ventana.iconbitmap('icono.ico')
    ventana.resizable(0,0)

    #LLAMA AL APARTADO DONDE APARECE LA LISTA DE CANCIONES
    cuadroc(ventana)

    #BOTON PLAY
    btnplay = Button(ventana,text='Reproducir',fg='black',bg='gray',font='arial 15', height=2, width=15, command=reproducir)
    btnplay.place(x=10,y=520)

    #BOTON STOP
    btnstop = Button(ventana,text='Parar',fg='black',bg='gray',font='arial 15', height=2, width=15, command=parar)
    btnstop.place(x=210,y=520)

    #BOTON PAUSA
    btnpause = Button(ventana,text='Pausar/Reanudar',fg='black',bg='gray',font='arial 15', height=2, width=15, command=lambda: pausar(pausado))
    btnpause.place(x=410,y=520)

    #BOTON PREVIOUS
    btnprevious = Button(ventana,text='Anterior',fg='black',bg='gray',font='arial 15', height=2, width=15, command=anteriorc)
    btnprevious.place(x=610,y=520)

    #BOTON NEXT
    btnnext = Button(ventana,text='Siguiente',fg='black',bg='gray',font='arial 15', height=2, width=15, command=siguientec)
    btnnext.place(x=810,y=520)

    #CUADRO DE TEXTO DE LA INFORMACION DE LA CANCION
    cuadroInfo = Text(ventana, bg="black", fg="green", width=78, height=10,font=("arial",12))
    cuadroInfo.place(x=10, y=10)


    #LLAMA AL GIF PARA MOSTRARLO EN LA VENTANA:
    mostrargif()
    #for i in range(len(listaCanciones)):
    #    print('Nombre: ' + str(listaCanciones[i].getNombre()))
    #    print('Artista: ' + str(listaCanciones[i].getArtista()))
    #    print('Ruta: ' + str(listaCanciones[i].getRuta()))
    #    print('Genero: ' + str(listaCanciones[i].getGenero()))
    #    print('Repetir: ' + str(listaCanciones[i].getRepetir()))
    #    print('Año: ' + str(listaCanciones[i].getAnio()))
    #    print()

    ventana.mainloop()

#FUNCION PARA RETORNAR LA RUTA DE LA CANCION
def rutac(nombrec):
    global listaCanciones
    for i in range(len(listaCanciones)):
        if nombrec == listaCanciones[i].getNombre():
            return listaCanciones[i].getRuta()

#FUNCION PARA RETORNAR EL OBJETO CANCION
def objcancion(rutac):
    global listaCanciones
    for i in range(len(listaCanciones)):
        if rutac == listaCanciones[i].getRuta():
            return listaCanciones[i]