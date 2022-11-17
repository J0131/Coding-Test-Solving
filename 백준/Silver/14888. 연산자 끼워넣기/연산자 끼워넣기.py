import sys
from collections import deque
from itertools import permutations

n = int(input())

n_list = list(map(int, sys.stdin.readline().split()))

cal_input = list(map(int, sys.stdin.readline().split()))

cal = ['+','-','*','//']
cal_list = []

for i in range(4):
  
  if cal_input[i] != 0:

    for j in range(cal_input[i]):
      cal_list.append(cal[i])

num_case = list(permutations(cal_list, len(cal_list)))
q = deque(num_case)

max_result = -1e9
min_result = 1e9

while q:
  
  now_list = q.popleft()
  result = n_list[0]
  
  for i in range(1, len(n_list)):
    
    if now_list[i-1] == '+':
      result += n_list[i]
   
    elif now_list[i-1] == '-':
      result -= n_list[i]
    
    elif now_list[i-1] == '*':
      result *= n_list[i]
    
    else:
      if result < 0:
        result = -(abs(result) // n_list[i])
      else:
        result = result // n_list[i]    
  
  max_result = max(max_result, result)
  min_result = min(min_result, result)


print(max_result)
print(min_result)