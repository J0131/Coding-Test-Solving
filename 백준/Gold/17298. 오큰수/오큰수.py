n = int(input())

n_list = list(map(int,input().split()))
stack_list = list()
o_large = [-1] * n
    
for i in range(n):
    x = n_list[i]
    if len(stack_list) == 0 or stack_list[-1][0] >= x:
        stack_list.append((x,i))
    else :
        while len(stack_list) > 0:
            pre, idx = stack_list.pop()
            if pre >= x:
                stack_list.append((pre,idx))
                break
            else:
                o_large[idx] = x
        stack_list.append((x,i))

print(*o_large)
