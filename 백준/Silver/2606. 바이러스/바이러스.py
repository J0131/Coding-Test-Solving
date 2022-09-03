n = int(input())

a = int(input())
n_dict = dict()
n_list = list()
ans_list = list()

for i in range(a):
    b,c = map(int,input().split())
    if b not in n_dict:
        n_dict[b] = [c]
    else :
        n_dict[b].append(c) 
    
    if c not in n_dict:
        n_dict[c] = [b]
    else:
        n_dict[c].append(b)

n_list.append(1)

while n_list:
    pp = n_list.pop(0)
    if pp not in ans_list:
        ans_list.append(pp)
        n_list.extend(n_dict[pp])

print(len(ans_list)-1)