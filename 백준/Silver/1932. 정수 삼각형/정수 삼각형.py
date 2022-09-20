import sys

n = int(input())

n_list = [[] for _ in range(n)]
dp_list = [0]*(n+1)

for i in range(0,n):
    n_list[i] = list(map(int,sys.stdin.readline().split()))

if n > 1:
    n_list[1][0] = n_list[1][0] + n_list[0][0]
    n_list[1][1] = n_list[1][1] + n_list[0][0]

    if n > 2:
        for i in range(2,n):
            for j in range(0,len(n_list[i])):
                    #dp_list[i] = max(dp_list[i],dp_list[i-1]+n_list[i][j])
                    if j == 0 :
                        n_list[i][j] = n_list[i-1][j]+n_list[i][j]
                    elif j == len(n_list[i])-1:
                        n_list[i][j] = n_list[i-1][j-1]+n_list[i][j]
                    else :
                        n_list[i][j] = max(n_list[i-1][j-1]+n_list[i][j],n_list[i-1][j]+n_list[i][j])


print(max(n_list[n-1]))