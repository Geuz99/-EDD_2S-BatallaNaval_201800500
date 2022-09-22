#include<iostream>
#include<fstream>
#include<nlohmann/json.hpp>
#include<string>

#include"LDobleCircular.h"
#include"ListaInterna.h"
#include"ListaPrincipal.h"
#include"Cola.h"
#include"Pila.h"
#include"Lista.h"
#include"ArbolB.h"

using namespace std;
using namespace nlohmann;


int main(int argc, char const *argv[])
{

    int opc = 0;
    LDobleCircular lista;
    ListaPrincipal listaArticulos;
    Cola colaTuto;
    Pila pilaMov;
    Lista listaMov;
    int id_usuarios = 0;
    int id_tutorial = 0;
    ArbolB tree;



    do
    {
        cout<<"********** Menu **********"<<endl;
        cout<<"*                        *"<<endl;
        cout<<"1. Carga masiva          *"<<endl;
        cout<<"2. Registrar usuario     *"<<endl;
        cout<<"3. Login                 *"<<endl;
        cout<<"4. Reportes              *"<<endl;
        cout<<"5. Salir del juego       *"<<endl;
        cout<<"*                        *"<<endl;
        cout<<"**************************"<<endl;
        cin>>opc;

        switch (opc)
        {
        case 1:
            {
                string path;
                //cout<<"Ingrese la ruta del archivo: ";cin>>path;
                //cout<<endl;
                //"C:/Users/GEUZ99/Downloads/prueba.json"
                ifstream archivo("C:/Users/GEUZ99/Downloads/prueba.json");
                json dato = json::parse(archivo);
                for(int i=0;i<dato["usuarios"].size();i++){
                    lista.insert(dato["usuarios"][i]["nick"].get<string>(),dato["usuarios"][i]["password"].get<string>(),dato["usuarios"][i]["monedas"].get<string>(),dato["usuarios"][i]["edad"].get<string>());
                    tree.insertar(id_usuarios, dato["usuarios"][i]["nick"].get<string>());
                    id_usuarios++;
                }
                for(int i=0;i<dato["articulos"].size();i++){
                    listaArticulos.Insertar(dato["articulos"][i]["id"].get<string>(),dato["articulos"][i]["precio"].get<string>(), dato["articulos"][i]["nombre"].get<string>(), dato["articulos"][i]["src"].get<string>(),dato["articulos"][i]["categoria"].get<string>());

                }
                string ancho = dato["tutorial"]["ancho"].get<string>();
                string alto = dato["tutorial"]["alto"].get<string>();
                for(int i=0;i<dato["tutorial"]["movimientos"].size();i++){
                    colaTuto.push(alto, ancho, dato["tutorial"]["movimientos"][i]["x"].get<string>(), dato["tutorial"]["movimientos"][i]["y"].get<string>(), id_tutorial);
                    id_tutorial++;
                }
            }
            break;

        case 2:
            {

            string nick="", password="", monedas="0", edad="";
            cout<<"********** Registrarse **********"<<endl;
            cout<<">Ingrese su nick: ";cin>>nick;
            cout<<">Ingrese su contrasenia: ";cin>>password;
            cout<<">Ingrese su edad: ";cin>>edad;
            lista.insert(nick, password, monedas, edad);
            cout<<"*********************************"<<endl;

            }
            break;
        case 3:
            {
              string nick="";
              string password="";
              cout<<"************* LOGIN *************"<<endl;
              cout<<"*Nick: ";cin>>nick;
              cout<<"*Password: ";cin>>password;
              cout<<"*********************************"<<endl;
              lista.buscar(nick, password, colaTuto, listaArticulos, pilaMov);
            }
            break;

        case 4:
            lista.GenerarGrafo();
            listaArticulos.GenerarGrafo();
            colaTuto.GenerarGrafo();
            pilaMov.GenerarGrafo2();
            cout<<"****************** USUARIOS ASCENDENTES ******************"<<endl;
            lista.Ascendente();
            cout<<"****************** USUARIOS DESCENDENTE ******************"<<endl;
            lista.Descendente();
            tree.Grafo();
            break;

        case 5:
            cout<<"***************************************************************"<<endl;
            break;

        default:
            cout<<"Ingresa una opcion correcta"<<endl;
            cout<<" ";
            break;
        }

    } while (opc != 5);
    remove("Usuarios.dot");
    remove("Usuarios.png");
    remove("Articulos.dot");
    remove("Articulos.png");
    remove("arbolb.dot");
    remove("arbolb.png");
    remove("Tutorial.dot");
    remove("Tutorial.png");
    return 0;
}

