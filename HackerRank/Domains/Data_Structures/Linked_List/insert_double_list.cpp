/*
 * Problem: Insert a node into a sorted doubly linked list
 * Author: Anirudha Bose <ani07nov@gmail.com>

   Insert Node in a doubly sorted linked list 
   After each insertion, the list should be sorted
   Node is defined as
     struct Node
     {
         int data;
         Node *next;
         Node *prev;
     }
 */

Node* SortedInsert(Node *head,int data)
{
    Node* list = new Node;
    list = head;

    Node* node = new Node;
    node->data = data;
    node->next = NULL;
    node->prev = NULL;
 
    if(head == NULL)
        return node;
    
    if(node->data < head->data)
    {
        node->next = head;
        head->prev = node;
        return node;
    }

    while(list->next != NULL && node->data >= list->next->data)
        list = list->next;
    
    node->prev = list;
    node->next = list->next;

    if(list->next != NULL)
        list->next->prev = node;

    list->next = node;
    
    return head;
}
