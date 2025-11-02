#!/usr/bin/env python
# coding: utf-8

# In[2]:


#peoblem1
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

#           A
#        /  |  \
#       B   C   D
#      / \      \
#     E   F      G
#    / \
#   H   I

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
H = Node("H")
I = Node("I")


A.children = [B, C, D]
B.children = [E, F]
D.children = [G]
E.children = [H, I]

def preorder(node, result):
    if not node:
        return
    result.append(node.value)
    for child in node.children:
        preorder(child, result)

def postorder(node, result):
    if not node:
        return
    for child in node.children:
        postorder(child, result)
    result.append(node.value)

from collections import deque

def breadth_first(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        current = queue.popleft()
        result.append(current.value)
        for child in current.children:
            queue.append(child)
    return result


if __name__ == "__main__":
    pre = []
    preorder(A, pre)

    post = []
    postorder(A, post)

    bfs = breadth_first(A)

    print("Preorder Traversal: ", " -> ".join(pre))
    print("Breadth-First Traversal: ", " -> ".join(bfs))
    print("Postorder Traversal: ", " -> ".join(post))


# In[3]:


# Problem 2

file = open("fewest_1.txt", "r")
n = int(file.readline().strip())
target = int(file.readline().strip())
arr = list(map(int, file.readline().split()))
file.close()

arr.sort(reverse=True)
total = 0
count = 0

for num in arr:
    total += num
    count += 1
    if total > target:
        break

print("Input:", ",".join(map(str, arr)), "Target:", target, "Answer:", count)


# In[4]:


# Problem 3

file = open("righttangles_1.txt", "r")
n = int(file.readline().strip())
pts = []
for _ in range(n):
    x, y = map(int, file.readline().split())
    pts.append((x, y))
file.close()

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            ax, ay = pts[i]
            bx, by = pts[j]
            cx, cy = pts[k]

            abx, aby = bx - ax, by - ay
            acx, acy = cx - ax, cy - ay
            bax, bay = ax - bx, ay - by
            bcx, bcy = cx - bx, cy - by
            cax, cay = ax - cx, ay - cy
            cbx, cby = bx - cx, by - cy

            area2 = (bx - ax) * (cy - ay) - (cx - ax) * (by - ay)
            if area2 == 0:
                continue

            if (abx * acx + aby * acy == 0 or
                bax * bcx + bay * bcy == 0 or
                cax * cbx + cay * cby == 0):
                ans += 1

print("The number of right triangles is:", ans)


# In[ ]:




