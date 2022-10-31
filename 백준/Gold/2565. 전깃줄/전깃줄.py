import sys

n = int(input())

n_list = []

for _ in range(n):
    n_list.append(list(map(int,sys.stdin.readline().split())))


n_list.sort(key= lambda x : x[0])

dp = [1] * (n+1)

for i in range(len(n_list)):
    x,y = n_list[i]
    for j in range(0, i):
        if n_list[j][1] < y:
            dp[i] = max(dp[i],dp[j]+1)

print(len(n_list) - max(dp))