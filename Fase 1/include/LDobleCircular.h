#ifndef LDOBLECIRCULAR_H
#define LDOBLECIRCULAR_H

#include<stddef.h>
#include<iostream>

#include "NodoLDobleCircular.h"

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
        void insert(string);
        void imprimir();


    protected:

    private:
};

#endif // LDOBLECIRCULAR_H
