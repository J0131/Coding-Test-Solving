n = int(input())
n_dict = dict()
ans_list = list()
real_list = list()

for i in range(n):
    a = input()
    if a not in n_dict:
        n_dict[a] = 0
    else:
        n_dict[a] += 1

for i in n_dict.values():
    ans_list.append(i)

for k,v in n_dict.items():
    if v == max(ans_list):
        real_list.append(k)

real_list.sort()
print(real_list[0])