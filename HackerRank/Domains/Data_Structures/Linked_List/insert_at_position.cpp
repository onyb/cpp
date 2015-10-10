/*
 * Problem: Insert a node at a specific position in a linked list
 * Author: Anirudha Bose <ani07nov@gmail.com>

   Insert Node at a given position in a linked list 
   head can be NULL 
   First element in the linked list is at position 0
     Node is defined as 
     struct Node
     {
         int data;
         struct Node *next;
     }
 */

Node* InsertNth(Node *head, int data, int position)
{
    Node* node = new Node;
    node->data = data;
    
    Node* list = new Node;
    list = head;
    
    if(head == NULL)
    {
        head = node;
        node->next = NULL;
        return head;
    }
    
    int c = 0;
    Node* prev = new Node;
    while(c != position)
    {
        prev = list;
        list = list->next;
        c++;
    }
    
    node->next = list;
    
    if(c==0)
        return node;
    else
        prev->next = node;

    return head;
}

