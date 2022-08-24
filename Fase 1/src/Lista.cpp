#include "Lista.h"

void Lista::InsertarFinal(string nombre) {
    NodoLista *nuevo = new NodoLista(nombre);

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
