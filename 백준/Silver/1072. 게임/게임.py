def BinarySearch(x, y):
    z = y*100//x
    if z >= 99 or x == y:
        print(-1)
        exit()
    count = x
    win = y
    left = 0
    right = x

    while left < right:
        mid = (left + right) // 2
        if (y+mid)*100 // (x+mid) <= z:
            left = mid + 1
        else:
            right = mid 

    return left

x, y = map(int,input().split())
print(BinarySearch(x,y))
