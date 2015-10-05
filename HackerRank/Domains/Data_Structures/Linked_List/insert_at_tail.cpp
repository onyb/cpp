/*
 * Problem: Insert a node at the tail of a linked list
 * Author: Anirudha Bose <ani07nov@gmail.com>

   Insert Node at the end of a linked list 
   head pointer input could be NULL as well for empty list
   Node is defined as 
     struct Node
     {
         int data;
         struct Node *next;
     }
 */

Node* Insert(Node *head,int data)
{
    Node *node = new Node;
    node->data = data;
    node->next = NULL;
    
    if(head == NULL)
        head = node;
    else
    {
        Node* list = new Node;
        list = head;
        while(list->next != NULL)
            list = list->next;

        list->next = node;
    }
    return head;
}
