#include "Cola.h"

#include<string>
#include<iostream>
#include <fstream>
#include <sstream>

using namespace std;

void Cola::push(string alto, string ancho, string x, string y){
    NodoCola *nuevo = new NodoCola(alto, ancho, x, y);
    if (head==NULL){
        head = nuevo;
        head->next = NULL;
        end = head;
    }else{
        end->next = nuevo;
        nuevo->next = NULL;
        end = nuevo;
    }

}

void Cola::pop(){
    NodoCola *actual;
    actual = head;
    NodoCola *anterior;
    anterior = NULL;
    bool flag = false;
    if(head!=NULL){
        while(actual!=NULL && flag!=true)
        {
            if(actual==head){
                head = head->next;
            }else if(actual==end){
                anterior->next = NULL;
                end = anterior;

            }else{
                anterior->next = actual->next;

            }
            flag = true;

        }
    }
    anterior = actual;
    actual = actual->next;

}

void Cola::ImprimirTuto() {
    NodoCola *aux = head;
    cout<<"-------------------------------------------"<<endl;
    cout<<"TUTORIAL:"<<endl;
    cout<<"     Tablero:"<<endl;
    cout<<"         Ancho: "<<aux->ancho<<endl;
    cout<<"         Alto: "<<aux->alto<<endl;
    cout<<"     Movimientos:"<<endl;
    while (aux != NULL) {
        cout <<"<-(" << aux->x << ","<< aux->y<< ")<-";
        aux = aux->next;
    }
    cout<<""<<endl;
    cout<<"-------------------------------------------"<<endl;
}

void Cola::GenerarGrafo(){
    string dot = "";
    dot = dot + "digraph G {\n";
    dot = dot + "node [shape=Msquare, color=seagreen1];\n";
    NodoCola *aux = head;
    dot = dot + "//agregar nodos\n";
    while (aux != NULL) {
        dot = dot + "\"" + aux->x+ "," + aux->y + "\"" + "[label=\"" + "x: " + aux->x + "\ny: " + aux->y + "\"];\n";
        aux = aux->next;
    }
    dot = dot + "{rank=same;\n";
    aux = head;
    while (aux != NULL) {

        dot = dot + "\"" + aux->x+ "," + aux->y + "\"";
        if (aux->next != NULL) {
            dot = dot + "->";
        }
        aux = aux->next;
    }
    dot = dot + "}\n";
    dot = dot + "}\n";

    //cout << dot;
    //------->escribir archivo
    ofstream file;
    file.open("Tutorial.dot");
    file << dot;
    file.close();

    //------->generar png
    system(("dot -Tpng Tutorial.dot -o  Tutorial.png"));

    //------>abrir archivo
    system(("Tutorial.png"));

}
