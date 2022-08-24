n = int(input())
a = list(map(int,input().split()))

b = list()
for i in a:
    b.append(i/max(a)*100)

print(sum(b)/n)