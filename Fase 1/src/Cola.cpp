#include "Cola.h"

#include<string>

using namespace std;

void Cola::push(string alto, string ancho, string x, string y){
    NodoCola *nuevo = new NodoCola(alto, ancho, x, y);
    if (head==NULL){
        head = nuevo;
        end = nuevo;
    }else{
        end->next = nuevo;
        end = nuevo;
    }

}

void Cola::Imprimir() {
    NodoCola *aux = head;
    while (aux != NULL) {
        cout <<"[" << aux->x << "]->";
        aux = aux->next;
    }
    cout<<""<<endl;
}

