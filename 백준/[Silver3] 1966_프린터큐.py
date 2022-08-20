n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    c = list(map(int,input().split()))
    c = [(i,idx) for idx,i in enumerate(c)]

    #print(c[0][1])
    count = 0

    while True:
        list_e = list()
        for i in range (len(c)):
            list_e.append(c[i][0])

        if c[0][0] == max(list_e):
            if c[0][1] == b:
                count+=1
                break 
            c.pop(0)
            count += 1
            
        else :
            c.append(c.pop(0))
    
    print(count)
