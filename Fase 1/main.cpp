#include<iostream>

using namespace std;

int main(int argc, char const *argv[])
{

    int opc = 0;

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

            break;

        case 2:
            cout<<"hola";
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

