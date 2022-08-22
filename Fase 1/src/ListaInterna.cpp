#include "ListaInterna.h"

void ListaInterna::InsertarFinal(int valor) {
    nodointerno*nuevo = new nodointerno();
    nuevo->valor = valor;

    if (Inicio == NULL) {
        Inicio = nuevo;
    } else {
        nodointerno*auxActual = Inicio;

        while (auxActual != NULL) {
            if (auxActual->sig == NULL) {
                auxActual->sig = nuevo;
                break;
            }
            auxActual = auxActual->sig;
        }
    }


}

void ListaInterna::InsertarEnOrden(int valor) {
    nodointerno*nuevo = new nodointerno();
    nuevo->valor = valor;
    if (Inicio == NULL) {//Si la lista se encuentra vacia
        Inicio = nuevo;
    } else {//si la lista no esta vacia
        nodointerno*auxActual = Inicio;
        nodointerno*auxSiguiente;
        while (auxActual != NULL) {
            auxSiguiente = auxActual->sig;
            if (nuevo->valor < auxActual->valor) {//insertar al inicio de la lista por que es menor
                nuevo->sig = auxActual;
                Inicio = nuevo;
                break;
            } else if (auxSiguiente == NULL) {//insertar al final de la lista
                auxActual->sig = nuevo;
                break;
            } else if (nuevo->valor < auxSiguiente->valor) {//insertar en medio de la lista
                auxActual->sig = nuevo;
                nuevo->sig = auxSiguiente;
                break;
            }
            auxActual = auxActual->sig;
        }
    }
}


void ListaInterna::Imprimir() {
    nodointerno*aux = Inicio;
    while (aux != NULL) {
        cout <<"[" << aux->valor << "]->";
        aux = aux->sig;
    }
    cout << ("NULL");
}
