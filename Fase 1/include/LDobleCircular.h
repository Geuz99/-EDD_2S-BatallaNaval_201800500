#ifndef LDOBLECIRCULAR_H
#define LDOBLECIRCULAR_H

#include<stddef.h>
#include<iostream>

#include "NodoLDobleCircular.h"
#include"ListaPrincipal.h"
#include"Cola.h"
#include"Pila.h"
#include"Lista.h"

using namespace std;

class LDobleCircular
{
    public:
        NodoLDobleCircular *head;
        NodoLDobleCircular *end;
        int size = 0;

        LDobleCircular(){
            this->head = NULL;
            this->end = NULL;
        }
        void insert(string nick, string password, string monedas, string edad);
        void imprimir();
        void editar(string nick, string password, string nicknew, string passwordnew, string edadnew);
        void buscar(string nick, string password, Cola colaTuto, ListaPrincipal listaArticulos, Pila pilaMov);
        void eliminar(string nick, string password);


    protected:

    private:
};

#endif // LDOBLECIRCULAR_H
