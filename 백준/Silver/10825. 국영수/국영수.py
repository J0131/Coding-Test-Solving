import sys
from itertools import combinations

n = int(input())

n_list = []

for _ in range(n):
    n_list.append(sys.stdin.readline().split())

n_list.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in n_list:
    print(i[0])