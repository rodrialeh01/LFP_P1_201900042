#------------------------------IMPORTANDO LIBRERIAS------------------------------------
#tkinter
import tkinter as tk
from tkinter import Button, scrolledtext, filedialog, messagebox
from tkinter import ttk
from tkinter import *
from typing import runtime_checkable
#------------------------------IMPORTANDO CLASES Y VENTANAS----------------------------
from Reproductor import VentanaReproductor
from AnalizadorLexico import AnalizadorLexico
from ReporteTokens import *
from ReporteErrores import *
from Cancion import Cancion

#VENTANA
ventana = tk.Tk()
ventana.title('T3 Musik')
ventana.geometry('900x600')
ventana.config(bg='black')
ventana.iconbitmap('icono.ico')
ventana.resizable(0,0)

#Label de Titulo
lbltitulo = Label(ventana,text='T3 Musik', font='arial 30 bold', fg='white', bg='black')
lbltitulo.place(x=30, y=20)

#CUADRO DE TEXTO
cuadrot = scrolledtext.ScrolledText(ventana, bg="black", fg="white", width=70, height=30,font=("arial",10),state='disabled')
cuadrot.place(x=30, y=70)

#VARIABLE GLOBAL UE MANTIENE EL CONTENIDO DEL ARCHIVO
contenido = ''

#FUNCION PARA ABRIR LA VENTANA PARA CARGAR EL ARCHIVO Y OBTENER SU RUTA
def obtenerruta():
    ruta = filedialog.askopenfilename(title='Cargar Archivo', filetypes = (("Text files", "*.mt3*"), ("all files", "*.*")))
    return ruta

#FUNCION PARA LEER EL CONTENIDO DEL ARCHIVO CARGADO
def leerArchivo():
    global contenido
    global cuadrot
    ruta = obtenerruta()
    if ruta != "":
        archivo = open(ruta,'r')   
        contenido = archivo.read()
        cuadrot.config(state='normal')
        #print(contenido)
        if cuadrot.get(1.0, END) != "":
            cuadrot.delete(1.0,END)
            cuadrot.insert(tk.INSERT, contenido)
            cuadrot.config(state='disabled')
        messagebox.showinfo("Success","Archivo cargado")
    else:
        messagebox.showinfo("Warning","No se cargó ningun archivo")


#METODO PARA ANALIZAR EL ARCHIVO
def analizar():
    global contenido
    #print(contenido)
    a = AnalizadorLexico()
    if contenido != '':
        a.analizar(contenido)
        if len(a.listaErrores) == 0:
            ventana.destroy()   
            generararchivoT(a.listaTokens)
            VentanaReproductor(nombreLista(a.listaTokens),aslistacan(aslistanombres(a.listaTokens),aslistaartistas(a.listaTokens),aslistarutas(a.listaTokens),aslistageneros(a.listaTokens),aslistarep(a.listaTokens),aslistaanios(a.listaTokens)))
        else:
            messagebox.showinfo("Warning","El archivo contiene errores, visualicelo en el reporte")
            generararchivoE(a.listaErrores,a.listaTokens)
    else:
        messagebox.showinfo("Warning","No se puede analizar un archivo inexistente")


#FUNCION PARA OBTENER EL NOMBRE DE LA LISTA
def nombreLista(listap):
    nombrelista = str(listap[2].lexema)
    caracteres = "\"'"
    for i in range(len(caracteres)):
        nombrelista = nombrelista.replace(caracteres[i],"")
    return nombrelista

def eliminarcomillas(cadena):
    caracteres = "\"'"
    for i in range(len(caracteres)):
        cadena = cadena.replace(caracteres[i],"")
    return cadena

#FUNCION PARA GUARDAR LA LISTA DE NOMBRES DE CANCIONES
def aslistanombres(listap):
    listaNombres = []
    for i in range(len(listap)):
        if listap[i].tipo == 'tk_nombre':
            nombre = eliminarcomillas(listap[i+2].lexema)
            listaNombres.append(nombre)
    return listaNombres

#FUNCION PARA GUARDAR LA LISTA DE ARTISTAS
def aslistaartistas(listap):
    listaArtistas = []
    for i in range(len(listap)):
        if listap[i].tipo == 'tk_artista':
            artista = eliminarcomillas(listap[i+2].lexema)
            listaArtistas.append(artista)
    return listaArtistas

#FUNCION PARA GUARDAR LA LISTA DE RUTAS
def aslistarutas(listap):
    listaRutas = []
    for i in range(len(listap)):
        if listap[i].tipo == 'tk_ruta':
            ruta = eliminarcomillas(listap[i+2].lexema)
            listaRutas.append(ruta)
    return listaRutas

#FUNCION PARA GUARDAR LA LISTA DE GENEROS
def aslistageneros(listap):
    listaGeneros = []
    for i in range(len(listap)):
        if listap[i].tipo == 'tk_genero':
            genero = eliminarcomillas(listap[i+2].lexema)
            listaGeneros.append(genero)
    return listaGeneros

#FUNCION PARA GUARDAR LA LISTA DE AÑOS
def aslistaanios(listap):
    listaAnios = []
    for i in range(len(listap)):
        if listap[i].tipo == 'tk_anio':
            anio = eliminarcomillas(listap[i+2].lexema)
            listaAnios.append(anio)
    return listaAnios

#FUNCION PARA GUARDAR LA LISTA DE REPETIR
def aslistarep(listap):
    listaRepetir = []
    for i in range(len(listap)):
        if listap[i].tipo == 'tk_repetir':
            rep = eliminarcomillas(listap[i+2].lexema)
            listaRepetir.append(rep)
    return listaRepetir

#FUNCION PARA RETORNAR LA LISTA DE OBJETOS DE CANCIONES
def aslistacan(listan,listaa,listar,listag,listare,listaan):
    listacanciones = []
    for i in range(len(listar)):
        listacanciones.append(Cancion(listan[i],listaa[i],listar[i],listag[i],listare[i],listaan[i]))
    return listacanciones

#BOTON DE CARGAR ARCHIVO
botonca = Button(ventana,text='Cargar Archivo', font='arial 24', bg="gray", command=leerArchivo)
botonca.place(x=580,y=70)

#BOTON DE ANALIZAR ARCHIVO
botonaa = Boton2 = Button(ventana,text='Analizar Archivo', font='arial 24', bg="gray", command=analizar)
Boton2.place(x=580,y=150)

ventana.mainloop()