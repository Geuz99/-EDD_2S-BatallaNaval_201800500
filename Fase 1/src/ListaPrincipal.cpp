#include "ListaPrincipal.h"
#include <string>
#include <iostream>

using namespace std;

void ListaPrincipal::Imprimir() {
    nodoprincipal*aux = Inicio;
    while (aux != NULL) {
        cout << "[" << aux->valor << "]->";
        nodointerno * auxI = aux->listainterna.Inicio;
        while (auxI != NULL) {
            cout << "[" << auxI->nombre << "]->";
            auxI = auxI->sig;
        }
        cout << ("NULL")<<endl;
        //cout << ("\n | ");
        aux = aux->sig;
    }
    cout << ("NULL")<<endl;
}

void ListaPrincipal::ImprimirTienda() {
    nodoprincipal*aux = Inicio;
    cout<<"-------------------------------------------------------"<<endl;
    cout<<"                         Total Tokens "<<endl;
    cout<<"Tienda"<<endl;
    while (aux != NULL) {
        cout <<"Categoria "<<aux->valor<<endl;
        nodointerno * auxI = aux->listainterna.Inicio;
        while (auxI != NULL) {
            cout <<" Id "<<auxI->id<<" Nombre "<<auxI->nombre<<" Precio "<<auxI->precio<<endl;
            auxI = auxI->sig;
        }
        aux = aux->sig;
    }
    cout<<"Elija opcion a comprar"<<endl;
    cout<<"-------------------------------------------------------"<<endl;
}

void ListaPrincipal::Insertar(string id, string precio, string nombre, string src, string categoria) {
    if (Inicio == NULL) {//lista se encuentra vacia
        nodoprincipal*nuevo = new nodoprincipal();
        nuevo->valor = categoria;
        nuevo->listainterna.InsertarFinal(id, precio, nombre, src); //
        Inicio = nuevo;
    } else {//la lista no se encuentra vacia
        nodoprincipal*busqueda = BuscarPrincipal(Inicio, categoria);
        nodoprincipal*nuevo = new nodoprincipal();
        nuevo->valor = categoria;
        nuevo->listainterna.InsertarFinal(id, precio, nombre, src);
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
            busqueda->listainterna.InsertarFinal(id, precio, nombre, src);
        }
    }



}

nodoprincipal* ListaPrincipal::BuscarPrincipal(nodoprincipal* inicioL, string categoria) {
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



