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

void LDobleCircular::editar(string nick, string password, string nicknew, string passwordnew, string edadnew){
    NodoLDobleCircular *edit;
    edit = head;
    int contar = size;

    while(contar!=0){
        if((edit!=head)){
            if((nick==edit->nick)&&(password==edit->password)){
                edit->nick = nicknew;
                edit->password = passwordnew;
                edit->edad = edadnew;
            }
            edit = edit->next;
            contar -= 1;
        }else{
            break;
        }
    }
}

void LDobleCircular::buscar(string nick, string password){
    NodoLDobleCircular *buscar;
    int flag = 0;

    while(buscar!=NULL){
        if((buscar->nick==nick) && (buscar->password==password)){
           cout<<"entraste"<<endl;
           flag = 1;

        }
        buscar = buscar->next;

        }
        if(flag==0){
            cout<<"nick no encontrado"<<endl;
        }

}

