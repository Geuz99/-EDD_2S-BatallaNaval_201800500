#include "LDobleCircular.h"

#include<string>
#include<iostream>

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
    bool flag = false;
    if(head!=NULL){
        do{
            if(edit->nick==nick){
                edit->nick = nicknew;
                edit->password = passwordnew;
                edit->edad = edadnew;
                flag = true;
                cout<<"SE HA EDITADO CON EXITO"<<endl;
            }
            edit = edit->next;

        }while(edit!=head && flag != true);
        if(!flag){
            cout<<">ha ocurrido un error";
        }
    }
}

void LDobleCircular::buscar(string nick, string password){
    int opc = 0;
    NodoLDobleCircular *buscar;
    buscar = head;
    bool flag = false;
    if(head!=NULL){

        do{
            if(buscar->nick==nick && buscar->password==password){
                //login(nick, password);
                do
                {
                cout<<"****** BIENVENIDO "<<buscar->nick<<" *******"<<endl;
                cout<<"*                                  *"<<endl;
                cout<<"1. Editar informacion              *"<<endl;
                cout<<"2. Eliminar cuenta                 *"<<endl;
                cout<<"3. Ver tutorial                    *"<<endl;
                cout<<"4. Ver articulos de la tienda      *"<<endl;
                cout<<"5. Realizar movimientos            *"<<endl;
                cout<<"6. Salir al menu principal         *"<<endl;
                cout<<"************************************"<<endl;
                cin>>opc;

                switch (opc)
                {
                case 1:
                    {
                    string nicknew, passwordnew, edadnew;
                    cout<<"Ingrese nuevo nick: ";cin>>nicknew;
                    cout<<"Ingrese nuevo password: ";cin>>passwordnew;
                    cout<<"Ingrese nueva edad: ";cin>>edadnew;
                    editar(nick, password, nicknew, passwordnew, edadnew);
                    }
                    break;
                case 2:
                    {
                    string aux;
                    cout<<"Desea eliminar su cuenta permanentemente [y/n] "<<endl;cin>>aux;
                    if(aux=="y"){
                        eliminar(buscar->nick, buscar->password);
                        return;
                    }else if(aux=="n"){
                        break;
                    }else{
                        cout<<"si o no ????"<<endl;
                    }
                    }
                    break;
                case 3:
                    cout<<"TUTORIAL:"<<endl;
                    cout<<"     Tablero:"<<endl;
                    cout<<"         Ancho:"<<endl;
                    cout<<"         Alto:"<<endl;
                    cout<<"     Movimientos:"<<endl;
                    break;
                case 4:
                    cout<<"Tienda"<<endl;
                    break;
                case 5:
                    cout<<"Realizar movimientos"<<endl;
                    break;
                case 6:
                    break;
                default:
                    cout<<"Ingresa una opcion correcta"<<endl;
                    cout<<" ";
                    break;

                }
            }while (opc != 6);

                flag = true;
            }
            buscar = buscar->next;
        }while(buscar!=head && flag!=true);

        if(!flag){
            cout<<"EL NICK O LA CONTRASEIA NO EXISTE"<<endl;
        }
    }else{
        cout<<"NULL"<<endl;
    }

}

void LDobleCircular::eliminar(string nick, string password){
    NodoLDobleCircular *actual;
    NodoLDobleCircular *anterior;
    actual = head;
    anterior = NULL;
    bool flag = false;
    if (head!=NULL){
        do{
            if(actual->nick==nick && actual->password==password){
                if(actual==head){
                    head = head->next;
                    head->prev = end;
                    end->next = head;
                }else if(actual==end){
                    end = anterior;
                    end->next = head;
                    head->prev = end;
                }else{
                    anterior->next = actual->next;
                    actual->next->prev = anterior;
                }
                cout<<"CUENTA ELIMINADA"<<endl;
                flag = true;
            }
            anterior = actual;
            actual = actual->next;
        }while(actual!=head && flag!=true);
    }if(!flag){
        cout<<"HA OCURRIDO UN ERROR"<<endl;
    }

}



