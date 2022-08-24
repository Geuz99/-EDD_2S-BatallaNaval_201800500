#ifndef NODOLISTA_H
#define NODOLISTA_H

#include <stddef.h>
#include<string>

using namespace std;

class NodoLista
{
    public:
        string name;
        NodoLista *next;

        NodoLista(string _name){
            name = _name;
            next = NULL;
        }

    private:
};

#endif // NODOLISTA_H
