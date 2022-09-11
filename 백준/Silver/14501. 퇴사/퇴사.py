n = int(input())
n_list = [[0,0]]
dp = [0] * (n+2)


for _ in range(n):
    n_list.append(list(map(int,input().split())))

for i in range(len(n_list)-1,-1,-1):
    if n_list[i][0] + i - 1 > n:
        dp[i] = dp[i+1]
    else :
        dp[i] = max(dp[i+1], n_list[i][1] + dp[i+n_list[i][0]])

print(dp[0])