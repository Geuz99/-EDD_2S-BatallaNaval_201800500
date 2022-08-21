#include "LDobleCircular.h"
#include"Usuarios.h"

void LDobleCircular::insert(string data){
    NodoLDobleCircular *nuevo = new NodoLDobleCircular(data);
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
            cout<<" <--> "<<aux->data;
            aux = aux->next;
        } while (aux != head);
        cout<<" <-->NULL<-->";
    }



}
