#include "ArbolB.h"
#include <fstream>
#include <sstream>
#include <string>
#include <iostream>
using namespace std;

string ArbolB::buscar(string nick, string password){
    string info = buscarRamas(raiz , nick, password);
    return info;
}

string ArbolB::buscarRamas(NodoB*rama, string nick, string password){
    string aux = "";
    if (rama != NULL){
        aux = buscarConexionesRamas(rama, nick, password);
        NodoB* aux = rama;
        while(aux != NULL){
            if(aux->L != NULL){
                buscarRamas(aux->L, nick, password);
            }
            if(aux->sig == NULL){
                if(aux->R != NULL){
                    buscarRamas(aux->R, nick, password);
                }
            }
            aux = aux->sig;
        }
    }
    return aux;
}

string ArbolB::buscarConexionesRamas(NodoB*rama, string nick, string password){
    bool flag = false;
    if (rama != NULL){
        NodoB*aux = rama;
        do{
            if(aux->sig != NULL){
                if(aux->nick == nick && aux->password == password){
                    flag = true;
                }
                //cout<<aux->nick<<endl;
            }else{
                if(aux->nick == nick && aux->password == password){
                    flag = true;
                }
                //cout<<aux->nick<<endl;
            }
            aux = aux->sig;
        }while(aux != NULL && flag != true);
        if(!flag){
            return "not found";
        }
    }
    return "found";
}

string ArbolB::editar(string nick, string password, string nicknew, string passwordnew, string edadnew){   
    string flag = editar2(raiz, nick, password, nicknew, passwordnew, edadnew); 
    return flag;
}

string ArbolB::editar2(NodoB* rama, string nick, string password, string nicknew, string passwordnew, string edadnew){
    string aux = "";
    if (rama != NULL){
        aux = editar3(rama, nick, password, nicknew, passwordnew, edadnew);
        NodoB* aux = rama;
        while(aux != NULL){
            if(aux->L != NULL){
                editar2(aux->L, nick, password, nicknew, passwordnew, edadnew);
            }
            if(aux->sig == NULL){
                if(aux->R != NULL){
                    editar2(aux->R, nick, password, nicknew, passwordnew, edadnew);
                }
            }
            aux = aux->sig;
        }
    }
    return aux;
}

string ArbolB::editar3(NodoB* rama, string nick, string password, string nicknew, string passwordnew, string edadnew){
    bool flag = false;
    if (rama != NULL){
        NodoB*aux = rama;
        do{
            if(aux->sig != NULL){
                if(aux->nick == nick){
                    aux->nick = nicknew;
                    aux->password = passwordnew;
                    aux->edad = edadnew;
                    flag = true;
                }
                //cout<<aux->nick<<endl;
            }else{
                if(aux->nick == nick){
                    aux->nick = nicknew;
                    aux->password = passwordnew;
                    aux->edad = edadnew;
                    flag = true;
                }
                //cout<<aux->nick<<endl;
            }
            aux = aux->sig;
        }while(aux != NULL && flag != true);
        if(!flag){
            return "error";
        }
    }
    return "editado";
}

void ArbolB::insertar(int id, string nick, string password, string monedas, string edad) {
    NodoB* nodo = new NodoB(id, nick, password, monedas, edad);
    if (raiz == NULL) {
        raiz = nodo;
    } else {
        pair < NodoB*, pair<bool, bool>> ret = insertarCrearRama(nodo, raiz);
        NodoB* obj = ret.first;
        if ((ret.second.first || ret.second.second) && obj != NULL) {
            raiz = obj;
        }
    }
}

