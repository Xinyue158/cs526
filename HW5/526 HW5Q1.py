#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

class NodeThing:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class MyBST:
    def __init__(self):
        self.root = None

    def addNode(self, x):
        if self.root is None:
            self.root = NodeThing(x)
        else:
            self._addHelp(self.root, x)

    def _addHelp(self, cur, x):
        if cur is None:
            return NodeThing(x)

        if x < cur.val:
            if cur.left is None:
                cur.left = NodeThing(x)
            else:
                self._addHelp(cur.left, x)
        elif x > cur.val:
            if cur.right is None:
                cur.right = NodeThing(x)
            else:
                self._addHelp(cur.right, x)
        return cur

    def findNode(self, x):
        return self._findHelp(self.root, x)

    def _findHelp(self, cur, x):
        if cur is None:
            return False
        if cur.val == x:
            return True
        if x < cur.val:
            return self._findHelp(cur.left, x)
        else:
            return self._findHelp(cur.right, x)

    def deleteNode(self, x):
        self.root = self._deleteHelp(self.root, x)

    def _deleteHelp(self, cur, x):
        if cur is None:
            return None

        if x < cur.val:
            cur.left = self._deleteHelp(cur.left, x)
        elif x > cur.val:
            cur.right = self._deleteHelp(cur.right, x)
        else:
            # found
            if cur.left is None and cur.right is None:
                return None
            if cur.left is None:
                return cur.right
            if cur.right is None:
                return cur.left

            tmp = cur.right
            while tmp.left is not None:
                tmp = tmp.left
            cur.val = tmp.val
            cur.right = self._deleteHelp(cur.right, tmp.val)

        return cur

    def printTree(self):
        print("Tree:", end=" ")
        self._printHelp(self.root)
        print()

    def _printHelp(self, cur):
        if cur is None:
            return
        self._printHelp(cur.left)
        print(cur.val, end=" ")
        self._printHelp(cur.right)


# In[12]:


t1 = MyBST()

size1 = random.randint(5, 50)
dataList = random.sample(range(1, 1001), size1)

print("Input size:", size1)
print("Input list:", dataList)

# the tree
for a1 in dataList:
    t1.addNode(a1)

print("\nInitial tree:")
t1.printTree()

# add
print("\n--- Testing addNode() ---")
for i in range(3):
    newNum = random.randint(1, 1000)
    print("Adding:", newNum)
    t1.addNode(newNum)
    t1.printTree()

# delete
print("\n--- Testing deleteNode() ---")
leftList = dataList[:]
for i in range(3):
    if not leftList:
        break
    delNum = random.choice(leftList)
    leftList.remove(delNum)
    print("Deleting:", delNum)
    t1.deleteNode(delNum)
    t1.printTree()

# find
print("\n--- Testing findNode() ---")

foundPos = None
tries = 0
while foundPos is None and tries < 40:
    # try to find something that exists
    if leftList:
        candidate = random.choice(leftList)
    else:
        candidate = random.randint(1, 1000)

    if t1.findNode(candidate):
        foundPos = candidate

    tries += 1   # <-- THIS is the correct line

print("Searching existing:", foundPos, "->", t1.findNode(foundPos))

# not exist
while True:
    maybe = random.randint(1, 1000)
    if not t1.findNode(maybe):
        break

print("Searching non-existing:", maybe, "->", t1.findNode(maybe))


# In[ ]:





# In[ ]:




