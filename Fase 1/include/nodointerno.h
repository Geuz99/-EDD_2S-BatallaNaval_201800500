#ifndef NODOINTERNO_H
#define NODOINTERNO_H

#include <stddef.h>
#include<string>

using namespace std;

class nodointerno
{
    public:
        string id;
        string precio;
        string nombre;
        string src;
        nodointerno*sig;
        nodosimple() {
        sig = NULL;
        id = "";
        precio = "";
        nombre = "";
        src = "";
    }
    private:
};

#endif // NODOINTERNO_H
