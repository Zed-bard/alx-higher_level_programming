#include "lists.h"

/**
 * print_dlistint - prints all the elements of a
 * dlistint_t list
 *
 * @z: head of the list
 * Return: the number of nodes
 */
size_t print_dlistint(const dlistint_t *z)
{
	int count;

	count = 0;

	if (z == NULL)
		return (count);

	while (z->prev != NULL)
		z = z->prev;

	while (z != NULL)
	{
		printf("%d\n", z->n);
		count++;
		z = z->next;
	}

	return (count);
}
