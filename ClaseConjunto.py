class Conjunto:
    __elementos = []

    def __init__(self):
        self.__elementos = []
    
    def agregarElemento(self, elemento):
        if isinstance(elemento, int):
            if elemento not in self.__elementos:
                self.__elementos.append(elemento)
                self.__elementos.sort()

    def ordenar(self):
        self.__elementos.sort()

    def getTamaño(self):
        return len(self.__elementos)

    def getElementoPorIndice(self, indice):
        return self.__elementos[indice]

    def quitarElemento(self, elemento):
        if elemento in self.__elementos:
            self.__elementos.remove(elemento)

    def __add__(self, otro):
        nuevo = None
        if isinstance(otro, Conjunto):
            nuevo = Conjunto()
            for unElemento in self.__elementos:
                nuevo.agregarElemento(unElemento)
            for i in range(otro.getTamaño()):
                nuevo.agregarElemento(otro.getElementoPorIndice(i))
        return nuevo
    
    def __sub__(self, otro):
        nuevo = None
        if isinstance(otro, Conjunto):
            nuevo = Conjunto()
            for unElemento in self.__elementos:
                nuevo.agregarElemento(unElemento)
            for i in range(otro.getTamaño()):
                nuevo.quitarElemento(otro.getElementoPorIndice(i))
        return nuevo
    
    def __eq__(self, otro):
        resultado = False
        if isinstance(otro, Conjunto):
            if self.getTamaño() == otro.getTamaño():
                band = True
                i = 0
                while i < self.getTamaño() and band:
                    if self.getElementoPorIndice(i) != otro.getElementoPorIndice(i):
                        band = False
                    i += 1
                resultado = band
        return resultado
    
    def __str__(self):
        if self.getTamaño() == 0:
            cadena = "{}"
        else:
            cadena = "{"
            for unElemento in self.__elementos:
                cadena += "{0}; ".format(unElemento)
            cadena = cadena[0:-2] + "}"
        return cadena