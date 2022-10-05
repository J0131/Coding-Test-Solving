import sys
from itertools import combinations
import collections


n_dict = dict()
n_set = set()

n, m = map(int,input().split())
n_set = [i for i in range(1,n+1)]

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    if a not in n_dict:
        n_dict[a] = [b]
    else :
        n_dict[a].append(b)
    
    if b not in n_dict:
        n_dict[b] = [a]
    else :
        n_dict[b].append(a)

count = 0

while n_set:
    q = collections.deque()
    q.append(list(n_set)[0])
    visited = []

    while q:
        node = q.popleft()

        if node not in visited:
            visited.append(node)   
            if node in n_dict:
                for j in n_dict[node]:
                    if j not in visited:
                        q.append(j)

    for k in visited:
        n_set.remove(k)

    count += 1

if count == 0:
    count = 1

print(count)


