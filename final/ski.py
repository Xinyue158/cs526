#!/usr/bin/env python
# coding: utf-8

# In[ ]:


m = int(input())
n = int(input())

mountain = []
for i in range(m):
    row = list(map(int, input().split()))
    mountain.append(row)

memo = []
for i in range(m):
    row = [-1] * n
    memo.append(row)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def find_longest_path(r, c):
    if memo[r][c] != -1:
        return memo[r][c]

    max_steps = 0

    for dr, dc in directions:
        new_r = r + dr
        new_c = c + dc

        if new_r >= 0 and new_r < m and new_c >= 0 and new_c < n:
            if mountain[new_r][new_c] < mountain[r][c]:
                steps = 1 + find_longest_path(new_r, new_c)
                if steps > max_steps:
                    max_steps = steps

    memo[r][c] = max_steps
    return max_steps

answer = 0
for i in range(m):
    for j in range(n):
        steps = find_longest_path(i, j)
        if steps > answer:
            answer = steps

print(answer)


# In[ ]:




