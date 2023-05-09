#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: A pointer to the head node of the linked list.
 * Return: 1 if there is a cycle, 0 if there is no cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next; /* Move slow pointer by one node */
		fast = fast->next->next; /* Move fast pointer by two nodes */

		/* If the pointers meet, there is a cycle in the linked list */
		if (slow == fast)
			return (1);
	}

	/* If we reach here, there is no cycle in the linked list */
	return (0);
}

