n = int(input())
list_int = list(map(int,input().split()))
list_int2 = list()

for i in range(len(list_int)):
    count = 0
    for j in range(len(list_int)):
        if i != j and list_int[i] > list_int[j]:
            count+=1
        if i > j and list_int[i] == list_int[j]:
            count+=1
    list_int2.append(count)

for k in list_int2:
    print(k,end=' ')