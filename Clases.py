class Token:
    def __init__(self, lexema, tipo, linea, columna):
        self.lexema = lexema
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

    def getInfo(self):
        print('*****')
        print('Lexema: ', self.lexema)
        print('Tipo: ', self.tipo)
        print('Linea: ', self.linea)
        print('Columna: ', self.columna)
        print('*****')

class Error:
    def __init__(self,caracter, descripcion, tipo, linea, columna):
        self.caracter = caracter
        self.descripcion = descripcion
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

    def getInfo(self):
        print('*****')
        print('Caracter: ', self.caracter)
        print('Descripcion: ', self.descripcion)
        print('Tipo: ', self.tipo)
        print('Linea: ', self.linea)
        print('Columna: ', self.columna)
        print('*****')