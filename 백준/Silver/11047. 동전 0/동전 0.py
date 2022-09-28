import sys
from itertools import combinations

n, k = map(int, input().split())

coin_list = list()

for _ in range(n):
    coin_list.append(int(sys.stdin.readline().strip()))

coin_reverse = sorted(coin_list, reverse = True)
max_v = 0

for i in coin_reverse:
    if k - i >= 0:
        max_v = i
        break

idx = coin_list.index(max_v)
coin_ans = 0

while k != 0:
    count = k // coin_list[idx]
    k -= count*coin_list[idx]
    coin_ans += count
    idx -= 1
   
print(coin_ans)