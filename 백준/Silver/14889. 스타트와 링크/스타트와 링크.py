import itertools
import sys

n = int(input())

n_list = [[0]*n for _ in range(n)]
ans_list = list()
combi = [i for i in range(n)]

for i in range(n):
    nn_list = list(map(int,input().split()))

    for j in range(n):
        n_list[i][j] = nn_list[j]


com_list = list(itertools.combinations(combi,n//2))
min = 100

for i in com_list:
    sum1 = 0
    sum2 = 0
    
    combi = [k for k in range(n)]
    
    for j in i:
        combi.remove(j)

    start_team = list(itertools.combinations(i,2))
    link_team = list(itertools.combinations(combi,2))

    for l in start_team:
        sum1 += n_list[l[0]][l[1]] + n_list[l[1]][l[0]]

    for m in link_team:
        sum2 += n_list[m[0]][m[1]] + n_list[m[1]][m[0]]

    if abs(sum1 - sum2) < min:
        min = abs(sum1 - sum2)

print(min)
