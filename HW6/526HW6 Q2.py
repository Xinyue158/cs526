{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "542e3ba8-be5f-4823-b11c-3abb3a826428",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " SMALL (15 values) \n",
      "Original: [34, 7, 23, 32, 5, 62, 9, 81, 44, 12, 1, 19, 50, 27, 3]\n",
      "Sorted: [1, 3, 5, 7, 9, 12, 19, 23, 27, 32, 34, 44, 50, 62, 81]\n",
      "\n",
      " MEDIUM (50 values) \n",
      "Original: [45, 12, 78, 34, 23, 89, 90, 11, 9, 56, 43, 27, 83, 72, 65, 39, 8, 14, 4, 20, 31, 99, 57, 67, 2, 18, 26, 33, 41, 52, 74, 61, 13, 6, 24, 80, 95, 1, 36, 28, 49, 70, 63, 21, 10, 17, 59, 3, 82, 47]\n",
      "Sorted (first 40): [1, 2, 3, 4, 6, 8, 9, 10, 11, 12, 13, 14, 17, 18, 20, 21, 23, 24, 26, 27, 28, 31, 33, 34, 36, 39, 41, 43, 45, 47, 49, 52, 56, 57, 59, 61, 63, 65, 67, 70]\n",
      "\n",
      "LARGE (500 values) \n",
      "Original (first 30): [823, 112, 457, 639, 284, 901, 753, 66, 520, 399, 712, 458, 230, 19, 887, 543, 210, 678, 305, 92, 119, 744, 820, 38, 557, 963, 204, 719, 415, 380]\n",
      "Sorted (first 40): [19, 37, 38, 42, 59, 59, 66, 77, 77, 77, 84, 87, 88, 89, 90, 91, 92, 94, 94, 96, 102, 103, 105, 105, 106, 108, 109, 110, 111, 112, 113, 114, 115, 118, 119, 120, 122, 133, 135, 139]\n"
     ]
    }
   ],
   "source": [
    "# function\n",
    "def load_numbers(filename):\n",
    "    nums = []\n",
    "    with open(filename, \"r\") as f:\n",
    "        for line in f:\n",
    "            parts = line.strip().split()\n",
    "            for p in parts:\n",
    "                nums.append(int(p))\n",
    "    return nums\n",
    "\n",
    "def counting_sort_exp(arr, exp):\n",
    "    n = len(arr)\n",
    "    output = [0] * n\n",
    "    count = [0] * 10\n",
    "\n",
    "    for i in range(n):\n",
    "        index = (arr[i] // exp) % 10\n",
    "        count[index] += 1\n",
    "\n",
    "    for i in range(1, 10):\n",
    "        count[i] += count[i - 1]\n",
    "\n",
    "    for i in range(n - 1, -1, -1):\n",
    "        index = (arr[i] // exp) % 10\n",
    "        output[count[index] - 1] = arr[i]\n",
    "        count[index] -= 1\n",
    "\n",
    "    for i in range(n):\n",
    "        arr[i] = output[i]\n",
    "\n",
    "\n",
    "def radix_sort(arr):\n",
    "    if len(arr) == 0:\n",
    "        return arr\n",
    "\n",
    "    a = arr[:]\n",
    "    max_val = max(a)\n",
    "    exp = 1\n",
    "\n",
    "    while max_val // exp > 0:\n",
    "        counting_sort_exp(a, exp)\n",
    "        exp *= 10\n",
    "\n",
    "    return a\n",
    "\n",
    "# run\n",
    "small = load_numbers(\"input_small.txt\")\n",
    "medium = load_numbers(\"input_medium.txt\")\n",
    "large = load_numbers(\"input_large.txt\")\n",
    "\n",
    "print(\" SMALL (15 values) \")\n",
    "print(\"Original:\", small)\n",
    "print(\"Sorted:\", radix_sort(small))\n",
    "print()\n",
    "\n",
    "print(\" MEDIUM (50 values) \")\n",
    "print(\"Original:\", medium)\n",
    "print(\"Sorted (first 40):\", radix_sort(medium)[:40])\n",
    "print()\n",
    "\n",
    "print(\"LARGE (500 values) \")\n",
    "print(\"Original (first 30):\", large[:30])\n",
    "print(\"Sorted (first 40):\", radix_sort(large)[:40])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7b11ad81-e84a-4c3e-85ec-6ad100bb152c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
