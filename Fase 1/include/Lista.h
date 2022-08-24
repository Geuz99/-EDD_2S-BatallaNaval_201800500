#ifndef LISTA_H
#define LISTA_H

#include"NodoLista.h"

#include <iostream>
#include<string>

using namespace std;

class Lista
{
    public:
        NodoLista *head;
        Lista(){
            head = NULL;
        }
        void InsertarFinal(string nombre);
        void Imprimir();

    private:
};

#endif // LISTA_H
