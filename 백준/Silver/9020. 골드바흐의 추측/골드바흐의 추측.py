import sys

global primelist

def prime(num):
    global primelist

    for j in range(2,num):
        for i in range(2,j+1):
            if i != j and j % i == 0:
                primelist[j] = False

n = int(input())
primelist = [True] * 10000
prime(10000)

for _ in range(n):
    min = 10000
    answer = []
    gold_partition = list()
    gold = int(sys.stdin.readline().strip())

    for i in range(2,gold//2+1):
        if primelist[i] == True and primelist[gold-i] == True:
            if abs(i-(gold-i)) < min:
                min = abs(i-(gold-i))
                answer = [i,gold-i]
            #gold_partition.append([i,gold-i])
        
    #gold_partition.sort(key = lambda x : abs(x[0]-x[1]))
    print(*answer)