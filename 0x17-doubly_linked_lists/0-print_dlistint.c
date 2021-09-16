#include "lists.h"

/**
 * print_dlistint - prints all the elements of a dlisting_t list
 * @h: the point to the node head
 *
 * Return: the number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t len = 0;

	for (; h; h = h->next)
	{
		printf("%d\n", h->n);
		len++;
	}

	return (len);

}
