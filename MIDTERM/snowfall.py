#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Problem 1

import sys


data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)

n = int(data[0])
arr = list(map(int, data[1:1+n]))

total = arr[-1]
half = total / 2.0
found = False

for i in range(n - 2):
    prev = 0 if i == 0 else arr[i - 1]
    three_sum = arr[i + 2] - prev
    if three_sum > half:
        found = True
        break

print(" ".join(map(str, arr)), "solution:", "YES" if found else "NO")

