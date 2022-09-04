import sys

n = int(input())
n_list = list()

for _ in range(n):
    a = int(sys.stdin.readline().strip())
    if a == 0:
        n_list.pop()
    else:
        n_list.append(a)

print(sum(n_list))