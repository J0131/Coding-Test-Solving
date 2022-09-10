n = int(input())

n_list = [0] + list(map(int,input().split()))
n_dict = dict()
dp = [0] * (n+1)

dp[1] = n_list[1]

for i in range(2,n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], dp[i-j] + n_list[j])

print(dp[n])