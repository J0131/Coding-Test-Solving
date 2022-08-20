n = int(input())
count = 0
ori = n
real = -1

while real != n :
    div = ori % 10 + ori // 10
    real = (ori % 10) * 10 + div % 10
    ori = real
    count += 1

print(count)
