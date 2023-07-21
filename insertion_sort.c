#include <stdio.h>
#include<stdlib.h>
int main(void)
{
    int i;          /* iterates over the array */
    int j;          /* compares elements */
    int key;        /* temporary variable to hold the current element*/
    int a[] = {8, 4, 9, 5, 7, 6, 3, 2}; /* input array to be sorted */
    int length = 8; /* length of the input array */


    for (i = 1; i < length; i++)
    {
        key = a[i]; /* Store the current element (a[i])*/
        j = i - 1;  /*points to second element */

        while (j >= 0 && a[j] > key)
        {
            a[j + 1] = a[j]; /* Move the element at index j one position*/
            j = j - 1;       /* Move j one position to the left*/
        }
        a[j + 1] = key; /* Insert the key in the sorted position */
    }
    /*Print the sorted array*/
    for (i = 0; i < 8; i++)
        printf("%d\n", a[i]);

    return (0);
}
