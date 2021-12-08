import tkinter as tk
from tkinter import Button, scrolledtext, filedialog
from tkinter import ttk
from tkinter import *

#VENTANA
ventana = tk.Tk()
ventana.title('T3 Musik')
ventana.geometry('900x600')
ventana.config(bg='orange')
ventana.iconbitmap('icono.ico')
ventana.resizable(0,0)

#Label de Titulo
lbltitulo = Label(ventana,text='T3 Musik', font='arial 30 bold', fg='black', bg='orange')
lbltitulo.place(x=30, y=20)

#CUADRO DE TEXTO
cuadrot = scrolledtext.ScrolledText(ventana, bg="white", width=70, height=30,font=("arial",10))
cuadrot.place(x=30, y=70)

#METODO PARA CARGAR EL ARCHIVO
def abrir():
    global cuadrot
    ruta = filedialog.askopenfilename(title='Cargar Archivo')    
    print(ruta)
    archivo = open(ruta,'r')    
    contenido = archivo.read()
    print(contenido)
    cuadrot.insert(tk.INSERT, contenido)
    archivo.close()

#BOTON DE CARGAR ARCHIVO
botonca = Button(ventana,text='Cargar Archivo', font='arial 24', command=abrir)
botonca.place(x=580,y=70)

#BOTON DE ANALIZAR ARCHIVO
botonaa = Boton2 = Button(ventana,text='Analizar Archivo', font='arial 24', command=abrir)
Boton2.place(x=580,y=150)

ventana.mainloop()



