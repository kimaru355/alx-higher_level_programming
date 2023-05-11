#include "lists.h"

/**
  * insert_node - insert a number in listint_t list
  * @head: pointer to pointer of first node of listint_t list
  * @number: integer to be included in new node
  * Return: address of the new element or NULL if it fails
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *copy, *new;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	copy = *head;
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	for (; copy != NULL; copy = copy->next)
	{
		if (number <= copy->n)
		{
			*head = new;
			new->next = copy;
			return (new);
		}
		if (number >= copy->n && copy->next == NULL)
		{
			new->next = NULL;
			copy->next = new;
			return (new);
		}
		if (number >= copy->n && number <= copy->next->n)
		{
			new->next = copy->next;
			copy->next = new;
			return (new);
		}
	}
	return (NULL);
}

