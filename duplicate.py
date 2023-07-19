#!/usr/bin/python3

"""program that finds duplicates in a list"""

numbers = [3,2,6,2,4,3,6,8,5,9]

for i in range(len(numbers)): # iterates over the entire list
    for j in range(i + 1, len(numbers)): # iterates over each index
        if numbers[i] == numbers[j]:
            print(f"number {numbers[i]} is a duplicate")
            break
