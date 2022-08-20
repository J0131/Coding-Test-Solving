def sum_atm(list_1):
    list_2=list()
    sum2 = 0
    for i in range(1,len(list_1)+1):
        sum = 0
        for j in range(i):
            sum += list_1[j]        
    #list_2.append(sum)
        sum2 += sum
    return sum2 

n = input()

a=[]
a=input().split()
a = list(map(int, a))
a.sort()

print(sum_atm(a))
