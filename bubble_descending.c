#include<stdio.h>

/*bubblesort that sorts elements next to each other in descending order*/

int main(void)
{
        int a[] =  {1,3,7,9,0,2,4,5,8,6};
        int length = 10;/*no of elements in the array are 10*/
        int i; /*for iterating the loop*/
        int temp;/*for keeping a copy of one element*/
        int j;/*for iterating the elements in the loop*/

        for (i = 0; i < length; i++)/*iterates over elements in the loop*/
        {
                for (j = 0; j < (length - 1); j++)/*compares each element*/
                {/*length - 1 because last element has no num to compare against*/
                        if (a[j] < a[j + 1])
                        {
                                /*a[j + 1] refers to next element*/
                                temp = a[j];
                                a[j] = a[j + 1];
                                a[j + 1] = temp;
                        }
                }


        }
        for (i = 0; i < length; i++)
                printf("%d\n", a[i]);
        return (0);
}
