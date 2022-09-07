n, m = map(int,input().split())
n_list = list()
m_list = list()
count = 0

for i in range(n):
    n_list.append(input())

for i in range(m):
    m_list.append(input())

for i in m_list:
    if i in n_list:
        count += 1

print(count)