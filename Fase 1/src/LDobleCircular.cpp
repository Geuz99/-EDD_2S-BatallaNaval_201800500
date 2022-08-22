#include "LDobleCircular.h"

#include<string>

using namespace std;

void LDobleCircular::insert(string nick, string password, string monedas, string edad){
    NodoLDobleCircular *nuevo = new NodoLDobleCircular(nick, password, monedas, edad);
    if ((head==NULL) && (end==NULL)){
        head = nuevo;
        end = nuevo;

    }else{
        end->next = nuevo;
        nuevo->prev = end;
        nuevo->next = head;
        head->prev = nuevo;
        end = nuevo;

    }

    this->size += 1;

}

void LDobleCircular::imprimir(){
    if ((head == NULL) && (end == NULL))
    {
        cout<<"<-->NULL<-->"<<endl;
    }else{
        NodoLDobleCircular *aux = head;
        do
        {
            cout<<" <--> "<<aux->nick;
            aux = aux->next;
        } while (aux != head);
        cout<<" <--> "<<aux->nick<<endl;
    }



}
