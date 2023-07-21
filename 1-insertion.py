#!/usr/bin/python3
def insert_sort(A=[]):
    i = 1
    while i < len(A):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j = j - 1
            print(A)
        i = i + 1

A = [19, 48, 99, 71, 13, 52, 96, 73, 86, 7]
insert_sort(A)
