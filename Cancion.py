class Cancion:
    def __init__(self,nombre,artista,ruta,genero,repetir,anio):
        self.nombre = nombre
        self.artista = artista
        self.ruta = ruta
        self.genero = genero
        self.repetir = repetir
        self.anio = anio

    def getNombre(self):
        return self.nombre

    def getArtista(self):
        return self.artista

    def getRuta(self):
        return self.ruta

    def getGenero(self):
        return self.genero

    def getRepetir(self):
        return self.repetir

    def getAnio(self):
        return self.anio