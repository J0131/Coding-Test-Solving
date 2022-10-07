import sys

a = -1
b = -1

while True:
    q = list()
    n_list = []
    one_list = []
    count = 0

    a,b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    for _ in range(b):
        n_list.append(list(map(int, sys.stdin.readline().split())))

    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [1,0,-1,1,-1,1,0,-1]

    for i in range(b):
        for j in range(a):
            if n_list[i][j] == 1:
                one_list.append([i,j])

    connected = list()

    while one_list:
        
        connected.append(one_list.pop(0))

        while connected:
            left = connected.pop(0)

            for k in range(8):
                x = left[0] + dx[k]
                y = left[1] + dy[k]
                    
                if 0 <= x < b and 0 <= y < a:
                    if n_list[x][y] == 1:
                        if [x,y] in one_list:
                            one_list.remove([x,y])
                            connected.append([x,y])
    
        count += 1

    print(count)