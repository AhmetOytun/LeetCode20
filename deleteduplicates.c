/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdlib.h>
#include <stdio.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *deleteDuplicates(struct ListNode *head)
{
    // Initialize a temporary pointer to traverse the list
    struct ListNode *temp = head;

    // If the list is empty, return NULL
    if (temp == NULL)
    {
        return NULL;
    }

    // Traverse the list
    while (temp->next != NULL)
    {
        // If the current node's value is equal to the next node's value
        if (temp->val == temp->next->val)
        {
            // Store the duplicate node
            struct ListNode *duplicate = temp->next;
            // Bypass the duplicate node
            temp->next = temp->next->next;
            // Free the memory of the duplicate node
            free(duplicate);
        }
        else
        {
            // Move to the next node if no duplicate
            temp = temp->next;
        }
    }
    return head;
}

int main()
{
}