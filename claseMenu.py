from ClaseConjunto import Conjunto

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.opcion5,
                            '6':self.opcion6,
                            '7':self.opcion7,
                            '8':self.salir
                          }
    def opcion(self, conjunto1, conjunto2, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='4' or op=='5' or op == '6' or op == '7':
            func(conjunto1, conjunto2)
        elif op =='2':
            func(conjunto1)
        elif op == '3':
            func(conjunto2)
        else:
            func()


    def salir(self):
        print('Usted salio del programa')


    def opcion1(self, conjunto1, conjunto2):
        print(conjunto1)
        print(conjunto2)


    def opcion2(self, conjunto1):
        elemento = int(input("Ingrese el entero a agregar: "))
        conjunto1.agregarElemento(elemento)


    def opcion3(self, conjunto2):
        elemento = int(input("Ingrese el entero a agregar: "))
        conjunto2.agregarElemento(elemento)
    

    def opcion4(self, conjunto1, conjunto2):
        conjunto3 = conjunto1 + conjunto2
        print(conjunto3)
    

    def opcion5(self, conjunto1, conjunto2):
        conjunto3 = conjunto1 - conjunto2
        print(conjunto3)
    

    def opcion6(self, conjunto1, conjunto2):
        conjunto3 = conjunto2 - conjunto1
        print(conjunto3)
    
    def opcion7(self, conjunto1, conjunto2):
        if conjunto1 == conjunto2:
            print("Los conjuntos son iguales")
        else:
            print("Los conjuntos son distintos")
    
    
    def ejecutarMenu(self):
            conjunto1 = Conjunto()
            conjunto2 = Conjunto()
            opcion = "0"
            while opcion != "8":
                print("Ingrese la opcion deseada")
                print("[1] Mostrar el contenido de ambos conjuntos")
                print("[2] Agregar un elemento al conjunto 1")
                print("[3] Agregar un elemento al conjunto 2")
                print("[4] Unir los conjuntos 1 y 2")
                print("[5] Hacer la diferencia del conjunto 1 con el conjunto 2")
                print("[6] Hacer la diferencia del conjunto 2 con el conjunto 1")
                print("[7] Verificar si ambos conjuntos son iguales")
                print("[8] Salir")
                opcion = input("--> ")  
                self.opcion(conjunto1, conjunto2, opcion)