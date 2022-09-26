#ifndef NODOB_H
#define NODOB_H

#include <stddef.h>
#include <iostream>
#include<string>

using namespace std;


class NodoB
{
    public:
        int id;
        string nick;
        string password;
        string monedas;
        string edad;

        NodoB* sig;
        NodoB* prev;

        NodoB* R;
        NodoB* L;

        NodoB(int _id, string _nick){
            sig = NULL;
            prev = NULL;
            R = NULL;
            L = NULL;
            id = _id;
            nick = _nick;
        }

    private:
};

#endif // NODOB_H