pair<NodoB*, pair<bool, bool>> ArbolB::insertarCrearRama(NodoB* nodo, NodoB* rama) {
    pair < NodoB*, pair<bool, bool>> ResultadoRama;
    ResultadoRama.first = NULL;
    ResultadoRama.second.first = false;
    ResultadoRama.second.second = false;
    if (esHoja(rama)) {
        pair < NodoB*, bool> resultado = insertarEnRama(rama, nodo);
        ResultadoRama.first = resultado.first;
        ResultadoRama.second.second = resultado.second;
        if (contador(resultado.first) == orden_arbol) {
            ResultadoRama.first = dividir(resultado.first);
            ResultadoRama.second.first = true;
        }
    } else {
        NodoB*temp = rama;
        do {
            if (nodo->id == temp->id) { //editado
                //cout << "insertarCrearRama(), El ID " << nodo->id << " ya existe\n";
                return ResultadoRama;
            } else if (nodo->id < temp->id) { //editado
                pair < NodoB*, pair<bool, bool>> ResultadoInsert = insertarCrearRama(nodo, temp->L);
                if (ResultadoInsert.second.second && ResultadoInsert.first != NULL) {
                    ResultadoRama.second.second = true;
                    temp->L = ResultadoInsert.first;
                }
                if (ResultadoInsert.second.first) {
                    pair < NodoB*, bool> auxInsert = insertarEnRama(rama, ResultadoInsert.first);
                    rama = auxInsert.first;
                    if (auxInsert.second) {
                        ResultadoRama.first = rama;
                    }
                    if (contador(rama) == orden_arbol) {
                        ResultadoRama.first = dividir(rama);
                        ResultadoRama.second.first = true;
                    }
                }
                return ResultadoRama;
            } else if (temp->sig == NULL) {
                pair < NodoB*, pair<bool, bool>> ResultadoInsert = insertarCrearRama(nodo, temp->R);
                if (ResultadoInsert.second.second && ResultadoInsert.first != NULL) {
                    ResultadoRama.second.second = true;
                    temp->R = ResultadoInsert.first;
                }
                if (ResultadoInsert.second.first) {
                    pair < NodoB*, bool> auxInsert = insertarEnRama(rama, ResultadoInsert.first);
                    rama = auxInsert.first;
                    if (auxInsert.second) {
                        ResultadoRama.first = rama;
                    }
                    if (contador(rama) == orden_arbol) {
                        ResultadoRama.first = dividir(rama);
                        ResultadoRama.second.first = true;
                    }
                }
                return ResultadoRama;
            }
            temp = temp->sig;
        } while (temp != NULL);
    }
    return ResultadoRama;
}

NodoB* ArbolB::dividir(NodoB* rama) {
    //int val = -999;
    //string nick;
    string password;
    NodoB*temp = NULL;
    NodoB*Nuevito = NULL;
    NodoB*aux = rama;

    NodoB*rderecha = NULL;
    NodoB*rizquierda = NULL;

    int cont = 0;
    while (aux != NULL) {
        cont++;
        if (cont < 3) {
            //val = aux->id;
            //nick = aux->nick;
            temp = new NodoB(aux->id, aux->nick, aux->password, aux->monedas, aux->edad);
            temp->L = aux->L;
            if (cont == 2) {
                temp->R = aux->sig->L;
            } else {
                temp->R = aux->R;
            }
            rizquierda = insertarEnRama(rizquierda, temp).first;
        } else if (cont == 3) {
            //val = aux->id;
            //nick = aux->nick;
            Nuevito = new NodoB(aux->id, aux->nick, aux->password, aux->monedas, aux->edad);
        } else {
            //val = aux->id;
            //nick = aux->nick;
            temp = new NodoB(aux->id, aux->nick, aux->password, aux->monedas, aux->edad);
            temp->L = aux->L;
            temp->R = aux->R;
            rderecha = insertarEnRama(rderecha, temp).first;
        }
        aux = aux->sig;
    }
    Nuevito->R = rderecha;
    Nuevito->L = rizquierda;
    return Nuevito;
}

pair<NodoB*, bool> ArbolB::insertarEnRama(NodoB* primero, NodoB* nuevo) {
    pair < NodoB*, bool> ret;
    ret.second = false;
    if (primero == NULL) {
        ret.second = true;
        primero = nuevo;
    } else {
        NodoB* aux = primero;
        while (aux != NULL) {
            if (aux->id == nuevo->id) {//------------->ya existe en el arbol
                //cout << "insertarEnRama(), El ID " << nuevo->id << " ya existe\n";
                break;
            } else {
                if (aux->id> nuevo->id) { //editado
                    if (aux == primero) {//------------->insertar al inicio
                        aux->prev = nuevo;
                        nuevo->sig = aux;
                        //ramas del nodo
                        aux->L = nuevo->R;
                        nuevo->R = NULL;
                        ret.second = true;
                        primero = nuevo;
                        break;
                    } else {//------------->insertar en medio;
                        nuevo->sig = aux;
                        //ramas del nodo
                        aux->L = nuevo->R;
                        nuevo->R = NULL;

                        nuevo->prev = aux->prev;
                        aux->prev->sig = nuevo;
                        aux->prev = nuevo;
                        break;
                    }
                } else if (aux->sig == NULL) {//------------->insertar al final
                    aux->sig = nuevo;
                    nuevo->prev = aux;
                    break;
                }
            }
            aux = aux->sig;
        }

    }
    ret.first = primero;

    return ret;
}

