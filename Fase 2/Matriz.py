from NodoMatriz import NodoMatriz


class Matriz():
    def __init__(self):
        self.root = NodoMatriz(-1, -1, "RAIZ")

    ##Insertar Cabecera Columna
    def crear_columna(self, x):
        nodo_col = self.root
        nuevo = NodoMatriz(x, -1, "COL")
        columna = self.insertar_orden_col(nuevo, nodo_col)
        return columna

    ##Insertar columnas en orden
    def insertar_orden_col(self, nuevo, cabeza_col):
        aux = cabeza_col
        insertado = False
        while True:
            if nuevo.x == aux.x:
                # la posicion ya existe y se sobreescribe la informacion
                aux.y = nuevo.y
                aux.dato = nuevo.dato
                return aux
            elif aux.x > nuevo.x:
                # insertar en medio, antes del aux
                insertado = True
                break
            if aux.siguiente is not None:
                aux = aux.siguiente
            else:
                insertado = False
                break

        if insertado:
            nuevo.siguiente = aux
            aux.anterior.siguiente = nuevo
            nuevo.anterior = aux.anterior
            aux.anterior = nuevo
        else:
            aux.siguiente = nuevo
            nuevo.anterior = aux
        return nuevo

    ##Insertar Cabecera Fila
    def crear_fila(self, y):
        nodo_fila = self.root
        nuevo = NodoMatriz(-1, y, "FIL")
        fila = self.insertar_orden_fila(nuevo, nodo_fila)
        return fila

    ##Insertar Fila en orden
    def insertar_orden_fila(self, nuevo, cabeza_fila):
        aux = cabeza_fila
        insertado = False
        while True:
            if nuevo.y == aux.y:
                # la posicion ya existe y se sobreescribe la informacion
                aux.x = nuevo.x
                aux.dato = nuevo.dato
                return aux
            elif aux.y > nuevo.y:
                # insertar en medio, antes del aux
                insertado = True
                break
            if aux.abajo is not None:
                aux = aux.abajo
            else:
                insertado = False
                break

        if insertado:
            nuevo.abajo = aux
            aux.arriba.abajo = nuevo
            nuevo.arriba = aux.arriba
            aux.arriba = nuevo
        else:
            aux.abajo = nuevo
            nuevo.arriba = aux
        return nuevo

    # Busqueda de cabecera columna
    def buscar_columna(self, x):
        aux = self.root
        while aux is not None:
            if aux.x == x:
                return aux
            aux = aux.siguiente
        return None

    # Busqueda de cabecera Fila
    def buscar_fila(self, y):
        aux = self.root
        while aux is not None:
            if (aux.y == y):
                return aux
            aux = aux.abajo
        return None

    ##Metodo para insertar
    def insertarNodo(self, x, y, dato):
        nuevo = NodoMatriz(x, y, dato)
        NodoColumna = self.buscar_columna(x)
        NodoFila = self.buscar_fila(y)
        ###Caso 1----No existe fila ni columna
        if NodoFila is None and NodoColumna is None:
            print("Caso 1")
            # crear las cabeceras
            NodoColumna = self.crear_columna(x)
            NodoFila = self.crear_fila(y)
            # insertar el contenido
            nuevo = self.insertar_orden_col(nuevo, NodoFila)
            nuevo = self.insertar_orden_fila(nuevo, NodoColumna)
            return
        ###Caso 2------No existe fila, pero si existe columna
        elif NodoFila is None and NodoColumna is not None:
            print("Caso 2")
            # crear las cabeceras
            NodoFila = self.crear_fila(y)
            # insertar el contenido
            nuevo = self.insertar_orden_col(nuevo, NodoFila)
            nuevo = self.insertar_orden_fila(nuevo, NodoColumna)
        ###Caso 3 ------ Existe fila pero no existe columna
        elif NodoFila is not None and NodoColumna is None:
            print("Caso 3")
            # crear las cabeceras
            NodoColumna = self.crear_columna(x)
            # insertar el contenido
            nuevo = self.insertar_orden_col(nuevo, NodoFila)
            nuevo = self.insertar_orden_fila(nuevo, NodoColumna)
            return
        ###Caso 4 ---- Existe fila y columna
        elif NodoFila is not None and NodoColumna is not None:
            print("Caso 4")
            # crear las cabeceras
            NodoColumna = self.crear_columna(x)
            NodoFila = self.crear_fila(y)
            # insertar el contenido
            nuevo = self.insertar_orden_col(nuevo, NodoFila)
            nuevo = self.insertar_orden_fila(nuevo, NodoColumna)
            return

    ##imprimir la matriz Nota: este metodo tambien esta imprimiendo las cabeceras
    def imprimir(self):
        aux = self.root
        while aux is not None:
            tex = ""
            aux2 = aux
            while aux2 is not None:
                tex += "[" + str(aux2.x) + str(aux2.y) + "]"
                tex += "[" + aux2.dato + "]"
                aux2 = aux2.siguiente
            print(tex)
            aux = aux.abajo
        return None

    def generarCol(self):
        aux2 = self.root
        aux = aux2.siguiente
        dot = ""
        dot = dot + "node [shape=component, style=filled, color=blue, fillcolor=lightsteelblue1];\n"
        while aux is not None:
            dot = dot + "C" + str(aux.x) + aux.dato + "[label=\"" + "[(" + "1," + str(aux.x) + ")]" + "\"];\n"
            aux = aux.siguiente
        return dot

    def generarFila(self):
        aux2 = self.root
        aux = aux2.abajo
        dot = ""
        dot += "node [shape=component, style=filled, color=black, fillcolor=firebrick1];\n"
        dot += aux2.dato + "[label=\"" + "[(" + str(aux2.dato) + "]" + "\"];\n"
        dot = dot + "node [shape=component, style=filled, color=blue, fillcolor=darkolivegreen1];\n"
        while aux is not None:
            dot = dot + "F" + str(aux.y) + aux.dato + "[label=\"" + "[(" + str(aux.y) + ",1)]" + "\"];\n"
            aux = aux.abajo
        return dot

    def Grafo(self):
        dot = ""
        dot += "digraph G {\n"
        dot += self.generarFila()
        dot += self.generarCol()
        dot += "}\n"
        print(dot)

