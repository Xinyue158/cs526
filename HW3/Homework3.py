#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


#Problem 1
count = 0

file = open("palendrome_0.txt", "r")

output = open("output.txt", "w")

for line in file:
    word = line.strip()
    if word == word[::-1]:
        output.write("true\n")
        count = count + 1
    else:
        output.write("false\n")

output.write(str(count))

file.close()
output.close()

print("Program finished. Results written to output.txt.")


# In[11]:


text = "abcab"

seen = set()
result = []
length = len(text)

def extend(start, end):
    if end > length:
        return
    substring = text[start:end]
    if substring not in seen:
        seen.add(substring)
        result.append(substring)
    extend(start, end + 1)

def generate(start_index):
    if start_index >= length:
        return
    extend(start_index, start_index + 1)
    generate(start_index + 1)

generate(0)

print(", ".join(result) + " -> " + str(len(result)))


# In[9]:


vals = [1,2,3,4,5,6,7,8,9,10]


arr = []
def push_arr(x):
    arr.append(x)
def pop_arr():
    return arr.pop()

for v in vals:
    push_arr(v)

def insert_bottom_arr(x):
    if not arr:
        arr.append(x)
        return
    t = pop_arr()
    insert_bottom_arr(x)
    push_arr(t)

def reverse_stack_array():
    if not arr:
        return
    t = pop_arr()
    reverse_stack_array()
    insert_bottom_arr(t)

reverse_stack_array()
print(", ".join(str(x) for x in arr))


class NodeS:
    def __init__(self, v):
        self.v = v
        self.next = None

head_s = None

def push_s(x):
    global head_s
    n = NodeS(x)
    n.next = head_s
    head_s = n

def pop_s():
    global head_s
    t = head_s
    head_s = head_s.next
    return t.v

for v in vals:
    push_s(v)

def reverse_list_s(node):
    if node is None or node.next is None:
        return node
    rest = reverse_list_s(node.next)
    node.next.next = node
    node.next = None
    return rest

head_s = reverse_list_s(head_s)

cur = head_s
out = []
while cur:
    out.append(cur.v)
    cur = cur.next
print(", ".join(str(x) for x in out))

# ==== 3) Stack as Doubly Linked List ====
class NodeD:
    def __init__(self, v):
        self.v = v
        self.prev = None
        self.next = None

head_d = None

def push_d(x):
    global head_d
    n = NodeD(x)
    n.next = head_d
    if head_d:
        head_d.prev = n
    head_d = n

def pop_d():
    global head_d
    t = head_d
    head_d = head_d.next
    if head_d:
        head_d.prev = None
    return t.v

for v in vals:
    push_d(v)

def reverse_list_d(node):
    if node is None:
        return None
    node.prev, node.next = node.next, node.prev
    if node.prev is None:
        return node
    return reverse_list_d(node.prev)

head_d = reverse_list_d(head_d)

cur = head_d
out2 = []
while cur:
    out2.append(cur.v)
    cur = cur.next
print(", ".join(str(x) for x in out2))


# In[10]:


fname = "ghostbusters_input_0.txt"

def orient(ax, ay, bx, by, cx, cy):
    v = (by - ay) * (cx - bx) - (bx - ax) * (cy - by)
    if v > 0:
        return 1
    if v < 0:
        return -1
    return 0

def on_segment(ax, ay, bx, by, cx, cy):
    return min(ax, cx) <= bx <= max(ax, cx) and min(ay, cy) <= by <= max(ay, cy)

def check_intersect(a1, a2, b1, b2):
    ax, ay = a1
    cx, cy = a2
    bx, by = b1
    dx, dy = b2
    o1 = orient(ax, ay, cx, cy, bx, by)
    o2 = orient(ax, ay, cx, cy, dx, dy)
    o3 = orient(bx, by, dx, dy, ax, ay)
    o4 = orient(bx, by, dx, dy, cx, cy)
    if o1 != o2 and o3 != o4:
        return True
    if o1 == 0 and on_segment(ax, ay, bx, by, cx, cy):
        return True
    if o2 == 0 and on_segment(ax, ay, dx, dy, cx, cy):
        return True
    if o3 == 0 and on_segment(bx, by, ax, ay, dx, dy):
        return True
    if o4 == 0 and on_segment(bx, by, cx, cy, dx, dy):
        return True
    return False

f = open(fname, "r")
n = int(f.readline().strip())
pairs = []

for _ in range(n):
    data = f.readline().split()
    bx = by = gx = gy = 0
    i = 0
    while i < len(data):
        if data[i] == "B":
            bx = float(data[i+1])
            by = float(data[i+2])
        if data[i] == "G":
            gx = float(data[i+1])
            gy = float(data[i+2])
        i = i + 3
    pairs.append(((bx, by), (gx, gy)))
f.close()

ok = True
for i in range(len(pairs)):
    for j in range(i + 1, len(pairs)):
        if check_intersect(pairs[i][0], pairs[i][1], pairs[j][0], pairs[j][1]):
            ok = False
            break
    if not ok:
        break

if ok:
    print("All Ghosts: were eliminated")
else:
    print("All Ghosts: were not eliminated")


# In[3]:





# In[ ]:





# In[ ]:




