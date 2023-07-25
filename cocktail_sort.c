#include <stdio.h>
#include <stdlib.h>
/**
 * cocktail_sort_array - Sorts an array of integers in ascending order
 * using the Cocktail shaker sort algorithm.
 * Traverses the list noth forward and backward 
 * @array: Pointer to the array to be sorted.
 * @size: Size of the array.
 */
void cocktail_sort_array(int *array, size_t size)
{
    int swapped = 1;
    size_t left, right;

    if (array == NULL || size < 2)
        return;

    for (; swapped;)
    {
        swapped = 0;

        for (left = 0; left < size - 1; left++)
        {/* traverses the array from left to right */
            if (array[left] > array[left + 1])
            {
                int temp = array[left];
                array[left] = array[left + 1];
                array[left + 1] = temp;
                swapped = 1;
            }
        }

        if (!swapped)/*no swaps were made so break out of the loop*/
            break;

        swapped = 0;

        for (right = size - 1; right > 0; right--)
        {/*traverses the array from right to left*/
            if (array[right] < array[right - 1])
            {
                int temp = array[right];
                array[right] = array[right - 1];
                array[right - 1] = temp;
                swapped = 1;
            }
        }
    }
}

int main(void)
{
    int array[] = {19, 48, 99, 71, 13, 52, 96, 73, 86, 7};
    size_t n = sizeof(array) / sizeof(array[0]);

    printf("Original Array: ");
    for (size_t i = 0; i < n; ++i)
        printf("%d, ", array[i]);
    printf("\n");

    cocktail_sort_array(array, n);

    printf("Sorted Array: ");
    for (size_t i = 0; i < n; ++i)
        printf("%d, ", array[i]);
    printf("\n");

    return 0;
}
