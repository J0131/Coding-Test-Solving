def twoFind(left,right,key):

    while left <= right:
        mid = (left+right) // 2 
        
        if key == list_ans[mid]:
            return 1

        elif key > list_ans[mid]:
            left = mid + 1
    
        else :
            right = mid - 1

    return 0

n = int(input())
list_ans = list(map(int,input().split()))

list_ans.sort()

n2 = int(input())
list_ans2 = list(map(int,input().split()))

for i in list_ans2:
    if twoFind(0,n-1,i) == 1:
        print(1)
    else:
        print(0)