#include<stdio.h>
#include<stdlib.h>

/*selection sort selects the smallest (or largest) element from unsorted list*/

int main(void)
{
	int a[] = {5,9,7,6,4,0};/*elements in the array*/
	int length = 6;/* 6 elements in the array*/
	int i;/*traverses array elements*/
	int j;
	int temp;
	for (i = 0; i < length - 1; i++)
	{
		int min_num = i;/*sets min num to be at first index*/
		for (j = i + 1; j < length; j++)
		{
			if (a[j] > a[min_num])/*use > to sort in descending*/
			{
				min_num = j;
			}
			if (min_num != i)/*if min num is not at first idx*/
			{/*swap value till min num is found*/
				temp = a[i];
				a[i] = a[min_num];
				a[min_num] = temp;
			}
		}
	}
	for (i = 0; i < length; i++)
		printf("%d\n", a[i]);
	return (0);
}
