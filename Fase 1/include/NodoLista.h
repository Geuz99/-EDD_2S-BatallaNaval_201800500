#ifndef NODOLISTA_H
#define NODOLISTA_H

#include <stddef.h>
#include<string>

#include"Pila.h"

using namespace std;

class NodoLista
{
    public:
        string name;
        Pila pila;
        NodoLista *next;

        NodoLista(){
            name = "";
            next = NULL;
        }

    private:
};

#endif // NODOLISTA_H
