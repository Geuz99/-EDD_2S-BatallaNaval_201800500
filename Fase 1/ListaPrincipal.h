#ifndef LISTAPRINCIPAL_H
#define LISTAPRINCIPAL_H

#include <iostream>
#include<string>
#include <vector>

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
        void ImprimirTienda();
        void GenerarGrafo();
        void Insertar(string id, string precio, string nombre, string src, string categoria);
        nodoprincipal * BuscarPrincipal(nodoprincipal*inicioL, string categoria);
        void Ascendente();
        void Descendente();
        string Categorias();
        string dameCategorias();
        string buscar(string categoria, string item);
        string dame_precio(string categoria, string item);
        string dame_id(string categoria, string item);

    private:
};

#endif // LISTAPRINCIPAL_H
