/*
 * Problem: Delete a Node
 * Author: Anirudha Bose <ani07nov@gmail.com>

   Delete Node at a given position in a linked list 
   Node is defined as 
     struct Node
     {
         int data;
         struct Node *next;
     }
 */

Node* Delete(Node *head, int position)
{
    if(head->next == NULL)
        return NULL;
    
    Node* list = new Node;
    list = head;
    
    int c = 0;
    Node* prev = new Node;
    while(c != position)
    {
        prev = list;
        list = list->next;
        c++;
    }
    if(c==0)
        return list->next;

    prev->next = list->next;
    
    return head;
}

