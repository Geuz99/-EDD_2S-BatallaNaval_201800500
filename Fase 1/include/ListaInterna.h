#ifndef LISTAINTERNA_H
#define LISTAINTERNA_H

#include"nodointerno.h"

#include <iostream>

using namespace std;


class ListaInterna
{
    public:
        nodointerno*Inicio;

    ListaInterna() {
        Inicio = NULL;
    }
    void InsertarFinal(int valor);
    void InsertarEnOrden(int valor);
    void Imprimir();

    private:
};

#endif // LISTAINTERNA_H
