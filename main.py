# Metodo para crear un nuevo nodo
def crear_nodo(valor):
    return [valor, [], []]

# Metodo para graficar el arbol en pantalla usando print
def mostrar_arbol(nodo, nivel=0):
    if nodo != []:
        print('   ' * nivel + str(nodo[0]))
        mostrar_arbol(nodo[1], nivel + 1)
        mostrar_arbol(nodo[2], nivel + 1)

# Metodo para insertar un nodo del lado izquierdo
def insertar_nodo_izq(nodo, valor):
    if nodo[1] == []:
        nodo[1] = crear_nodo(valor) # Si no hay ningun nodo en el lado izquierdo, crea un nuevo nodo en esa posicion
    else:
        insertar_nodo_izq(nodo[1], valor) # Si la funcion encuentra un nodo en esa posicion, vuelve a ejecutar la funcion en forma recursiva hasta encontrar un espacio vacio

# Metodo para insertar un nodo del lado derecho
def insertar_nodo_der(nodo, valor):
    if nodo[2] == []:
        nodo[2] = crear_nodo(valor) # Al igual que el la funcion anterior, verifica que no haya ningun nodo y de ser asi, lo crea, con la unica diferencia de que se va a crear en la posicion de la lista 2
    else:
        insertar_nodo_der(nodo[2], valor)

# Se encarga de pedirle los datos al usuario, y parar hasta que el usuario presione 'z'
def pedir_datos():
    raiz = input('Ingrese el nodo raíz de su árbol: ')
    arbol = crear_nodo(raiz)

    while True:
        posicion = input('Ingrese la posición del nodo (izquierda o derecha) o z para finalizar: ').lower()
        if posicion == 'z':
            break
        valor = input('Ingrese el nombre de su familiar: ')
        if posicion == 'izquierda':
            insertar_nodo_izq(arbol, valor)
        elif posicion == 'derecha':
            insertar_nodo_der(arbol, valor)
        else:
            print("Posición inválida. Escriba 'izquierda' o 'derecha'.")

        mostrar_arbol(arbol)

    return arbol
    
"""
# Recorrido de Árbol - PreORDEN.
"""
def recorrer_preorden(arbol):
    preorden = []                                         # Lista que va a contener el recorrido en preorden
    preorden.append(arbol[0])                             # Se agrega primero la raíz del árbol (preorden: raíz - izquierda - derecha)

    # Si ambos hijos (izquierdo y derecho) están vacíos, es un nodo hoja
    if arbol[1] == [] and arbol[2] == []:
        return preorden                                   # Se retorna solo la raíz porque no hay más nodos que recorrer

    # Si el hijo izquierdo NO está vacío
    if arbol[1] != []:                                    
        preorden.extend(recorrer_preorden(arbol[1]))      # Se recorre primero el subárbol izquierdo (recursivamente)

        # Luego, si el hijo derecho también tiene contenido, se recorre
        if arbol[2] != []:
            preorden.extend(recorrer_preorden(arbol[2]))
            return preorden                               # Se retorna el recorrido acumulado
        else:
            return preorden                               # Si no hay hijo derecho, se retorna el recorrido hasta ahora

    else:                                                 # Si el hijo izquierdo está vacío
        if arbol[2] != []:
            preorden.extend(recorrer_preorden(arbol[2]))  # Se recorre solo el subárbol derecho
            return preorden                               # Se retorna el recorrido
"""
# Recorrido de Árbol - InORDEN.
"""
def recorrer_inorden(arbol):
    inorden = []                                          # Lista que almacenará el recorrido inorden

    # Si ambos hijos están vacíos, es un nodo hoja
    if arbol[1] == [] and arbol[2] == []:
        inorden.append(arbol[0])                          # Se agrega el único valor (la raíz de este nodo hoja)
        return inorden                                    # Se retorna la lista con ese único elemento

    # Si el hijo izquierdo tiene contenido
    if arbol[1] != []:
        inorden.extend(recorrer_inorden(arbol[1]))        # Primero se recorre el subárbol izquierdo
        inorden.append(arbol[0])                          # Luego se agrega la raíz (nodo actual)

        # Si el hijo derecho también tiene contenido
        if arbol[2] != []:
            inorden.extend(recorrer_inorden(arbol[2]))    # Se recorre el subárbol derecho
            return inorden                                # Se retorna el recorrido completo
        else:
            return inorden                                # Si no hay hijo derecho, se retorna lo acumulado hasta ahora

    else:                                                 # Si el hijo izquierdo está vacío
        inorden.append(arbol[0])                          # Se agrega la raíz directamente

        # Si hay hijo derecho, se recorre
        if arbol[2] != []:
            inorden.extend(recorrer_inorden(arbol[2]))    # Se recorre el subárbol derecho
            return inorden                                # Se retorna el recorrido
"""
# Recorrido de Árbol - PostORDEN.
"""
def recorrer_postorden(arbol):
    postorden = []                                        # Lista donde se almacenará el recorrido en postorden

    # Caso base: si el nodo es una hoja (sin hijos izquierdo ni derecho)
    if arbol[1] == [] and arbol[2] == []:
        postorden.append(arbol[0])                        # Se agrega la raíz del nodo hoja
        return postorden                                  # Se devuelve esa lista con un solo elemento

    # Si el hijo izquierdo tiene contenido
    if arbol[1] != []:
        postorden.extend(recorrer_postorden(arbol[1]))    # Primero se recorre el subárbol izquierdo

        if arbol[2] != []:
            postorden.extend(recorrer_postorden(arbol[2])) # Luego se recorre el subárbol derecho (si existe)

        postorden.append(arbol[0])                        # Finalmente se agrega la raíz
        return postorden                                  # Se retorna la lista con el recorrido acumulado

    else:                                                 # Si el hijo izquierdo está vacío
        if arbol[2] != []:
            postorden.extend(recorrer_postorden(arbol[2])) # Se recorre solo el subárbol derecho (si existe)

        postorden.append(arbol[0])                        # Finalmente se agrega la raíz
        return postorden                                  # Se retorna la lista con el recorrido
    
def main():
    arbol = pedir_datos()
    preorden = recorrer_preorden(arbol)
    inorden = recorrer_inorden(arbol)
    postorden = recorrer_postorden(arbol)
    print(f"Recorrido PreORDEN:\n{preorden}")
    print(f"Recorrido InORDEN:\n{inorden}")
    print(f"Recorrido PostORDEN:\n{postorden}")

main()
