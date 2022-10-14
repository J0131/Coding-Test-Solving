import itertools
import math
import sys
from collections import deque as dq

def binary_search(str_x, list_x, start, end):
    if start > end:
        return False

    mid = (start+end) // 2
    if list_x[mid] == str_x :
        return True

    elif list_x[mid] > str_x :
        return binary_search(str_x, list_x, start, mid-1)

    elif list_x[mid] < str_x:
        return binary_search(str_x, list_x, mid+1, end)

n, m = map(int,input().split())

hear = list()
see = list()
answer = []


for _ in range(n):
    hear.append(sys.stdin.readline().strip())

for _ in range(m):
    see.append(sys.stdin.readline().strip())

hear.sort()
see.sort()

if len(hear) < len(see):
    for i in hear:
        if binary_search(i,see,0,len(see)-1):
            answer.append(i)
else :
    for i in see:
        if binary_search(i,hear,0,len(hear)-1):
            answer.append(i)

print(len(answer))
for i in answer:
    print(i)