bool ArbolB::esHoja(NodoB* primero) {
    NodoB* aux = primero;
    while (aux != NULL) {
        if (aux->L != NULL || aux->R != NULL) {
            return false;
        }
        aux = aux->sig;
    }
    return true;
}

int ArbolB::contador(NodoB* primero) {
    int contador = 0;
    NodoB* aux = primero;
    while (aux != NULL) {
        contador++;
        aux = aux->sig;
    }
    return contador;
}

void ArbolB::Grafo() {
    string dotFull = "";

    dotFull += "digraph G {\n";
    dotFull += "node[shape=record]\n";
    dotFull += "\t\t//Agregar Nodos Rama\n";
    dotFull += GrafoArbolAbb(raiz);
    //agregar conexiones de ramas
    dotFull += "\t\t//Agregar conexiones\n";
    dotFull += GrafoConexionRamas(raiz);

    dotFull += "}";

    //------->escribir archivo
    ofstream file;
    file.open("C:/Users/GEUZ99/Desktop/[EDD_2S]BatallaNaval_201800500/-EDD_2S-BatallaNaval_201800500/Fase 1/arbolb.dot");
    file << dotFull;
    file.close();
}

string ArbolB::GrafoArbolAbb(NodoB* rama) {
    string dot = "";
    if (rama != NULL) {
        //agrear rama actual
        dot += GrafoRamas(rama);
        //agregar las ramas siguientes recursivamente
        NodoB*aux = rama;
        while (aux != NULL) {
            if (aux->L != NULL) {
                dot += GrafoArbolAbb(aux->L);
            }
            if (aux->sig == NULL) {
                if (aux->R != NULL) {
                    dot += GrafoArbolAbb(aux->R);
                }
            }
            aux = aux->sig;
        }
    }
    return dot;
}

string ArbolB::GrafoRamas(NodoB*rama) {
    string dot = "";
    stringstream auxTXT;
    if (rama != NULL) {
        //============================================agregar rama=================================
        NodoB*aux = rama;
        auxTXT.str("");
        auxTXT << rama;
        dot = dot + "R" + auxTXT.str() + "[label=\"";
        int r = 1;
        while (aux != NULL) {
            if (aux->L != NULL) {
                dot = dot + "<C" + to_string(r) + ">|";
                r++;
            }
            if (aux->sig != NULL) {
                dot = dot + to_string(aux->id) + " usr: " + aux->nick + "|";
            } else {
                dot = dot + to_string(aux->id) + " usr: " + aux->nick;
                if (aux->R != NULL) {
                    dot = dot + "|<C" + to_string(r) + ">";
                }
            }
            aux = aux->sig;
        }
        dot = dot + "\"];\n";
    }
    return dot;
}

string ArbolB::GrafoConexionRamas(NodoB*rama) {
    string dot = "";
    stringstream auxTXT;
    if (rama != NULL) {
        //============================================agregar rama=================================
        NodoB*aux = rama;
        auxTXT << rama;
        string actual = "R" + auxTXT.str();
        int r = 1;
        while (aux != NULL) {
            if (aux->L != NULL) {
                auxTXT.str("");
                auxTXT << aux->L;
                dot += actual + ":C" + to_string(r) + "->" + "R" + auxTXT.str() + ";\n";
                r++;
                dot += GrafoConexionRamas(aux->L);
            }
            if (aux->sig == NULL) {
                if (aux->R != NULL) {
                    auxTXT.str("");
                    auxTXT << aux->R;
                    dot += actual + ":C" + to_string(r) + "->" + "R" + auxTXT.str() + ";\n";
                    r++;
                    dot += GrafoConexionRamas(aux->R);
                }
            }
            aux = aux->sig;
        }
    }
    return dot;
}
