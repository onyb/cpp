/*
 * Problem: Merge two sorted linked lists
 * Author: Anirudha Bose <ani07nov@gmail.com>

   Merge two sorted lists A and B as one linked list
   Node is defined as 
   struct Node
   {
       int data;
       struct Node *next;
   }
 */

Node* MergeLists(Node *headA, Node* headB)
{
    Node *result = new Node;
    
    if(headA == NULL)
        return headB;
    
    if(headB == NULL)
        return headA;
    
    if(headA->data <= headB->data)
    {
        result = headA;
        result->next = MergeLists(headA->next, headB);
    }
    else
    {
        result = headB;
        result->next = MergeLists(headA, headB->next);
    }
    
    return result;
}
