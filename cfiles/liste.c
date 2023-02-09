#include<stdio.h>
#include<stdlib.h>


struct Knoten
{
    int data;
   struct Knoten* next;

};

struct Knoten* kopf = NULL;

void insert(int data)
{
    struct Knoten* newKnoten = malloc(sizeof(newKnoten));
    newKnoten->data = data;
    newKnoten->next = kopf;
    kopf = newKnoten;
}

void ausgeben()
{
    struct Knoten* p = kopf;
        while(p!=NULL)
        {
            printf("%d, ",p->data);
            p = p->next;
        }

}



int main ()
{
    insert(1);
    insert(42);
    insert(69);
    insert(107);
    insert(88);

    ausgeben();


}