#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to head of list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 * An empty list is considered a palindrome.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *prev = NULL, *tmp = NULL;
    int ret = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast && fast->next)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    tmp = slow;
    if (fast)
        slow = slow->next;

    prev->next = NULL;
    reverse_listint(&slow);
    ret = compare_listint(*head, slow);
    reverse_listint(&slow);

    if (tmp)
        prev->next = tmp;

    return (ret);
}
