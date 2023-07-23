#include "sort.h"
/**
 * merge_sort - sorts an array of integers in ascending order
 * @array: array to be sorted
 * @size: size of the array
 */
void merge_sort(int *array, size_t size)
{
	int *tmp = NULL;

	if (array == NULL || size < 2)
		return;

	tmp = malloc(sizeof(int) * size);
	if (tmp == NULL)
		return;

	merge_sort_helper(array, 0, size - 1, tmp);
	free(tmp);
}

/**
 * merge_sort_helper - helper function for merge_sort
 * @array: array to be sorted
 * @left: left index
 * @right: right index
 * @tmp: temporary array to store sorted elements
 */
void merge_sort_helper(int *array, int left, int right, int *tmp)
{
	int mid = 0;/*refers to the middle element*/

	if (left < right)
	{
		mid = (left + right) / 2;
		merge_sort_helper(array, left, mid, tmp);
		merge_sort_helper(array, mid + 1, right, tmp);
		merge(array, left, mid + 1, right + 1, tmp);
	}
}

/**
 * merge - merges two subarrays into one sorted array
 * @array: array to be sorted
 * @left: left index
 * @mid: middle index
 * @right: right index
 * @tmp: temporary array to store sorted elements
 */
void merge(int *array, int left, int mid, int right, int *tmp)
{
	int i = left;
	int j = mid;
	int k = left;

	while (i < mid && j < right)
	{
		if (array[i] <= array[j])
			tmp[k++] = array[i++];
		else
			tmp[k++] = array[j++];
	}

	while (i < mid)
		tmp[k++] = array[i++];

	while (j < right)
		tmp[k++] = array[j++];

	for (i = left; i < right; i++)
		array[i] = tmp[i];
}
