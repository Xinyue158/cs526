#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#problem 4
n = int(input().strip())
symbols = input().strip().split(',')
board = []
for i in range(n):
    row = input().strip().split(',')
    board.append(row)

def check_rows():
    for row in board:
        used = []
        for cell in row:
            if cell != '.' and cell in used:
                return False
            used.append(cell)
    return True

def check_cols():
    for c in range(n):
        used = []
        for r in range(n):
            cell = board[r][c]
            if cell != '.' and cell in used:
                return False
            used.append(cell)
    return True

def check_boxes():
    size = int(n ** 0.5)
    for row_start in range(0, n, size):
        for col_start in range(0, n, size):
            used = []
            for r in range(row_start, row_start + size):
                for c in range(col_start, col_start + size):
                    cell = board[r][c]
                    if cell != '.' and cell in used:
                        return False
                    used.append(cell)
    return True

if check_rows() and check_cols() and check_boxes():
    print("The board is valid")
else:
    print("The board is invalid")

