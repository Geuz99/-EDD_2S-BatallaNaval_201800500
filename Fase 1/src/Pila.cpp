#include "Pila.h"

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

