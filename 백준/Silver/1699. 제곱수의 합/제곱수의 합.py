import math

n = int(input())


idx = 0
dp = [x for x in range(n+1)]

dp[1] = 1

for i in range(1,n+1):
    for j in range(1,i):
        if j*j > i:
            break
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1 

print(dp[n])