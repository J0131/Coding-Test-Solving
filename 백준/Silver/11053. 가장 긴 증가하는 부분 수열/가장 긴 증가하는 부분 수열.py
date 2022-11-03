import sys

n = int(input())

n_list = list(map(int,sys.stdin.readline().split()))
dp = [1] * (n)



for i in range(1,len(n_list)):
    for j in range(i):
        if n_list[i] > n_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))