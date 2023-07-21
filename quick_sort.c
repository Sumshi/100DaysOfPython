#include<stdio.h>

/*quick sort algorithm*/

void swap(int *x, int *y);
void quicksort(int array[], int length);
void quicksort_recursion(int array[], int low, int high);
int partition(int array, int low, int high);

int main(void)
{
	int a = {10,22,23,44,8,15}
	int length = 6
	int i;

	quicksort(a, length);
	for (i = 0; i < length; i++)
		printf("%d\n", a[i]);
	printf("\n");

return (0);
}

void swap(int *x, int *y)
{
	int temp;
	temp = *x;
	*x = *y;
	*y = temp;
}

void quicksort(int array[], int length)
{
/* 0 is the first index, length - 1 is the last*/

	quicksort_recursion(array, 0, length - 1);
}
void quicksort_recursion
