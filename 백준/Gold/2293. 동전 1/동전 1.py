import sys
from itertools import combinations

n, k = map(int, input().split())

dp = [0] * (k+1)

coin_list = []

for _ in range(n):
    coin_list.append(int(input()))

dp[0] =1

for i in coin_list:
    for j in range(i, k+1):
        pre = dp[j-i]
        dp[j] += pre

print(dp[k])