#ifndef NODOINTERNO_H
#define NODOINTERNO_H

#include <stddef.h>


class nodointerno
{
    public:
        int valor;
        nodointerno*sig;
        nodosimple() {
        sig = NULL;
        valor = 0;
    }
    private:
};

#endif // NODOINTERNO_H
