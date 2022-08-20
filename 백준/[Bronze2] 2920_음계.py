def judge(list_1):
    ascend_list = [1,2,3,4,5,6,7,8]
    descend_list = [8,7,6,5,4,3,2,1]
    
    if list_1 == ascend_list:
        return "ascending"
        
    elif list_1 == descend_list:
        return "descending"

    else:
        return "mixed"

a = input().split()
a = list(map(int,a))
print(judge(a))
