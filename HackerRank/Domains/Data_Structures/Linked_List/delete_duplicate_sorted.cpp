/*
 * Problem: Delete duplicate-value nodes from a sorted linked list
 * Author: Anirudha Bose <ani07nov@gmail.com>

   Remove all duplicate elements from a sorted linked list
   Node is defined as 
   struct Node
   {
       int data;
       struct Node *next;
   }
 */

Node* RemoveDuplicates(Node *head)
{
    if(head == NULL || head->next == NULL)
        return head;
    
    Node *list = new Node;
    list = head;
    
    while(list->next != NULL)
    {
        if(list->data == list->next->data)
            list->next = list->next->next;
        else
            list = list->next;
    }
    return head;
}
