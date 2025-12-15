#!/usr/bin/env python
# coding: utf-8

# In[5]:


def count_vowel_combos(code_str):
    n = len(code_str)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):


        if code_str[i - 1:i] == ".":
            dp[i] += dp[i - 1]

        if i >= 2:
            last2 = code_str[i - 2:i]
            if last2 == ".-" or last2 == "..":
                dp[i] += dp[i - 2]

        if i >= 3:
            last3 = code_str[i - 3:i]
            if last3 == "---" or last3 == "..-":
                dp[i] += dp[i - 3]

    return dp[n]

# RUN FILE 1
filename1 = "vowel_input1.txt"
with open(filename1, "r") as f:
    lines = f.read().strip().splitlines()
code1 = lines[-1].strip()

print("File Input:", filename1)
print("The Number of Vowel combinations is:", count_vowel_combos(code1))
print()


# RUN FILE 2
filename2 = "vowel_input2.txt"
with open(filename2, "r") as f:
    lines = f.read().strip().splitlines()
code2 = lines[-1].strip()

print("File Input:", filename2)
print("The Number of Vowel combinations is:", count_vowel_combos(code2))
print()


# RUN FILE 3
filename3 = "vowel_input3.txt"
with open(filename3, "r") as f:
    lines = f.read().strip().splitlines()
code3 = lines[-1].strip()

print("File Input:", filename3)
print("The Number of Vowel combinations is:", count_vowel_combos(code3))
print()

# FILE 4
filename4 = "vowel_input4.txt"
with open(filename4, "r") as f:
    lines = f.read().strip().splitlines()
code4 = lines[-1].strip()

print("File Input:", filename4)
print("The Number of Vowel combinations is:", count_vowel_combos(code4))
print()


# In[ ]:




