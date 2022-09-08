n = input()
gan = 0
count = 0
nn = '1'

while int(nn) <= int(n):
    for i in range(len(nn)):
        if i == 1:
            gan = int(nn[i])-int(nn[i-1])
        elif i > 1:
            if int(nn[i])-int(nn[i-1]) == gan:
                count += 1
    if len(nn) == 1 or len(nn) == 2:
        count += 1
    nn = str(int(nn) + 1)

print(count)