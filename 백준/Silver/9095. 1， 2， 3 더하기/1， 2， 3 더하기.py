import sys
from itertools import combinations


n_list = []
n = int(input())

for _ in range(n):

    n_list.append(int(sys.stdin.readline().strip()))


m = max(n_list)

dp = [0]*(m+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7

for i in range(5,m+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in n_list:
    print(dp[i])