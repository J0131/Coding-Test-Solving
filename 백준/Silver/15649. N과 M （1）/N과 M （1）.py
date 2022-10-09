import itertools


n, m = map(int,input().split())


n_list = [i for i in range(1,n+1)]


comb_list = list(itertools.permutations(n_list,m))
answer_list = []

for i in comb_list:
    answer_list.append([*i])

for i in answer_list:
    print(*i)
