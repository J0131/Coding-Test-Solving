from itertools import combinations

def judge(list_1,maxi):
    max_value = 0 
    max = list()
    max2 = list()
    max = list(combinations(list_1,3))
    for i in range(len(max)):
        max2.append (sum(max[i]))
    for i in max2:
        if i > max_value and i<= maxi:
            max_value = i

    return max_value
        

n,m = input().split()
n,m = int(n),int(m)
a = input().split()
a = list(map(int,a))
print(judge(a,m))
