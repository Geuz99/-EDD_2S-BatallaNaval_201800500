#ifndef NODOPRINCIPAL_H
#define NODOPRINCIPAL_H

#include <stddef.h>

#include "ListaInterna.h"


class nodoprincipal
{
    public:
    //----valores
    ListaInterna listainterna;
    int valor;
    //----apuntadores
    nodoprincipal*sig;

    nodoprincipal() {
        sig = NULL;
        valor = 0;
    }
    private:
};

#endif // NODOPRINCIPAL_H
