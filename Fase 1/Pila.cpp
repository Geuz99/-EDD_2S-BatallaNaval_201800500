#include "Pila.h"

#include<string>
#include<iostream>
#include <fstream>
#include <sstream>

void Pila::push(int x, int y){
    NodoPila *nuevo = new NodoPila(x, y);
    if (head == NULL) {
        head = nuevo;
    } else {
        nuevo->next=head;
        head=nuevo;
    }

}

void Pila::pop() {
    NodoPila *aux = head;
    head = aux->next;
}

void Pila::Imprimir() {
    NodoPila *aux = head;
    while (aux != NULL) {
        cout <<"[" << aux->x << "," << aux->y << "]\n";
        aux = aux->next;
    }
}

void Pila::GenerarGrafo(){
    string dot = "";
    dot = dot + "digraph G {\n";
    dot = dot + "node [shape=tab, color=goldenrod2, style=filled];\n";
    NodoPila *aux = head;
    dot = dot + "//agregar nodos\n";
    while (aux != NULL) {
        dot = dot + "\"" + std::to_string(aux->x) + "," + std::to_string(aux->y) + "\"" + "[label=\"" + "x: " + std::to_string(aux->x) + "\ny: " + std::to_string(aux->y) + "\"];\n";
        aux = aux->next;
    }
    dot = dot + "{rank=same;\n";
    aux = head;
    while (aux != NULL) {

        dot = dot + "\"" + std::to_string(aux->x) + "," + std::to_string(aux->y) + "\"";
        if (aux->next != NULL) {
            dot = dot + "->";
        }
        aux = aux->next;
    }
    dot = dot + "}\n";
    dot = dot + "}\n";

    //cout << dot;
    //------->escribir archivo
    ofstream file;
    file.open("Mov.dot");
    file << dot;
    file.close();

    //------->generar png
    system(("dot -Tpng Mov.dot -o  Mov.png"));

}

void Pila::GenerarGrafo2(){
    //------>abrir archivo
    system(("Mov.png"));
}

