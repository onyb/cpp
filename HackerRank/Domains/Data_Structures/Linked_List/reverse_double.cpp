/*
 * Problem: Reverse a doubly linked list
 * Author: Anirudha Bose <ani07nov@gmail.com>

   Reverse a doubly linked list, input list may also be empty
   Node is defined as
     struct Node
     {
         int data;
         Node *next;
         Node *prev;
     }
 */

#include <algorithm>

Node* Reverse(Node* head)
{
    Node* list = new Node;
    list = head;
    while(list != NULL)
    {
        swap(list->next, list->prev);
        head = list;
        list = list->prev;
    }
    return head;
}
