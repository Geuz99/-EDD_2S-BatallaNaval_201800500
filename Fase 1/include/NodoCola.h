#ifndef NODOCOLA_H
#define NODOCOLA_H

#include<string>
#include <stddef.h>

using namespace std;

class NodoCola
{
    public:
        string alto;
        string ancho;
        string x;
        string y;
        NodoCola *next;

        NodoCola(string _alto, string _ancho, string _x, string _y){
            alto = _alto;
            ancho = _ancho;
            x = _x;
            y = _y;
            next = NULL;
        }
    private:
};

#endif // NODOCOLA_H
