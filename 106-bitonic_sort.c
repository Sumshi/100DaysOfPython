#include "sort.h"
/**
 * bitonic_sort - sorts an array
 * @array: array to sort
 * @size: size of the array
 * Return: void
 */
void bitonic_sort(int *array, size_t size)
{
	int k;

	if (size > 1)
	{
		k = size / 2;
		bitonic_sort(array, k);/*sort in ascending order*/
		bitonic_sort(array + k, k);/*sort in descending order*/
		merge(array, 0, size, 1);/*merge the sequence in ascending order*/
	}
}
/**
 * sort - sorts an array
 * @a: array to sort
 * @n: array of integers to sort
 * @order: sorts array in a specified order
 * Return: void
 */
void sort(int a[], int n, int order)
{
	int i, j;

	bitonic_sort(a, n);
	if (order == 0)
	{
		for (i = 0, j = n - 1; i < j; i++, j--)
			exchange(a, i, j, 1);
	}
}
/**
 * swap - swaps the elements in the array
 * @a: array to swap
 * @i: element to swap
 * @j: element to swap
 * @d: direction 1 for ascending, 0 for descending
 * Return: void
 */
void swap(int a[], int i, int j, int d)
{
	int temp;

	if (d == (a[i] > a[j]))
	{
		temp = a[i];
		a[i] = a[j];
		a[j] = temp;
	}
}
/**
 * merge_bitonic - merges the bitonic list
 * @a: array to merge
 * @begin: starting index of current sequence
 * @count: size of the current sequence
 * @d: direction 1 for ascending, 0 for descending
 * Return: void
 */
void merge_bitonic(int a[], int begin, int count, int d)
{
	int k, i;

	if (count > 1)
	{
		k = count / 2;/*splits current sequence in 2 halves*/
		for (i = begin; i < begin + k; i++)
			swap(a, i, i + k, d);
		merge(a, begin, k, d);
		merge(a, begin + k, k, d);
	}
}
void print(int a[], int n)
{
    int i;
    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
}

int main()
{
    int a[] = {30, 70, 40, 80, 60, 20, 10, 50};
    int n = sizeof(a) / sizeof(a[0]);
    int order = 1; // It means sorting in increasing order
    printf("Before sorting, array elements are - \n");
    print(a, n);
    sort(a, n, order);
    printf("\nAfter sorting, array elements are - \n");
    print(a, n);
    return 0;
}

