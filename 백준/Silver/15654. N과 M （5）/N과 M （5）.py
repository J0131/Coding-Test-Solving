import itertools

n, m = map(int, input().split())

n_list = list(map(int, input().split()))


comb_list = list(itertools.permutations(n_list, m))

#print(comb_list)

comb_list.sort()

for i in comb_list:
    print(*i)