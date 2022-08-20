n = int(input())

for _ in range(n):
    list_emp = list()
    idx = 0
    s = input()
    left = list()
    right = list()

    for z in s:
        if z == "<":
            if left:
                right.append(left.pop())
        elif z == ">": 
            if right:
                left.append(right.pop())
        elif z == "-":
            if left:
                left.pop()
        else :
            left.append(z)
    
    left.extend(reversed(right))
    print(*left,sep="")
