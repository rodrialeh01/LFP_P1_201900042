#--------------------------------IMPORTANDO LIBRERIAS Y CLASES-----------------------------
from Clases import Token, Error
from tkinter import messagebox

class AnalizadorLexico:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []

    def analizar(self, contenido):
        self.listaTokens = []
        self.listaErrores = []

        contenido += '$'
        indice = 0
        linea = 1
        columna = 1
        buffer = ""
        estado = 'A'

        while indice < len(contenido):
            caracter = contenido[indice]
            if estado == 'A':
                if caracter == '=':
                    buffer = caracter
                    columna += 1
                    if contenido[indice+1] == '>':
                        buffer += contenido[indice+1]
                        columna += 1
                        self.listaTokens.append(Token(buffer,'tk_flecha',linea,columna))
                        buffer = '' 
                        estado = 'A'
                        indice += 1 
                    else:
                        self.listaTokens.append(Token(buffer,'tk_igual',linea,columna))
                        buffer = '' 
                        estado = 'A'
                elif caracter == '(':
                    buffer = caracter
                    columna += 1
                    self.listaTokens.append(Token(buffer, 'tk_parentesisa', linea, columna))
                    buffer = ''
                    estado = 'A'
                elif caracter == ')':
                    buffer = caracter
                    columna += 1
                    self.listaTokens.append(Token(buffer, 'tk_parentesisc', linea, columna))
                    buffer = ''
                    estado = 'A'
                elif caracter == '{':
                    buffer = caracter
                    columna += 1
                    self.listaTokens.append(Token(buffer, 'tk_llavea', linea, columna))
                    buffer = ''
                    estado = 'A'
                elif caracter == '}':
                    buffer = caracter
                    columna += 1
                    self.listaTokens.append(Token(buffer, 'tk_llavec', linea, columna))
                    buffer = ''
                    estado = 'A'
                elif caracter == ':':
                    buffer = caracter
                    columna += 1
                    self.listaTokens.append(Token(buffer, 'tk_dospuntos', linea, columna))
                    buffer = ''
                    estado = 'A'
                elif caracter == ',':
                    buffer = caracter
                    columna += 1
                    self.listaTokens.append(Token(buffer, 'tk_coma', linea, columna))
                    buffer = ''
                    estado = 'A'
                elif caracter == ';':
                    buffer = caracter
                    columna += 1
                    self.listaTokens.append(Token(buffer, 'tk_puntoycoma', linea, columna))
                    buffer = ''
                    estado = 'A'
                elif caracter.isalpha() and (not caracter.isdigit()):
                    buffer = caracter
                    columna += 1
                    estado = 'B'
                elif caracter == '\n':
                    columna = 1
                    linea += 1
                elif caracter == ' ':
                    columna += 1
                elif caracter == '\t':
                    columna += 1
                elif caracter == "'":
                    buffer += caracter
                    columna += 1
                    estado = 'C'
                elif caracter == '"':
                    buffer = caracter
                    columna += 1
                    estado = 'D'
                elif caracter.isdigit():
                    buffer = caracter
                    columna += 1
                    estado = 'E'
                elif caracter == '$':
                    buffer = caracter
                    columna += 1
                    self.listaTokens.append(Token(buffer, '<< EOF >>' , linea, columna))
                    buffer = ''
                    estado = 'A'
                    messagebox.showinfo("Success","Archivo Analizado con éxito")
                else:
                    self.listaErrores.append(Error(caracter,caracter + " no reconocido como token.", 'Léxico', linea, columna)) 
                    buffer = ''
                    columna += 1 
            elif estado == 'B':
                if caracter.isalpha() and (not caracter.isdigit()):
                    buffer += caracter
                    columna += 1
                    estado = 'B'
                else:
                    if buffer == 'replist':
                        self.listaTokens.append(Token(buffer, 'tk_replist', linea, columna))
                    elif buffer == 'nombre':
                        self.listaTokens.append(Token(buffer, 'tk_nombre', linea, columna))
                    elif buffer == 'artista':
                        self.listaTokens.append(Token(buffer, 'tk_artista', linea, columna))
                    elif buffer == 'ruta':
                        self.listaTokens.append(Token(buffer, 'tk_ruta', linea, columna))
                    elif buffer == 'genero':
                        self.listaTokens.append(Token(buffer, 'tk_genero', linea, columna))
                    elif buffer == 'repetir':
                        self.listaTokens.append(Token(buffer, 'tk_repetir', linea, columna))
                    elif buffer == 'anio':
                        self.listaTokens.append(Token(buffer, 'tk_anio', linea, columna))
                    else:
                        self.listaErrores.append(Error(buffer, buffer + " no esta reconocido como token.", 'Léxico', linea, columna))
                    buffer = ''
                    estado = 'A'
                    indice -= 1
            elif estado == 'C':
                if caracter == "'":
                    buffer += caracter
                    columna += 1
                    self.listaTokens.append(Token(buffer, 'tk_cadena', linea, columna))
                    buffer = ''
                    estado = 'A'
                elif caracter =='\n':
                    columna = 1
                    linea += 1
                elif caracter == '"':
                    buffer += caracter
                    columna += 1
                    self.listaErrores.append(Error(buffer,"La forma de escritura de la cadena es incorrecta.", 'Léxico', linea, columna))
                    buffer = ''
                    estado = 'A'
                else:
                    buffer += caracter
                    columna += 1
                    estado = 'C'
            elif estado == 'D':
                if caracter == '"':
                    buffer += caracter
                    columna += 1
                    self.listaTokens.append(Token(buffer, 'tk_cadena', linea, columna))
                    buffer = ''
                    estado = 'A'
                elif caracter =='\n':
                    columna = 1
                    linea += 1
                elif caracter == "'":
                    buffer += caracter
                    columna += 1
                    self.listaErrores.append(Error(buffer, "La forma de escritura de la cadena es incorrecta.", 'Léxico', linea, columna))
                    buffer = ''
                    estado = 'A'
                else:
                    buffer += caracter
                    columna += 1
                    estado = 'D'
            elif estado == 'E':
                if caracter.isdigit():
                    buffer += caracter 
                    columna +=1
                    estado = 'E'
                else:
                    self.listaTokens.append(Token(buffer, 'tk_entero', linea, columna))
                    buffer = ''
                    indice -= 1
                    estado = 'A'
            indice += 1
'''
def imprimir(self):
print('Tokens')
for token in self.listaTokens:
token.getInfo()
print()
print('Errores')
for token in self.listaErrores:
token.getInfo()
print()
print("Cantidad de tokens: " + str(len(self.listaTokens)))
print("Cantidad de errores: " + str(len(self.listaErrores)))
'''
