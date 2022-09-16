import itertools
import sys

n = list()
count = 0

while n != [0]:
    n = list(map(int,input().split()))
    if count != 0:
        print("")
        
    nn = n[0]
    nn_list = n[1:]

    n_list = list(itertools.combinations(nn_list,6))
    
    for i in n_list:
        print(*i)

    count += 1