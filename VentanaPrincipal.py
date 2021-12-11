import tkinter as tk
from tkinter import Button, scrolledtext, filedialog, messagebox
from tkinter import ttk
from tkinter import *
from typing import runtime_checkable
from Reproductor import VentanaReproductor
from AnalizadorLexico import AnalizadorLexico

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

contenido = ''
def obtenerruta():
    ruta = filedialog.askopenfilename(title='Cargar Archivo', filetypes = (("Text files", "*.mt3*"), ("all files", "*.*")))
    return ruta


def leerArchivo():
    global contenido
    ruta = obtenerruta()
    if ruta != "":
        archivo = open(ruta,'r')   
        contenido = archivo.read()
        #print(contenido)
        if cuadrot.get(1.0, END) != "":
            cuadrot.delete(1.0,END)
            cuadrot.insert(tk.INSERT, contenido)
        messagebox.showinfo("Success","Archivo cargado")
    else:
        messagebox.showinfo("Warning","No se cargó ningun archivo")


#METODO PARA ANALIZAR EL ARCHIVO
def analizar():
    global contenido
    print(contenido)
    a = AnalizadorLexico()
    a.analizar(contenido)
    a.imprimir()
    ventana.destroy()    
    VentanaReproductor()


#BOTON DE CARGAR ARCHIVO
botonca = Button(ventana,text='Cargar Archivo', font='arial 24', command=leerArchivo)
botonca.place(x=580,y=70)

#BOTON DE ANALIZAR ARCHIVO
botonaa = Boton2 = Button(ventana,text='Analizar Archivo', font='arial 24', command=analizar)
Boton2.place(x=580,y=150)

ventana.mainloop()