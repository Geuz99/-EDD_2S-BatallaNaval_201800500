#ifndef LISTAPRINCIPAL_H
#define LISTAPRINCIPAL_H

#include <iostream>

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
        void Insertar(int valor, int categoria);
        nodoprincipal * BuscarPrincipal(nodoprincipal*inicioL, int categoria);

    private:
};

#endif // LISTAPRINCIPAL_H
