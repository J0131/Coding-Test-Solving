n,m = map(int,input().split())
list_pack = list()
list_one = list()

for i in range(m):
    a,b = map(int,input().split())
    list_pack.append(a)
    list_one.append(b)

if  min(list_one) * 6 < min(list_pack):
    count = n * min(list_one)
else :
    count = n // 6 * min(list_pack)
    if n % 6 * min(list_one) > min(list_pack) :
        count +=  min(list_pack)
    else :
        count += n % 6 *min(list_one)

print(count)