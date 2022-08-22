n = int(input())
count = n
dict_group = dict()

for i in range(n):
    group = input()
    list_group = list()

    for k in group:
        if k not in list_group or list_group[-1] == k: 
            list_group.append(k)
            
        else :
            count -= 1
            break
    
print(count)