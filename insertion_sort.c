#include <stdio.h>
int main(void)
{
    int i;          /* iterates over the array */
    int j;          /* compares elements */
    int key;        /* temporary variable to hold the current element being considered */
    int a[] = {8, 4, 9, 5, 7, 6, 3, 2}; /* input array to be sorted */
    int length = 8; /* length of the input array */

    // Outer loop: iterate over the array from the second element (index 1) to the last element (index length - 1)
    for (i = 1; i < length; i++)
    {
        key = a[i]; /* Store the current element (a[i]) in the temporary variable key */
        j = i - 1;  /* Initialize j to the previous index (i - 1) */

        // Inner loop: compares elements and shifts elements to the right until the correct position for the key is found
        while (j >= 0 && a[j] > key)
        {
            a[j + 1] = a[j]; /* Move the element at index j one position to the right */
            j = j - 1;       /* Move j one position to the left to continue comparing with the previous element */
        }

        // Place the key in its correct position
        a[j + 1] = key; /* Insert the key in the sorted position */
    }

    // Print the sorted array
    for (i = 0; i < 8; i++)
        printf("%d\n", a[i]);

    return (0);
}

