#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;

while (current)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*head = prev;
}

/**
 * get_middle - finds the middle node of a linked list
 * @head: pointer to the linked list
 *
 * Return: pointer to the middle node
 */
listint_t *get_middle(listint_t *head)
{
listint_t *slow = head;
listint_t *fast = head;

while (fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
}

return (slow);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
if (*head == NULL || (*head)->next == NULL)
return (1);

listint_t *middle = get_middle(*head);
reverse_listint(&middle);

listint_t *current = *head;
while (middle)
{
if (current->n != middle->n)
return (0);
current = current->next;
middle = middle->next;
}

return (1);
}
