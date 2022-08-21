#ifndef NODOLDOBLECIRCULAR_H
#define NODOLDOBLECIRCULAR_H

#include<iostream>
#include<string>

#include"Usuarios.h"

using namespace std;

class NodoLDobleCircular
{
    public:
        string data;
        NodoLDobleCircular *next;
        NodoLDobleCircular *prev;

        NodoLDobleCircular(string _data){
            this ->next = NULL;
            this ->prev = NULL;
            this ->data = _data;
        }

    protected:

    private:
};

#endif // NODOLDOBLECIRCULAR_H
