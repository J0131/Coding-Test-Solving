import math
import itertools
import sys
import copy

n = int(input())

n_list = []

for _ in range(n):
    n_list.append(list(map(int,sys.stdin.readline().split())))

answer = []

for i in n_list:
    num = 1
    for j in n_list:
        if i[0] < j[0] and i[1] < j[1]:
            num += 1
    answer.append(num)

print(*answer)