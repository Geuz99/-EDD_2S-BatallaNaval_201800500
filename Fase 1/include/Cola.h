#ifndef COLA_H
#define COLA_H

#include<stddef.h>
#include<iostream>

#include"NodoCola.h"

using namespace std;

class Cola
{
    public:
        NodoCola *head;
        NodoCola *end;

        Cola(){
            this->head = NULL;
            this->end = NULL;
        }
        void push(string alto, string ancho, string x, string y);
        void pop();
        void ImprimirTuto();
        void GenerarGrafo();

    private:
};

#endif // COLA_H
