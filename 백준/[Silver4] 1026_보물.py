from itertools import combinations
import math

n = int(input())
c = 0
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort(reverse=True)
b.sort()

for i in range(n):
    c += a[i] * b[i]

print(c)
