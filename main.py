"""
Esto lo fui sacando de las clases del campus
"""
# Creamos la clase Nodo con dos atributos (valor e hijos) y un metodo (agregar_hijo).

class Nodo:
    
    def __init__(self, valor):           # Constructor de la Clase Nodo
        self.valor = valor               # Guarda el dato o valor que le pasás al nodo
        self.hijos = {}                  # Diccionario con todos los hijos que va a tener el Nodo
    
    # Metodo agregar_hijo
    def agregar_hijo(self, nodo):
        self.hijos[nodo.valor] = nodo    # Agregamos al diccionario "hijos" --> diccionario[key_nueva] = valuer 
    
    # Metodo buscar_camino 
    def buscar_camino(self, destino, camino=None):
        # Inicializamos el camino solo una vez.
        if camino is None:
            camino = []

        # Agregamos el nodo actual al camino
        camino.append(self.valor)

        # Si el nodo actual es el mismo que el nodo destino, retomamos el camino
        if self.valor == destino:
            return camino                 # Me devuelve None
        
        # Recorremos los hijos
        for hijo in self.hijos.values():
            # Buscamos de manera recursiva en cada hijo, pasando el camino como
            # una copia para no modificar la lista original
            camino_encontrado = hijo.buscar_camino(destino, camino[:])
            # Si encontramos el camino, lo retomamos
            if camino_encontrado:
                return camino_encontrado

# Creamos 6 objetos, uno para cada nodo, a partir de la clase Nodo

raiz   = Nodo("A")
nodo_b = Nodo("B")
nodo_c = Nodo("C")
nodo_d = Nodo("D")
nodo_e = Nodo("E")
nodo_f = Nodo("F")

# Conectamos la raiz a sus hijos (B y C)
raiz.agregar_hijo(nodo_b)
raiz.agregar_hijo(nodo_c)

# Conectamos el Nodo B a sus hijos (D y E)
nodo_b.agregar_hijo(nodo_d)
nodo_b.agregar_hijo(nodo_e)

# Conectamos el Nodo C a sus hijos (F)
nodo_c.agregar_hijo(nodo_f)

print(raiz.hijos)

print(nodo_b.hijos)

print(nodo_c.hijos)

