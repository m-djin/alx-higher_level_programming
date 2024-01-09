#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

void rev(listint_t **head);
int comp_list(listint_t *head, listint_t *middle, int len);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the first node in the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int len;
	listint_t *temp;
	listint_t *middle;
	int i;

	if (head == NULL || *head == NULL)
		return (1);
	temp = *head;
	middle = *head;
	for (len = 0 ; temp != NULL ; len++)
		temp = temp->next;
	len = len / 2;

	for (i = 1; i < len; i++)
		middle = middle->next;
	if (len % 2 != 0 && len != 1)
	{
		middle = middle->next;
		len = len - 1;
	}
	rev(&middle);
	i =  comp_list(*head, middle, len);

	return (i);
}

/**
 * comp_list - compare lists
 * @head: point to head node
 * @middle: points to middl node
 * @len: length of list
 * Return: 1 or 0
 */

int comp_list(listint_t *head, listint_t *middle, int len)
{
	int i;

	if (head == NULL || middle == NULL)
		return (1);
	for (i = 0 ; i < len; i++)
	{
		if (head->n != middle->n)
			return (0);
		head = head->next;
		middle = middle->next;
	}
	return (1);
}

/**
 * rev - changes order in reverse
 * @head: points to head
 */

void rev(listint_t **head)
{
	listint_t *next, *current, *prev;

	if (head == NULL || *head == NULL)
		return;

	prev = NULL;
	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
