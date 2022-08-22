#ifndef NODOPRINCIPAL_H
#define NODOPRINCIPAL_H

#include <stddef.h>

class NodoPrincipal
{
    public:
        ListaInterna listaInterna;
        int valor;
        NodoPrincipal *next;
        NodoPrincipal(){
            next = NULL;
            valor = 0;
        }
        virtual ~NodoPrincipal();

    protected:

    private:
};

#endif // NODOPRINCIPAL_H
