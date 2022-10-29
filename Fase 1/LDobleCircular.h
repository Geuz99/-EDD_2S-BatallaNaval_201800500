#ifndef LDOBLECIRCULAR_H
#define LDOBLECIRCULAR_H

#include<stddef.h>
#include<iostream>
#include<string>

#include "NodoLDobleCircular.h"
#include"ListaPrincipal.h"
#include"Cola.h"
#include"Pila.h"
#include"Lista.h"

using namespace std;

class LDobleCircular
{
    public:
        NodoLDobleCircular *head;
        NodoLDobleCircular *end;
        int size = 0;

        LDobleCircular(){
            this->head = NULL;
            this->end = NULL;
        }
        void insertar(string nick, string password, string monedas, string edad);
        void imprimir();
        void editar(string nick, string password, string nicknew, string passwordnew, string edadnew);
        string editar2(string nick, string password, string nicknew, string passwordnew, string edadnew);
        void buscar(string nick, string password, Cola colaTuto, ListaPrincipal listaArticulos, Pila pilaMov);
        void eliminar(string nick, string password);
        string eliminar2(string nick, string password);
        void GenerarGrafo();
        void Ascendente();
        string Ascendente2();
        void Descendente();   
        string Descendente2();
        string buscar(string nick, string password);
    private:
};

#endif // LDOBLECIRCULAR_H
