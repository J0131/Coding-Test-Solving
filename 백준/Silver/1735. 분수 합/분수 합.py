
def division(a,b):
    
    while a % b != 0:
        mod = a % b
        a = b
        b = mod
    return b

a1, a2 = map(int,input().split())
b1, b2 = map(int, input().split())

sum1 = division(a1*b2 + a2*b1, a2 * b2)

print((a1*b2 + a2*b1)//sum1, (a2*b2)//sum1)
