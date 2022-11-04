import sys

n = int(input())

if n == 1 or n== 3:
    print(-1)
    sys.exit()

count5 = n // 5

n = n % 5


while True:

    if n % 2 != 0:
        n += 5
        count5 -=1
    
    else :
        break

count2 = n // 2

print(count5 + count2)