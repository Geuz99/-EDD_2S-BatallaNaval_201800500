#ifndef NODOPILA_H
#define NODOPILA_H

#include <stddef.h>
#include<string>

class NodoPila
{
    public:
        int x;
        int y;
        NodoPila *next;
        NodoPila(int _x, int _y){
            x = _x;
            y = _y;
            next = NULL;
        }



    private:
};

#endif // NODOPILA_H
