import sys

n = int(input())
n_list = [0]
dp = [0] * (n+1)

for _ in range(n):
    n_list.append(int(sys.stdin.readline().strip()))

dp[1] = n_list[1]

if n>= 2:
    dp[2] = n_list[1] + n_list[2]
#dp[3] = max(n_list[-1]+n_list[-2],n_list[-1]+n_list[-3])
#print("---------------")

    if n>= 3:
        for i in range(3,n+1):
            dp[i] = max(dp[i-3]+n_list[i]+n_list[i-1],dp[i-2]+n_list[i])

print(dp[n])