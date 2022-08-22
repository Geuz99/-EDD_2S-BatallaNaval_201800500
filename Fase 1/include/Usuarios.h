#ifndef USUARIOS_H
#define USUARIOS_H

#include<stddef.h>
#include<iostream>
#include<string>

using namespace std;


class Usuarios
{
    public:
        string nick;
        string password;
        string monedas;
        string edad;

        Usuarios(string _nick, string _password, string _monedas, string _edad){
            this->nick = _nick;
            this->password = _password;
            this->monedas = _monedas;
            this->edad = _edad;
        }

        virtual ~Usuarios();


    protected:

    private:
};

#endif // USUARIOS_H
