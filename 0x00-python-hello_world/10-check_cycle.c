#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *set = list;
	listint_t *roll = list;

	if (!list)
		return (0);

	while (set && roll && roll->next)
	{
		set = set->next;
		roll = roll->next->next;
		if (set == roll)
			return (1);
	}
	return (0);
}
