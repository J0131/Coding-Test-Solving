
n = input()

n_list = set()


for i in range(1,len(n)+1):
    for j in range(0, len(n)-i+1):
            n_list.add(n[j:j+i])

print(len(n_list))