#ifndef LISTAPRINCIPAL_H
#define LISTAPRINCIPAL_H

#include <iostream>
#include<string>

#include "nodoprincipal.h"

using namespace std;


class ListaPrincipal
{
    public:
        nodoprincipal*Inicio;

        ListaPrincipal() {
            Inicio = NULL;
        }
        void Imprimir();
        void GenerarGrafo();
        void Insertar(string id, string precio, string nombre, string src, string categoria);
        nodoprincipal * BuscarPrincipal(nodoprincipal*inicioL, string categoria);

    private:
};

#endif // LISTAPRINCIPAL_H
