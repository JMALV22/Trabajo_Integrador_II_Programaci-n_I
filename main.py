def crear_nodo(valor):
  return [valor, [], []]

def mostrar_arbol(nodo, nivel=0):
    if nodo != []:
        print('   ' * nivel + str(nodo[0]))
        mostrar_arbol(nodo[1], nivel + 1)
        mostrar_arbol(nodo[2], nivel + 1)

def insertar_nodo_izq(nodo, valor):
    if nodo[1] == []:
        nodo[1] = crear_nodo(valor)
    else:
        insertar_nodo_izq(nodo[1], valor)

def insertar_nodo_der(nodo, valor):
    if nodo[2] == []:
        nodo[2] = crear_nodo(valor)
    else:
        insertar_nodo_der(nodo[2], valor)

def pedir_datos():
    raiz = input('Ingrese el nodo raíz de su árbol: ')
    arbol = crear_nodo(raiz)

    while True:
        posicion = input('Ingrese la posición del nodo (izquierda o derecha): ').lower()
        valor = input('Ingrese el nombre de su familiar (o "z" para finalizar): ')
        if valor == 'z':
            break
        if posicion == 'izquierda':
            insertar_nodo_izq(arbol, valor)
        elif posicion == 'derecha':
            insertar_nodo_der(arbol, valor)
        else:
            print("Posición inválida. Escriba 'izquierda' o 'derecha'.")

        mostrar_arbol(arbol)

    return arbol
    
def main():
  print(pedir_datos())

main()
    