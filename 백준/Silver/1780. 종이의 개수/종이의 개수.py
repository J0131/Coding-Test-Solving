import sys

count_one = 0
count_minusone = 0
count_zero = 0

def mod(n_list):
    global count_one
    global count_minusone
    global count_zero

    if len(n_list) == 3:
        for i in range(3):
            for j in range(3):
                if n_list[i][j] == 1:
                    count_one += 1
                elif n_list[i][j] == 0:
                    count_zero += 1
                elif n_list[i][j] == -1:
                    count_minusone += 1
        return

    lens = len(n_list) // 3 
    mod_list = [[0]*lens for _ in range(lens)]

    for i in range(9):
        for j in range(lens):
            for k in range(lens):
                if i < 3:
                    mod_list[j][k] = n_list[j][k+i%3*lens]
                elif i >= 3 and i < 6:
                    mod_list[j][k] = n_list[j+lens][k+i%3*lens]
                elif i >= 6:
                    mod_list[j][k] = n_list[j+lens*2][k+i%3*lens]

        if descision(mod_list, lens) == False:
            mod(mod_list)


def descision(mod_list, lens):

    global count_one
    global count_minusone
    global count_zero

    for j in range(lens):
        for k in range(lens):
            if j == 0 and k == 0:
                pre = mod_list[j][k] 

            if mod_list[j][k] == pre:
                pre = mod_list[j][k]
                if j == lens-1 and k == lens-1:
                    if pre == 1:
                        count_one += 1
                    elif pre == 0:
                        count_zero += 1
                    elif pre == -1:
                        count_minusone += 1
                    return True
            else :
                return False


n = int(input())
n_list = [[0]*n for _ in range(n)]

for i in range(n):
    n_list[i] = list(map(int, sys.stdin.readline().split()))

if descision(n_list, len(n_list)) == False:
    mod(n_list) 

print(count_minusone)
print(count_zero)
print(count_one)