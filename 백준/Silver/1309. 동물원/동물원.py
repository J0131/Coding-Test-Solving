n = int(input())

f = [[0]*3 for i in range(n+1)]

for i in range(3):
    f[1][i] = 1

for i in range(2,n+1):
    f[i][0] = (f[i-1][1] + f[i-1][2])%9901
    f[i][1] = (f[i-1][0] + f[i-1][2])%9901
    f[i][2] = (f[i-1][0] + f[i-1][1] + f[i-1][2])%9901


print(sum(f[n])%9901)