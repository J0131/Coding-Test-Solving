n = int(input())

n_list = [0]+list(map(int,input().split()))

seq_list = [0] * (n+1)

for i in range(1,n+1):
    if i == 1:
        seq_list[n_list[1]+1] = 1
    
    else:
        count = 0
        j = 1

        while count < n_list[i] :
            if seq_list[j] == 0:
                count += 1
            j += 1

        for k in range(j,n+1):
            if seq_list[k] < i and seq_list[k] != 0:
                j += 1
            else :
                break

        seq_list[j] = i

    
print(*seq_list[1:])