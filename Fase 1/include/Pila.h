#ifndef PILA_H
#define PILA_H

#include <iostream>
#include<string>

#include"NodoPila.h"

using namespace std;

class Pila
{
    public:
        NodoPila *head;
        Pila(){
            head = NULL;
        }
        void push(int x, int y);
        void pop();
        void Imprimir();

    private:
};

#endif // PILA_H
