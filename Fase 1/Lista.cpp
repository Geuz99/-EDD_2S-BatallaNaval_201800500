#include "Lista.h"

void Lista::InsertarFinal(string nombre, int x, int y) {
    NodoLista *nuevo = new NodoLista();
    nuevo->name = nombre;
    nuevo->pila.push(x,y);

    if (head == NULL) {
        head = nuevo;
    } else {
        NodoLista *auxActual = head;

        while (auxActual != NULL) {
            if (auxActual->next == NULL) {
                auxActual->next = nuevo;
                break;
            }
            auxActual = auxActual->next;
        }
    }
}

void Lista::Imprimir() {
    NodoLista *aux = head;
    while (aux != NULL) {
        cout <<"[" << aux->name << "]->";
        aux = aux->next;
    }
    cout << ("NULL");
}
