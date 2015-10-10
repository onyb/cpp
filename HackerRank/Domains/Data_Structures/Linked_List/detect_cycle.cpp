/*
 * Problem: Detect Cycle
 * Author: Anirudha Bose <ani07nov@gmail.com>

   Detect loop in a linked list 
   List could be empty also
   Node is defined as 
     struct Node
     {
         int data;
         struct Node *next;
     }
 */

int HasCycle(Node* head)
{
    Node *tortoise = new Node;
    Node *hare = new Node;
    
    tortoise = head;
    hare = head;
    
    while(tortoise != NULL && hare != NULL && hare->next != NULL)
    {
        tortoise = tortoise->next;
        hare = hare->next->next;
        
        if(tortoise == hare)
            return 1;
    }
    return 0;
}
