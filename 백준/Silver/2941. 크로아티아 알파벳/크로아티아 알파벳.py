croa = input()

croa_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

answer = 0

for i in croa_list:
    if i in croa:
        answer += croa.count(i)
        croa = croa.replace(i,'-')

croa = croa.replace('-','')
print(answer + len(croa))