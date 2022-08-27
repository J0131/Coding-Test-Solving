n = input()
n_list = list()

for i in n:
    n_list.append(int(i))

n_list.sort(reverse=True)
n_list = ''.join([str(i) for i in n_list])
print(n_list)