#include<iostream>
#include<fstream>
#include<nlohmann/json.hpp>
#include<string>

#include"LDobleCircular.cpp"
#include"ListaInterna.cpp"
#include"ListaPrincipal.cpp"
#include"Cola.cpp"
#include"Pila.cpp"
#include"Lista.cpp"
#include"ArbolB.cpp"
#include "crow.h"

using namespace std;
using json = nlohmann::json;

int opc = 0;
LDobleCircular lista;
ListaPrincipal listaArticulos;
Cola colaTuto;
Pila pilaMov;
Lista listaMov;
int id_usuarios = 0;
int id_tutorial = 0;    
ArbolB tree;
crow::SimpleApp app;

int main(int argc, char const *argv[])
{    
    CROW_ROUTE(app, "/tutorial")([](){ 
        string info = colaTuto.Tutorial();
        return info;
    });

    CROW_ROUTE(app, "/arbolb")([](){        
        tree.Grafo();   
        return "C:/Users/GEUZ99/Desktop/[EDD_2S]BatallaNaval_201800500/-EDD_2S-BatallaNaval_201800500/Fase 1/arbolb.dot";
    });

    CROW_ROUTE(app, "/carga/<path>")([](string path){
        ifstream archivo(path);  
        json dato = json::parse(archivo);
        for(int i=0;i<dato["usuarios"].size();i++){              
            tree.insertar(id_usuarios, dato["usuarios"][i]["nick"].get<string>(), dato["usuarios"][i]["password"].get<string>(),dato["usuarios"][i]["monedas"].get<string>(),dato["usuarios"][i]["edad"].get<string>());
            lista.insertar(dato["usuarios"][i]["nick"].get<string>(), dato["usuarios"][i]["password"].get<string>(),dato["usuarios"][i]["monedas"].get<string>(),dato["usuarios"][i]["edad"].get<string>());
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
        return "Cargado con exito";
    });

    CROW_ROUTE(app, "/login/<string>/<string>")([](string user, string password){              
        if (lista.buscar(user, password) == "found"){
            return "correcto";
        }else{
            return "incorrecto";
        }
        
    });

    CROW_ROUTE(app, "/login/tokens/<string>/<string>")([](string user, string password){              
        return lista.dame_tokens(user, password);
        
    });

    CROW_ROUTE(app, "/login/editar/<string>/<string>/<string>/<string>/<string>")([](string user, string password, string nicknew, string passwordnew, string edadnew){              
        string info = lista.editar2(user, password, nicknew, passwordnew, edadnew);       
        return info;
        
    });

    CROW_ROUTE(app, "/login/eliminar/<string>/<string>")([](string user, string password){              
        if(lista.eliminar2(user, password) == "eliminado"){
            return "correcto";
        }else{
            return "incorrecto";
        }        
    });

    CROW_ROUTE(app, "/usuarios/ascendente")([](){    
        string data = lista.Ascendente2();   
        return data;
    });

    CROW_ROUTE(app, "/usuarios/descendente")([](){    
        string data = lista.Descendente2();   
        return data;
    });

    CROW_ROUTE(app, "/tienda")([](){    
        string data = listaArticulos.Categorias();           
        return  data;
    });

    CROW_ROUTE(app, "/categorias")([](){    
        string data = listaArticulos.dameCategorias();           
        return data;
    });

    app.port(18080).run();    



    do
    {
        cout<<"             ********** Menu **********"<<endl;
        cout<<"             *                        *"<<endl;
        cout<<"             1.   Carga masiva        *"<<endl;
        cout<<"             2.   Registrar usuario   *"<<endl;
        cout<<"             3.   Login               *"<<endl;
        cout<<"             4.   Reportes            *"<<endl;
        cout<<"             5.   Salir del juego     *"<<endl;
        cout<<"             *                        *"<<endl;
        cout<<"             **************************"<<endl;
        cin>>opc;

        switch (opc)
        {
        case 1:
            {                              
                ifstream archivo("C:/Users/GEUZ99/Downloads/prueba.json");                
                json dato = json::parse(archivo);
                for(int i=0;i<dato["usuarios"].size();i++){
                    lista.insertar(dato["usuarios"][i]["nick"].get<string>(),dato["usuarios"][i]["password"].get<string>(),dato["usuarios"][i]["monedas"].get<string>(),dato["usuarios"][i]["edad"].get<string>());
                    
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
            lista.insertar(nick, password, monedas, edad);
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
            cout<<"SEE YOU SOON"<<endl;
            break;

        default:
            cout<<"Ingresa una opcion correcta"<<endl;
            cout<<" ";
            break;
        }

    } while (opc != 5);
    
    remove("C:/Users/GEUZ99/Desktop/[EDD_2S]BatallaNaval_201800500/-EDD_2S-BatallaNaval_201800500/Fase 1/Usuarios.dot");
    remove("Usuarios.png");
    remove("Articulos.dot");
    remove("Articulos.png");
    remove("Tutorial.dot");
    remove("Tutorial.png");
    remove("arbolb.dot");
    remove("arbolb.png");
    
    return 0;
}

