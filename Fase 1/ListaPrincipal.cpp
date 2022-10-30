#include "ListaPrincipal.h"
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

string ListaPrincipal::dameCategorias(){
    string categoria = "";
    nodoprincipal*aux = Inicio;
     while (aux != NULL) {
        categoria = categoria + aux->valor + "\n";
        aux = aux->sig;
        
     }
     return categoria;
}


string ListaPrincipal::Categorias(){
    string categoria = "";
    nodoprincipal*aux = Inicio;
     while (aux != NULL) {
        categoria = categoria + "           CATEGORIA: " + aux->valor + "\n"; 
        categoria = categoria + "---------------------------------------------------------------------\n";            
        nodointerno * auxI = aux->listainterna.Inicio;
        while (auxI != NULL) {
            categoria = categoria + "* " + auxI->nombre + ", precio: " + auxI->precio +  "      ";            
            auxI = auxI->sig;
        }
        aux = aux->sig;
        categoria = categoria + "\n";
        categoria = categoria + "\n";
        categoria = categoria + "\n";
        
     }
     return categoria;
}

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

void ListaPrincipal::GenerarGrafo(){
    string dot = "";
    dot = dot + "digraph G {\n";
    dot = dot + "node [shape=signature, style=filled, color=lawngreen, fillcolor=lightgreen];\n";

    nodoprincipal *aux = Inicio;
    dot = dot + "//agregar nodos\n";
    while (aux != NULL) {
        dot = dot + aux->valor + "[label=\"" + aux->valor + "\"];\n";
        nodointerno *auxI = aux->listainterna.Inicio;
        while (auxI != NULL){
            dot = dot + auxI->nombre + "[label=\"" + auxI->nombre + "\"];\n";
            auxI = auxI->sig;
        }
        aux = aux->sig;
    }
    dot = dot + "{rank=same;\n";
    aux = Inicio;
    while (aux != NULL) {
        dot = dot + aux->valor;
        if (aux->sig != NULL) {
            dot = dot + "->";
        }
        aux = aux->sig;
    }
    dot = dot + "}\n";

    aux = Inicio;
    while (aux != NULL) {
        nodointerno *auxI = aux->listainterna.Inicio;
        dot = dot + aux->valor;
        dot = dot + "->";
        while(auxI != NULL){
            dot = dot + auxI->nombre;
            if (auxI->sig != NULL) {
                dot = dot + "->";
            }
            auxI = auxI->sig;
        }
        dot = dot + " ";
        aux = aux->sig;
    }
    dot = dot + "}\n";

    //cout << dot;
    //------->escribir archivo
    ofstream file;
    file.open("Articulos.dot");
    file << dot;
    file.close();

    //------->generar png
    system(("dot -Tpng Articulos.dot -o  Articulos.png"));

    //------>abrir archivo
    system(("Articulos.png"));
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



