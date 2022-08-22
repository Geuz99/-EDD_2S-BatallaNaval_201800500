#ifndef LISTAINTERNA_H
#define LISTAINTERNA_H

#include"nodointerno.h"

#include <iostream>
#include<string>

using namespace std;


class ListaInterna
{
    public:
        nodointerno*Inicio;

    ListaInterna() {
        Inicio = NULL;
    }
    void InsertarFinal(string id, string precio, string nombre, string src);
    //void InsertarEnOrden(string id, string precio, string nombre, string src);
    void Imprimir();

    private:
};

#endif // LISTAINTERNA_H
