#!/usr/bin/env python
# coding: utf-8

# In[4]:


def read_preferences(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    first = lines[0].split()[0]
    if first.isdigit():
        n = int(first)
        data = lines[1:1 + 2 * n]
    else:
        data = lines
        n = len(data) // 2

    men_lines = data[:n]
    women_lines = data[n:]

    men = []
    women = []
    men_pref = {}
    women_pref = {}

    for line in men_lines:
        parts = line.split()
        man = parts[0]
        prefs = parts[1:]
        men.append(man)
        men_pref[man] = prefs

    for line in women_lines:
        parts = line.split()
        woman = parts[0]
        prefs = parts[1:]
        women.append(woman)
        women_pref[woman] = prefs

    return men, women, men_pref, women_pref


def gale_shapley(men, women, men_pref, women_pref):
    free_men = men[:]
    next_proposal_index = {m: 0 for m in men}
    engagements = {}

    women_rank = {}
    for w in women:
        ranking = {}
        prefs = women_pref[w]
        for i in range(len(prefs)):
            ranking[prefs[i]] = i
        women_rank[w] = ranking

    while free_men:
        m = free_men[0]
        idx = next_proposal_index[m]
        w = men_pref[m][idx]
        next_proposal_index[m] = idx + 1

        if w not in engagements:
            engagements[w] = m
            free_men.pop(0)
        else:
            current = engagements[w]
            if women_rank[w][m] < women_rank[w][current]:
                engagements[w] = m
                free_men.pop(0)
                free_men.append(current)
            else:
                # 被拒绝的男人继续 free，不从队列里删掉，让他以后再追下一个
                pass

    man_match = {}
    for w, m in engagements.items():
        man_match[m] = w
    return man_match


def run_one_file(filename, show_pairs=10):
    men, women, men_pref, women_pref = read_preferences(filename)
    print("========== Input file:", filename, "==========")
    print("Number of pairs:", len(men))
    print("First 3 men and their preferences:")
    for m in men[:3]:
        print(m, "->", men_pref[m])

    matching = gale_shapley(men, women, men_pref, women_pref)

    print("\nSample of matching (man -> woman):")
    count = 0
    for m in men:
        print(m, "->", matching[m])
        count += 1
        if count >= show_pairs:
            break
    print("========================================\n")


run_one_file("marraige_ten.txt", show_pairs=10)
run_one_file("marriage_hundred.txt", show_pairs=15)
run_one_file("marraige_thousand.txt", show_pairs=15)


# In[ ]:




