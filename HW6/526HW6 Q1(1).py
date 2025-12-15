#!/usr/bin/env python
# coding: utf-8

# In[1]:


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_part = merge_sort(arr[:mid])
    right_part = merge_sort(arr[mid:])
    return merge(left_part, right_part)


def merge(left, right):
    result = []
    i = 0
    j = 0


    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # add remaining items
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def quick_sort(arr):
    return quick_sort_helper(arr, 0, len(arr) - 1)


def quick_sort_helper(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort_helper(arr, low, p - 1)
        quick_sort_helper(arr, p + 1, high)
    return arr


def partition(arr, low, high):
    pivot = arr[high]  # choose last element as pivot (simple student method)
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # swap
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def read_input_file(filename):
    numbers = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.split()
            for p in parts:
                numbers.append(int(p))
    return numbers


def main():
    print("Enter which input file to use: small / medium / large")
    choice = input()

    if choice == "small":
        filename = "input_small.txt"
    elif choice == "medium":
        filename = "input_medium.txt"
    else:
        filename = "input_large.txt"

    data = read_input_file(filename)

    print("\nOriginal numbers:")
    print(data)

    print("\nChoose sorting algorithm: insertion / merge / quick")
    algo = input()

    if algo == "insertion":
        sorted_data = insertion_sort(data.copy())
    elif algo == "merge":
        sorted_data = merge_sort(data.copy())
    else:
        sorted_data = quick_sort(data.copy())

    print("\nSorted numbers:")
    print(sorted_data)


if __name__ == "__main__":
    main()


# In[2]:


if __name__ == "__main__":
    main()



# In[3]:


if __name__ == "__main__":
    main()


# In[ ]:




