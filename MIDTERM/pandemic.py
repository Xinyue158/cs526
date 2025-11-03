#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#  Problem 2

n = int(input().strip())  
grid = [[0 for _ in range(n)] for _ in range(n)]

for line in range(n):
    try:
        r, c = map(int, input().split())
        grid[r - 1][c - 1] = 1
    except:
        break  

def has_healthy(g):
    for row in g:
        if 0 in row:
            return True
    return False

def infected_neighbors(g, r, c):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and g[nr][nc] == 1:
            count += 1
    return count

changed = True
while changed:
    changed = False
    new_grid = [row[:] for row in grid]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0 and infected_neighbors(grid, i, j) >= 2:
                new_grid[i][j] = 1
                changed = True
    grid = new_grid
if has_healthy(grid):
    print("There are healthy counties left")
else:
    print("There are no healthy counties left")


# In[ ]:




