#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#  Problem 3

n = int(input().strip())
aisles = input().strip().split(',')

max_items = 0

for start in range(n):
    baskets = []  
    count = 0
    for i in range(start, n):
        item = aisles[i]
        if item in baskets:
            count += 1
        elif len(baskets) < 2:
            baskets.append(item)
            count += 1
        else:
            break
    if count > max_items:
        max_items = count

print(f"{max_items} items were selected")


# In[ ]:





# In[ ]:





# In[ ]:




