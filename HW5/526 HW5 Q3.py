#!/usr/bin/env python
# coding: utf-8

# In[4]:


def getLongestSeq(A, B):
    n = len(A)
    m = len(B)

    bestA = [1] * n
    bestB = [1] * m

    fromA = [None] * n
    fromB = [None] * m

    for i in range(n):
        for j in range(m):
            if A[i] < B[j]:
                if bestA[i] + 1 > bestB[j]:
                    bestB[j] = bestA[i] + 1
                    fromB[j] = ("A", i)
            if B[j] < A[i]:
                if bestB[j] + 1 > bestA[i]:
                    bestA[i] = bestB[j] + 1
                    fromA[i] = ("B", j)

    bestLen = 0
    lastSide = None
    lastPos = -1

    for i in range(n):
        if bestA[i] > bestLen:
            bestLen = bestA[i]
            lastSide = "A"
            lastPos = i

    for j in range(m):
        if bestB[j] > bestLen:
            bestLen = bestB[j]
            lastSide = "B"
            lastPos = j

    ans = []
    side = lastSide
    pos = lastPos

    while side is not None and pos != -1:
        if side == "A":
            ans.append(A[pos])
            prev = fromA[pos]
        else:
            ans.append(B[pos])
            prev = fromB[pos]

        if prev is None:
            break

        side, pos = prev

    ans.reverse()
    return ans


def readABfromFile(fname):
    with open(fname, "r") as f:
        lines = f.read().strip().splitlines()

    sizeA = int(lines[0].strip())
    sizeB = int(lines[1].strip())

    A = [int(x) for x in lines[2].split()]
    B = [int(x) for x in lines[3].split()]

    return A, B


file1 = "longest_seq1.txt"
A1, B1 = readABfromFile(file1)
seq1 = getLongestSeq(A1, B1)
print("File Input:", file1)
print("Longest Sequence:", seq1)
print()

file2 = "longest_seq2.txt"
A2, B2 = readABfromFile(file2)
seq2 = getLongestSeq(A2, B2)
print("File Input:", file2)
print("Longest Sequence:", seq2)
print()

file3 = "longest_seq3.txt"
A3, B3 = readABfromFile(file3)
seq3 = getLongestSeq(A3, B3)
print("File Input:", file3)
print("Longest Sequence:", seq3)
print()

file4 = "longest_seq4.txt"
A4, B4 = readABfromFile(file4)
seq4 = getLongestSeq(A4, B4)
print("File Input:", file4)
print("Longest Sequence:", seq4)
print()

file5 = "longest_seq5.txt"
A5, B5 = readABfromFile(file5)
seq5 = getLongestSeq(A5, B5)
print("File Input:", file5)
print("Longest Sequence:", seq5)
print()

file6 = "longest_seq6.txt"
A6, B6 = readABfromFile(file6)
seq6 = getLongestSeq(A6, B6)
print("File Input:", file6)
print("Longest Sequence:", seq6)
print()


# In[ ]:




