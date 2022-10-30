import shutil
from subprocess import check_call
from PIL import Image

from NodoAdy import NodoAdy


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = NodoAdy(d)
        node.next = self.graph[s]
        self.graph[s] = node

        # node = NodoAdy(s)
        # node.next = self.graph[d]
        # self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertice " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

    def showList(self):
        cadena = ""
        cadena = cadena + "digraph ListaAdy{\n" + "node [shape=box3d, style=filled, color=olivedrab2, " \
                                                  "fillcolor=aquamarine];\n" + "rankdir=LR\n "
        for i in range(self.V):
            cadena = cadena + "vertice" + str(i) + ' [label = \"' + str(i) + "\"];\n"
            temp = self.graph[i]
            while temp:
                cadena = cadena + "v" + str(i) + "No" + str(temp.vertex) + '[label = \"' + str(temp.vertex) + "\"];\n"
                temp = temp.next
        for i in range(self.V):
            cadena = cadena + "vertice" + str(i)
            temp = self.graph[i]
            while temp:
                cadena = cadena + "->" + "v" + str(i) + "No" + str(temp.vertex)
                temp = temp.next
            cadena = cadena + "\n"

        cadena = cadena + "}"

        with open('ListaAdy.dot', 'w') as f:
            f.write(cadena)
        check_call(['dot', '-Tpng', 'ListaAdy.dot', '-o', 'ListaAdy.png'])
        img = Image.open('ListaAdy.png')
        img.show()

    def showGraph(self):
        cadena = ""
        cadena = cadena + "digraph Grapho{\n" + "node [style=filled, color=olivedrab2, " \
                                                "fillcolor=aquamarine];\n"
        for i in range(self.V):
            temp = self.graph[i]
            while temp:
                cadena = cadena + "i" + str(temp.vertex) + '[label = \"' + str(temp.vertex) + "\"];\n"
                temp = temp.next
        for i in range(self.V):
            temp = self.graph[i]
            while temp:
                cadena = cadena + "i" + str(temp.vertex) + "->"
                temp = temp.next
        cadena = cadena + "i1 \n}"

        with open('Grapho.dot', 'w') as f:
            f.write(cadena)
        check_call(['dot', '-Tpng', 'Grapho.dot', '-o', 'Grapho.png'])
        img = Image.open('Grapho.png')
        img.show()
