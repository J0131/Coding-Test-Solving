import sys
sys.setrecursionlimit(10**6)

def find_worm(n_list,m,n,start):


    if start[0] < m and start[1] < n and start[0] >= 0 and start[1] >= 0 and n_list:
        if start in n_list:
            n_list.remove(start)
            find_worm(n_list,m,n,[start[0],start[1] + 1])
            find_worm(n_list,m,n,[start[0]+1,start[1]])
            find_worm(n_list,m,n,[start[0]-1,start[1]])
            find_worm(n_list,m,n,[start[0],start[1]-1])

a = int(input())

for i in range(a):
    n_list = list()
    start = [0,0]
    count = 0
    m,n,k = map(int,input().split())
    for j in range(k):
        n_list.append(list(map(int,input().split())))
    
    while n_list:
        find_worm(n_list,m,n,n_list[0])
        count += 1

    print(count)