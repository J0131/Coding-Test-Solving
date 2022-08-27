n,k = map(int,input().split())
n_list = list()
ans_list = list()
num = 0

for i in range(1,n+1):
    n_list.append(i)

while n_list:
    num += k-1  
    if num >= len(n_list):   # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
        num = num%len(n_list)
 
    ans_list.append(str(n_list.pop(num)))

print("<",end='')
for i in ans_list:
    print(i,end='')
    if i != ans_list[-1]:
        print(", ",end='')
print(">")    