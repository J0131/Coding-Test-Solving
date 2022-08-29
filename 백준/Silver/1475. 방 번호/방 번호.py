n = input()
n_dict = dict()
n_list= list()
for i in range(10):
    n_dict[str(i)] = 0

for j in n:
    if j == '9':
        if n_dict['9'] >= n_dict['6']:
            n_dict['6'] += 1
        else:
            n_dict['9'] += 1

    elif j == '6':
        if n_dict['6'] >= n_dict['9']:
            n_dict['9'] += 1
        else:
            n_dict['6'] += 1
    
    else:
        n_dict[str(j)] += 1
    
print(max([i for i in n_dict.values()]))