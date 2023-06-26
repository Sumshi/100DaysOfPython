#!/usr/bin/python3
#Write your code below this row 👇
sum = 0
for i in range(1, 101): # or range(2, 101, 2)
    if i % 2 == 0:
        sum +=  i
print(sum)
