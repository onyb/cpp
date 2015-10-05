/*
 * Problem: Get Node Value
 * Author: Anirudha Bose <ani07nov@gmail.com>
 * Inspired by the cool solution by 'salcio'

   Get Nth element from the end in a linked list of integers
   Number of elements in the list will always be greater than N.
   Node is defined as 
     struct Node
     {
         int data;
         struct Node *next;
     }
 */

int GetNode(Node *head,int positionFromTail)
{
    Node *list = new Node;
    Node *list_delayed = new Node;
    
    int index = 0;
    
    list = head;
    list_delayed = head;
    
    while(list != NULL)
    {
        list = list->next;
        if(index++ > positionFromTail)
            list_delayed = list_delayed->next;
    }
    return list_delayed->data;
        
}
