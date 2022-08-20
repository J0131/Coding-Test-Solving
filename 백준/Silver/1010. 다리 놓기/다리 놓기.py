from itertools import combinations
import math

n = int(input())

for i in range(n):
    a,b = input().split()
    a,b= int(a),int(b)
    if a<b:
        a,b=b,a
    print(math.factorial(a)//(math.factorial(a-b)*math.factorial(b)))