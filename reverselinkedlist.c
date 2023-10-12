#include "stdio.h"
struct ListNode {
    int val;
    struct ListNode *next;
};
struct ListNode* reverseList(struct ListNode* head){
    struct ListNode *ptr;
    ptr=head;
    if(ptr->next == NULL){
        printf("head is null");
    }else{

    }
}