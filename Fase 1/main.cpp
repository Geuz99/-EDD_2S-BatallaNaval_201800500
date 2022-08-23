#include<iostream>
#include<fstream>
#include<nlohmann/json.hpp>
#include<string>

#include"LDobleCircular.h"
#include"ListaInterna.h"
#include"ListaPrincipal.h"
#include"Cola.h"

using namespace std;
using namespace nlohmann;


int main(int argc, char const *argv[])
{

    int opc = 0;
    LDobleCircular lista;
    ListaPrincipal listaArticulos;
    Cola colaTuto;

    do
    {
        cout<<"********** Menu **********"<<endl;
        cout<<"*                        *"<<endl;
        cout<<"1. Carga masiva          *"<<endl;
        cout<<"2. Registrar usuario     *"<<endl;
        cout<<"3. Login                 *"<<endl;
        cout<<"4. Reportes              *"<<endl;
        cout<<"5. Salir del juego       *"<<endl;
        cout<<"**************************"<<endl;
        cin>>opc;

        switch (opc)
        {
        case 1:
            {
                ifstream archivo("C:/Users/GEUZ99/Downloads/prueba.json");
                json dato = json::parse(archivo);
                for(int i=0;i<dato["usuarios"].size();i++){
                    lista.insert(dato["usuarios"][i]["nick"].get<string>(),dato["usuarios"][i]["password"].get<string>(),dato["usuarios"][i]["monedas"].get<string>(),dato["usuarios"][i]["edad"].get<string>());

                }
                for(int i=0;i<dato["articulos"].size();i++){
                    listaArticulos.Insertar(dato["articulos"][i]["id"].get<string>(),dato["articulos"][i]["precio"].get<string>(), dato["articulos"][i]["nombre"].get<string>(), dato["articulos"][i]["src"].get<string>(),dato["articulos"][i]["categoria"].get<string>());

                }
                string ancho = dato["tutorial"]["ancho"].get<string>();
                string alto = dato["tutorial"]["alto"].get<string>();
                for(int i=0;i<dato["tutorial"]["movimientos"].size();i++){
                    colaTuto.push(alto, ancho, dato["tutorial"]["movimientos"][i]["x"].get<string>(), dato["tutorial"]["movimientos"][i]["y"].get<string>());
                }
                /*lista.imprimir();
                cout<<" "<<endl;
                listaArticulos.Imprimir();*/
                //colaTuto.Imprimir();
            }
            break;

        case 2:
            {

            string nick="", password="", monedas="", edad="";
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
              lista.buscar(nick, password);
            }
            break;

        case 4:
            lista.imprimir();
            cout<<" "<<endl;
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

    return 0;
}

