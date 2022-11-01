import sys

n = int(input())
n_list = []

for _ in range(n):

    n_list.append(list(sys.stdin.readline().split()))

n_list.sort(key = lambda x : (int(x[0])))

for i in n_list:
    print(*i)