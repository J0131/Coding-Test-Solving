n = int(input())
count = 0

n_list = [0 for _ in range(91)]

n_list[1] = 1
n_list[2] = 1

for i in range(3,91):
    n_list[i] = n_list[i-1] + n_list[i-2]

print(n_list[n])
