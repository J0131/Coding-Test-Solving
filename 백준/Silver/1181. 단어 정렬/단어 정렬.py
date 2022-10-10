n = int(input())
n_list = set()

for _ in range(n):
    n_list.add(input().strip())

n_list = list(n_list)
n_list.sort(key = lambda x : (len(x), str(x)))

for i in n_list:
    print(i)
