#include<iostream>
#include<fstream>
#include<nlohmann/json.hpp>
#include<string>

#include"LDobleCircular.h"
#include"ListaInterna.h"
#include"ListaPrincipal.h"

using namespace std;
using namespace nlohmann;


int main(int argc, char const *argv[])
{

    int opc = 0;
    LDobleCircular lista;
    ListaPrincipal pruebas;

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
                    //lista->insert(dato["usuarios"][i]["nick"].get<string>());
                    /*cout<<"nick:  "<<dato["usuarios"][i]["nick"].get<string>()<<endl;
                    cout<<"pass:  "<<dato["usuarios"][i]["password"].get<string>()<<endl;
                    cout<<"monedas:  "<<dato["usuarios"][i]["monedas"].get<string>()<<endl;
                    cout<<"edad:  "<<dato["usuarios"][i]["edad"].get<string>()<<endl;*/
                }
                /*for(int i=0;i<dato["articulos"].size();i++){
                    cout<<"id:  "<<dato["articulos"][i]["id"].get<string>()<<endl;
                    cout<<"categoria:  "<<dato["articulos"][i]["categoria"].get<string>()<<endl;
                    cout<<"precio:  "<<dato["articulos"][i]["precio"].get<string>()<<endl;
                    cout<<"nombre:  "<<dato["articulos"][i]["nombre"].get<string>()<<endl;
                    cout<<"src:  "<<dato["articulos"][i]["src"].get<string>()<<endl;*/
                lista.imprimir();
                }
            break;

        case 2:
            pruebas.Insertar("1", "10", "carro1", "carro1.png", "Epico");
            pruebas.Insertar("2", "100", "carro2", "carro2.png", "Epico");
            pruebas.Insertar("3", "1000", "carro3", "carro3.png", "Epico");

            pruebas.Insertar("1", "10", "moto1", "moto1.png", "Raro");
            pruebas.Insertar("2", "100", "moto2", "moto2.png", "Raro");
            pruebas.Insertar("3", "1000", "moto3", "moto3.png", "Raro");

            pruebas.Imprimir();

            break;
        case 3:
            cout<<"Login"<<endl;
            break;

        case 4:
            cout<<"Reportes"<<endl;
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

