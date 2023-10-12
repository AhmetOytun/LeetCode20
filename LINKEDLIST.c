#include "stdio.h"
#include "stdlib.h"
struct node{
    int data;
    struct node *next;
};
void add_data(struct node *head,int data);
void show_data(struct node *head);
void add_data_head(struct node *head,int data);
int main(void){
    struct node *head=(struct node*)malloc(sizeof (struct node));
    add_data_head(head,7);
    add_data(head,6);
    add_data(head,5);
    add_data(head,4);
    add_data(head,3);
    add_data(head,2);
    add_data(head,1);
    show_data(head);
}
void add_data(struct node *head,int data){
    struct node *curr=(struct node*) malloc(sizeof (struct node));
        while (head->next!=NULL) {
            head = head->next;
        }
        curr->data=data;
        head->next=curr;
        curr->next=NULL;

}
void show_data(struct node *head){
    while (head->next!=NULL){
        printf("%d ",head->data);
        head=head->next;
    }
    printf("%d",head->data);
}
void add_data_head(struct node *head,int data){
    head->data=data;
}
