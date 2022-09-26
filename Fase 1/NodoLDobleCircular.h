#ifndef NODOLDOBLECIRCULAR_H
#define NODOLDOBLECIRCULAR_H

#include<iostream>
#include<string>

using namespace std;

class NodoLDobleCircular
{
    public:
        string nick;
        string password;
        string monedas;
        string edad;
        NodoLDobleCircular *next;
        NodoLDobleCircular *prev;

        NodoLDobleCircular(string _nick, string _password, string _monedas, string _edad){
            this ->next = NULL;
            this ->prev = NULL;
            this ->nick = _nick;
            this ->password = _password;
            this ->monedas = _monedas;
            this ->edad = _edad;
        }

    protected:

    private:
};

#endif // NODOLDOBLECIRCULAR_H
