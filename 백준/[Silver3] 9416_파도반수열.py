n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

p = [0,1,1,1,2,2,3,4,5,7,9]

for i in range(11,101):
    p.append(p[i-1]+p[i-5])

for i in range(n):
    print(p[a[i]])
