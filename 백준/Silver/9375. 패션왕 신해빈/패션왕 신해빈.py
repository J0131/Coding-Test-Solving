n = int(input())

for _ in range(n):
    sum = 0
    n_dict = dict()
    n_set = set()
    n2 = int(input())
    n_list = list()
    for i in range(n2):
        a,b = input().split()
        n_set.add(b)
        if b not in n_dict:
            n_dict[b] = [a]
        else :
            n_dict[b].append(a)

    for i in n_set:
        n_list.append(len(n_dict[i]))
    
    idx = 1
    for i in n_list:
        if len(n_list) != 1:
            idx *= (i+1)
        else :
            idx = i + 1

    print(idx-1)