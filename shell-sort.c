#include <stdio.h>
/* function to implement shellSort */
int shell(int a[], int n)
{
	int interval;
	int i, j, temp;

	for (interval = n/2; interval > 0; interval /= 2)
	{
		for (i = interval; i < n; i ++)
		{
			temp = a[i];
			for (j = i; j >= interval && a[j - interval] > temp; j -= interval)
				a[j] = a[j - interval];
			a[j] = temp;
		}
	}
	return 0;
}
void printArr(int a[], int n) /* function to print the array elements */
{
	int i;
	for (i = 0; i < n; i++)
		printf("%d ", a[i]);
}
int main()
{
	int a[] = { 33, 31, 40, 8, 12, 17, 25, 42 };
	int n = sizeof(a) / sizeof(a[0]);
	printf("Before sorting array elements are - \n");
	printArr(a, n);
	shell(a, n);
	printf("\nAfter applying shell sort, the array elements are - \n");
	printArr(a, n);
	return 0;
}
