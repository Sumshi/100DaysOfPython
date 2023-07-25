#include <stdio.h>

/*function to get maximum element from array*/
int find_max(int arr[], int n)
{
	int max_element = arr[0];
	int i;

	for(i = 1; i<n; i++)
	{
		if(arr[i] > max_element)
			max_element = arr[i];
	}
	return max_element;
}

void countingSort(int arr[], int n, int pos)
{
	int result[n + 1];
	int count[10] = {0};
	int i;

	/*count howmany numbers are present with digit 0-9 at given position*/
	for (i = 0; i < n; i++)
		count[(arr[i] / pos) % 10]++;

	/*now do prefix sum of the count array*/
	for (i = 1; i < 10; i++)
		count[i] += count[i - 1];

	/*Place the elements in sorted order*/
	for (i = n - 1; i >= 0; i--)
	{
		result[count[(arr[i] / pos) % 10] - 1] = arr[i];
		count[(arr[i] / pos) % 10]--;
	}
	for (i = 0; i < n; i++)
		arr[i] = result[i];
}
void radixsort(int arr[], int n)
{

	int max_element = find_max(arr, n);
	int pos;

	/*counting sort from the least significant digit to the msd*/
	for (pos = 1; max_element / pos > 0; pos *= 10)
		countingSort(arr, n, pos);
}
int main()
{
	int arr[] = {312, 42, 635, 11, 8, 783, 954, 777};
	int n = sizeof(arr) / sizeof(arr[0]);
	int i;

	printf("An array before applying the radix sort: \n");
	for (i = 0; i < n; ++i)
	{
		printf("%d  ", arr[i]);
	}
	printf("\n");

	radixsort(arr, n);
	printf("An array after applying the radix sort: \n");
	for (i = 0; i < n; ++i) {
		printf("%d  ", arr[i]);
	}
	printf("\n");
}
