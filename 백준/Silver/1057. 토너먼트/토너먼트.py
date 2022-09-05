n, a, b = map(int,input().split())

n_list = [-1] * n
n_list[a-1] = a
n_list[b-1] = b
count = 0

while len(n_list) > 1:
    next_list = list()
    count += 1
    for i in range(0,len(n_list)-1,2):

        if n_list[i] != a and n_list[i] != b and n_list[i+1] != a and n_list[i+1] != b:
            next_list.append(-1)
        elif n_list[i] == a and n_list[i+1] == b:
            print(count)
            exit()
        elif n_list[i] == b and n_list[i+1] == a:
            print(count)
            exit()
        elif n_list[i] == a or n_list[i+1] == a:
            next_list.append(a)
        elif n_list[i] == b or n_list[i+1] == b:
            next_list.append(b)
        
        if len(n_list) % 2 == 1 and i == len(n_list)-3:
            next_list.append(n_list[-1])
    n_list = next_list

print(count)