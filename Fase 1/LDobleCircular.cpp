#include"LDobleCircular.h"
#include"Cola.h"

#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;
Cola cola;

void LDobleCircular::insertar(string nick, string password, string monedas, string edad){
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

string LDobleCircular::editar2(string nick, string password, string nicknew, string passwordnew, string edadnew){
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
            }
            edit = edit->next;

        }while(edit!=head && flag != true);
        if(!flag){
            return "Error";
        }
    }
    return "Editado";
}

string LDobleCircular::buscar(string nick, string password){
    NodoLDobleCircular *buscar;
    buscar = head;
    bool flag = false;
    if(head!=NULL){
        do{
            cout<<buscar->nick<<" "<<buscar->password<<endl;
            if(buscar->nick==nick && buscar->password==password){
                flag = true;               
            }
            buscar = buscar->next;
        }while(buscar!=head && flag!=true);
        if(!flag){
            return "not found";
        }
    }        
    return "found";
}

void LDobleCircular::buscar(string nick, string password, Cola colaTuto, ListaPrincipal listaArticulos, Pila pilaMov){
    int opc = 0;
    NodoLDobleCircular *buscar;
    buscar = head;
    bool flag = false;
    if(head!=NULL){

        do{
            if(buscar->nick==nick && buscar->password==password){

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
                        cout<<"Cuenta no eliminada";
                        }
                    }
                    break;
                case 3:
                    {
                    colaTuto.ImprimirTuto();
                    }
                    break;
                case 4:
                    {
                    listaArticulos.ImprimirTienda();
                    }
                    break;
                case 5:
                    {
                    int mov = 0;
                    int x,y;
                    string name = "";
                    cout<<"Realizar movimientos"<<endl;
                    cout<<"Cuantos movimientos desea realizar: "<<endl;cin>>mov;
                    for(int i=0;i<mov;i++){
                        cout<<i+1<<"- "<<" (x,y) ";cin>>x;cin>>y;
                        cout<<"";
                        pilaMov.push(x,y);
                    }
                    pilaMov.GenerarGrafo();
                    cout<<"Nombre para guardar los movimientos: "<<endl;cin>>name;
                    }
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
        cout<<"BASE DE DATOS VACIA..."<<endl;
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

void LDobleCircular::GenerarGrafo(){
    string dot = "";

    dot = dot + "digraph G {\n";
    dot = dot + "label=\"Usuarios\";\n";
    dot = dot + "node [shape=component, style=filled, color=blue, fillcolor=lightsteelblue1];\n";
    NodoLDobleCircular *aux = head;
    do{
        dot = dot + aux->nick + "[label=\"" + "nick: " + aux->nick + "\npassword: " + aux->password + "\nedad: " + aux->edad + "\nmonedas: " + aux->monedas + "\"];\n";
        aux = aux->next;

    }while (aux != head);
    dot = dot + "//Enlazar Usuarios\n";
    dot = dot + "{rank=same;\n";
    aux = head;
    do{
        dot = dot + aux->nick;
        if (aux->next != NULL) {
            dot = dot + "->";
        }
        aux = aux->next;
    }while (aux != head);
    dot = dot + head->nick + "\n";
    aux = head;
    do{
        dot = dot + aux->next->nick;
        if (aux->next != NULL) {
            dot = dot + "->";
            dot = dot + aux->nick + " ";
        }
        aux = aux->next;
    }while (aux != head);
    dot = dot + "\n";
    dot = dot + "}\n";
    dot = dot + "}\n";
    //cout<<dot;

     //------->escribir archivo
    ofstream file;
    file.open("C:/Users/GEUZ99/Desktop/[EDD_2S]BatallaNaval_201800500/-EDD_2S-BatallaNaval_201800500/Fase 1/Usuarios.dot");
    file << dot;
    file.close();

    //------->generar png
    system(("dot -Tpng Usuarios.dot -o  Usuarios.png"));

    //------>abrir archivo
    system(("Usuarios.png"));

}

void LDobleCircular::Ascendente(){
    NodoLDobleCircular *aux = head;
    NodoLDobleCircular *tem;
    string nick, password, monedas, edad;
    do{
        tem = aux->next;
        while(tem!=head){
            if(stoi(aux->edad) > stoi(tem->edad)){
                nick = aux->nick;
                password = aux->password;
                monedas = aux->monedas;
                edad = aux->edad;

                aux->nick = tem->nick;
                aux->password = tem->password;
                aux->monedas = tem->monedas;
                aux->edad = tem->edad;

                tem->nick = nick;
                tem->password = password;
                tem->monedas = monedas;
                tem->edad = edad;
            }
            tem = tem->next;
        }
        aux = aux->next;
        tem = aux->next;
    }while(tem!=head);
    aux = head;
    do
        {
            cout<<"nick: "<<aux->nick<<", password: "<<aux->password<<", monedas: "<<aux->monedas<<", edad: "<<aux->edad<<endl;
            aux = aux->next;
        } while (aux != head);
}

string LDobleCircular::Ascendente2(){
    NodoLDobleCircular *aux = head;
    NodoLDobleCircular *tem;
    string nick, password, monedas, edad;
    string data = "";
    do{
        tem = aux->next;
        while(tem!=head){
            if(stoi(aux->edad) > stoi(tem->edad)){
                nick = aux->nick;
                password = aux->password;
                monedas = aux->monedas;
                edad = aux->edad;

                aux->nick = tem->nick;
                aux->password = tem->password;
                aux->monedas = tem->monedas;
                aux->edad = tem->edad;

                tem->nick = nick;
                tem->password = password;
                tem->monedas = monedas;
                tem->edad = edad;
            }
            tem = tem->next;
        }
        aux = aux->next;
        tem = aux->next;
    }while(tem!=head);
    aux = head;
    do
        {
            data = data + "nick: " + aux->nick + ", password: " + aux->password + ", monedas: " + aux->monedas + ", edad: " + aux->edad + "\n";
            aux = aux->next;
        } while (aux != head);
    return data;
}

void LDobleCircular::Descendente(){
    NodoLDobleCircular *aux = head;
    NodoLDobleCircular *tem;
    string nick, password, monedas, edad;
    do{
        tem = aux->next;
        while(tem!=head){
            if(stoi(aux->edad) < stoi(tem->edad)){
                nick = aux->nick;
                password = aux->password;
                monedas = aux->monedas;
                edad = aux->edad;

                aux->nick = tem->nick;
                aux->password = tem->password;
                aux->monedas = tem->monedas;
                aux->edad = tem->edad;

                tem->nick = nick;
                tem->password = password;
                tem->monedas = monedas;
                tem->edad = edad;
            }
            tem = tem->next;
        }
        aux = aux->next;
        tem = aux->next;
    }while(tem!=head);
    aux = head;
    do
        {
            cout<<"nick: "<<aux->nick<<", password: "<<aux->password<<", monedas: "<<aux->monedas<<", edad: "<<aux->edad<<endl;
            aux = aux->next;
        } while (aux != head);
}

string LDobleCircular::Descendente2(){
    NodoLDobleCircular *aux = head;
    NodoLDobleCircular *tem;
    string nick, password, monedas, edad;
     string data = "";
    do{
        tem = aux->next;
        while(tem!=head){
            if(stoi(aux->edad) < stoi(tem->edad)){
                nick = aux->nick;
                password = aux->password;
                monedas = aux->monedas;
                edad = aux->edad;

                aux->nick = tem->nick;
                aux->password = tem->password;
                aux->monedas = tem->monedas;
                aux->edad = tem->edad;

                tem->nick = nick;
                tem->password = password;
                tem->monedas = monedas;
                tem->edad = edad;
            }
            tem = tem->next;
        }
        aux = aux->next;
        tem = aux->next;
    }while(tem!=head);
    aux = head;
    do
        {
            data = data + "nick: " + aux->nick + ", password: " + aux->password + ", monedas: " + aux->monedas + ", edad: " + aux->edad + "\n";
            aux = aux->next;
        } while (aux != head);

    return data;
}





