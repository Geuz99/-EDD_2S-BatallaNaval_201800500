#include<iostream>
#include<fstream>
#include<nlohmann/json.hpp>
#include<string>

#include"LDobleCircular.h"

using namespace std;
using namespace nlohmann;


int main(int argc, char const *argv[])
{

    int opc = 0;
    LDobleCircular *lista = new LDobleCircular();

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
                    lista->insert(dato["usuarios"][i]["nick"].get<string>());
                    cout<<dato["usuarios"][i]["nick"].get<string>();
                    //lista->insert(dato["usuarios"][i]["nick"].get<string>(),dato["usuarios"][i]["password"].get<string>(),dato["usuarios"][i]["monedas"].get<string>(),dato["usuarios"][i]["edad"].get<string>());
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
                lista->imprimir();
                }
            break;
        case 2:
            cout<<"Login"<<endl;
            break;

        case 3:
            cout<<"Login"<<endl;
            break;

        case 4:
            cout<<"Reportes"<<endl;
            break;

        default:
            cout<<"Ingresa una opción correcta"<<endl;
            cout<<" ";
            break;
        }

    } while (opc != 5);

    return 0;
}

