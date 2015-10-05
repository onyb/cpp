/*
 * Problem: Print the elements of a linked list
 * Author: Anirudha Bose <ani07nov@gmail.com>

   Print elements of a linked list on console 
   head pointer input could be NULL as well for empty list
   Node is defined as 
     struct Node
     {
         int data;
         struct Node *next;
     }
 */

#include <iostream>
using namespace std;

void Print(Node *head)
{
    while(head != NULL)
    {
        cout << head->data << endl;
        head = head->next;
    }
}
