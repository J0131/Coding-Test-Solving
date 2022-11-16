import sys
from collections import deque

n, m = list(map(int,sys.stdin.readline().split()))
n_list = list(map(int,sys.stdin.readline().split()))

sum_list = [0] * (len(n_list)+1)
sum_list[1] = n_list[0]


for i in range(2,len(n_list)+1):
    sum_list[i] = sum_list[i-1] + n_list[i-1]

for _ in range(m):

    a, b = list(map(int,sys.stdin.readline().split()))

    print(sum_list[b] - sum_list[a-1])
