import sys
import copy
from collections import deque 
import itertools

alpha = ['a','e','i','o','u']
ja = ['b','c']
m, n = map(int,input().split())

n_list = list(sys.stdin.readline().split())

n_list.sort()

comb_list = list(itertools.combinations(n_list,m))


for i in comb_list:
    print_list = list()
    mo_count = 0 
    ja_count = 0
    for j in i:
        if j in alpha:
            mo_count += 1
        elif j.islower():
            ja_count += 1

    if mo_count >= 1 and ja_count >= 2:
        print(''.join(k for k in i))
