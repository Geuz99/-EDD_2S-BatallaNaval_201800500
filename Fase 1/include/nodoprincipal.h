#ifndef NODOPRINCIPAL_H
#define NODOPRINCIPAL_H

#include <stddef.h>
#include <string>

#include "ListaInterna.h"

using namespace std;


class nodoprincipal
{
    public:
    //----valores
    ListaInterna listainterna;
    string valor;
    //----apuntadores
    nodoprincipal*sig;

    nodoprincipal() {
        sig = NULL;
        valor = "";
    }
    private:
};

#endif // NODOPRINCIPAL_H
