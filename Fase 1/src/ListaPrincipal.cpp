#include "ListaPrincipal.h"
#include <string>
#include <iostream>

void ListaPrincipal::Imprimir() {
    nodoprincipal*aux = Inicio;
    while (aux != NULL) {
        cout << "[" << aux->valor << "]->";
        nodointerno * auxI = aux->listainterna.Inicio;
        while (auxI != NULL) {
            cout << "[" << auxI->valor << "]->";
            auxI = auxI->sig;
        }
        cout << ("NULL");
        cout << ("\n | ");
        aux = aux->sig;
    }
    cout << ("NULL");
}

void ListaPrincipal::Insertar(int valor, int categoria) {
    if (Inicio == NULL) {//lista se encuentra vacia
        nodoprincipal*nuevo = new nodoprincipal();
        nuevo->valor = categoria;
        nuevo->listainterna.InsertarEnOrden(valor);
        Inicio = nuevo;
    } else {//la lista no se encuentra vacia
        nodoprincipal*busqueda = BuscarPrincipal(Inicio, categoria);
        nodoprincipal*nuevo = new nodoprincipal();
        nuevo->valor = categoria;
        nuevo->listainterna.InsertarEnOrden(valor);
        if (busqueda == NULL) {//como no hay categoria insertamos al final una nueva
            nodoprincipal*auxActual = Inicio;
            while (auxActual != NULL) {
                if (auxActual->sig == NULL) {
                    auxActual->sig = nuevo;
                    break;
                }
                auxActual = auxActual->sig;
            }
        } else {//si la categoria existe se inserta en la misma
            busqueda->listainterna.InsertarEnOrden(valor);
        }
    }



}

nodoprincipal* ListaPrincipal::BuscarPrincipal(nodoprincipal* inicioL, int categoria) {
    if (inicioL == NULL) {
        return inicioL;
    } else {
        nodoprincipal*auxActual = inicioL;
        while (auxActual != NULL) {
            if (auxActual->valor == categoria) {
                break;
            }
            auxActual = auxActual->sig;
        }
        return auxActual;
    }
}



