

n = int(input())
count = 0

while n != 0:
    if n >= 3:
        n -= 3
        count += 1
    elif 0 < n < 3 :
        n -= 1
        count += 1
    
    if n >= 3:
        n -= 3
        count += 1
    elif 0 < n < 3 :
        n -= 1
        count += 1

if count % 2 == 1:
    print("SK")
elif count % 2 == 0:
    print("CY")


