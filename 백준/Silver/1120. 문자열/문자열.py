def find_diff(a,b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count


a, b = input().split()

min = 50

for i in range(len(b)-len(a)+1):
    s = find_diff(a,b[i:i+len(a)])
    if s < min:
        min = s
    
print(min)