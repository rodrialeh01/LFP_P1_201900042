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
    def __init__(self, descripcion, tipo, linea, columna):
        self.descripcion = descripcion
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

    def getInfo(self):
        print('*****')
        print('Descripcion: ', self.descripcion)
        print('Tipo: ', self.tipo)
        print('Linea: ', self.linea)
        print('Columna: ', self.columna)
        print('*****')