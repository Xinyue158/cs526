#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq

def solve_flood():
    n = int(input())
    threshold = int(input())
    drain = int(input())

    cracks = []
    for i in range(n):
        time, size = map(int, input().split())
        cracks.append((time, size))

    if n == 0:
        print("SAFE")
        print(0)
        return

    current_water = 0
    max_water_ever = 0
    unfixed_cracks = []
    next_crack_index = 0

    max_time = n + 100
    if len(cracks) > 0:
        max_time = cracks[-1][0] + n + 100

    for time in range(max_time):

        while next_crack_index < n and cracks[next_crack_index][0] == time:
            crack_size = cracks[next_crack_index][1]
            heapq.heappush(unfixed_cracks, -crack_size)
            next_crack_index += 1

        if len(unfixed_cracks) > 0:
            heapq.heappop(unfixed_cracks)

        total_water_in = 0
        for crack in unfixed_cracks:
            total_water_in += (-crack)

        current_water = current_water + total_water_in
        current_water = current_water - drain

        if current_water < 0:
            current_water = 0

        if current_water > max_water_ever:
            max_water_ever = current_water

        if current_water >= threshold:
            print("FLOOD")
            print(time)
            print(current_water)
            return

        new_unfixed = []
        for crack in unfixed_cracks:
            old_size = -crack
            new_size = old_size + 1
            new_unfixed.append(-new_size)

        unfixed_cracks = new_unfixed
        heapq.heapify(unfixed_cracks)

        if len(unfixed_cracks) == 0 and next_crack_index >= n:
            break

    print("SAFE")
    print(max_water_ever)

solve_flood()


# In[ ]:




