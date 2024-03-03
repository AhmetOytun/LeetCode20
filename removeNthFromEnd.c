#include <stdio.h> 
#include <stdlib.h> 

struct ListNode {
    int val;
    struct ListNode *next;
};
 
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode *temp = head;
    int length = 0;
    
    while (temp != NULL){
        temp = temp->next;
        length++;
    }

    temp=head;

    for (int i = 0; i < length-n-1; i++){
        temp = temp->next;
    }
    
    if(length==0){
        return NULL;
    }else if(n==length){
        temp=temp->next;
    }else{
        temp->next = temp->next->next;
        temp = head;
    }

    return temp;
}