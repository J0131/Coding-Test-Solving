n = int(input())

n_list = list()

for i in range(n):
    n_list.append(list(map(int,input().split())))

for i in range(1,n):
    n_list[i][0] = min(n_list[i-1][1],n_list[i-1][2]) + n_list[i][0]
    n_list[i][1] = min(n_list[i-1][0],n_list[i-1][2]) + n_list[i][1]
    n_list[i][2] = min(n_list[i-1][0],n_list[i-1][1]) + n_list[i][2]

print(min(n_list[n-1][0],n_list[n-1][1],n_list[n-1][2]))