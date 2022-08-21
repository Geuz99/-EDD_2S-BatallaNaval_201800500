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
            ifstream archivo("C:/Users/GEUZ99/Downloads/ejemplo1.json");
            nlohmann::json  dato= nlohmann::json::parse(archivo);
            for(int i=0;i<dato["usuarios"].size();i++){
                cout<<"nick:  "<<dato["usuarios"][i]["nick"].get<string>()<<endl;
                cout<<"pass:  "<<dato["usuarios"][i]["password"].get<string>()<<endl;
            }
            break;
            }
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

