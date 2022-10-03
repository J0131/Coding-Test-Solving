import sys
from itertools import combinations
import collections

n = int(input())
count = 0

n_list = []

if n >= 5:
    div5 = n // 5

    for i in range(1,div5+1):
        if (n - (5*i)) % 3 == 0:
            n_list.append(i)
    
    if not n_list:
        if n % 3 == 0:
            print(n // 3)
        else :
            print(-1)
        sys.exit()

    print(max(n_list) + ((n - (5*max(n_list))) // 3))

else:
    if n % 3 != 0:
        print(-1)
    else:
        print(1)


#print(n_list)

    
