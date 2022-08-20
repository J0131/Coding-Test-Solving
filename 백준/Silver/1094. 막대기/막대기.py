a = int(input())
start = 64
result = 0
count = 0

while a != 0:
    if a // start > 0:
        a = a - start
        count += 1
    start = start >> 1

print(count)