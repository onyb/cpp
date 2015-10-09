/*
 * Problem: Find Merge Point of Two Lists
 * Author: Anirudha Bose <ani07nov@gmail.com>

   Find merge point of two linked lists
   Node is defined as
     struct Node
     {
         int data;
         Node* next;
     }
 */

int lengthOfList(Node* head)
{
    int l=0;
    while(head != NULL)
    {
        head = head->next;
        l++;
    }
    return l+1;
}

int FindMergeNode(Node *headA, Node *headB)
{
    int A = lengthOfList(headA), B = lengthOfList(headB);
    
    int c = 0;
    if(A>B)
    {
        while(c != A-B)
        {
            headA = headA->next;
            c++;
        }
    }
    else
    {
        while(c != B-A)
        {
            headB = headB->next;
            c++;
        }
    }
    
    while(headA != NULL && headB != NULL)
    {
        if(headA == headB)
            return headA->data;
        headA = headA->next;
        headB = headB->next;
    }
    return -1;
}
