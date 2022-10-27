n = int(input())
nn_list = list(map(int,input().split()))

n_list = [i for i in range(1,n+1)]

k = -1
for i in range(len(nn_list)-1):
    if nn_list[i] > nn_list[i+1]:
        k = i

if k == -1:
    print(-1)
else :
    for i in range(k+1,len(nn_list)):
        if nn_list[i] < nn_list[k]:
            m = i

    nn_list[k], nn_list[m] = nn_list[m], nn_list[k]

    answer = nn_list[:k+1] + sorted(nn_list[k+1:],reverse=True)

    print(*answer)