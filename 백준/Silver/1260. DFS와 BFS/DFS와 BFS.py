import itertools

def bfs(bfs_dic, v):
    need = list()
    visited = list()

    need.append(v)

    while need:
        node = need.pop(0)

        if node not in visited:
            visited.append(node)
            if node in bfs_dict:
                for i in sorted(bfs_dic[node]):
                    need.append(i)

    return visited

def dfs(dfs_dic, v):
    need = list()
    visited = list()

    need.append(v)

    while need:
        node = need.pop()

        if node not in visited:
            visited.append(node)
            if node in dfs_dict:
                for i in sorted(dfs_dic[node],reverse=True):
                    need.append(i)

    return visited

N, M, V = map(int,input().split())

bfs_dict = dict()
dfs_dict = dict()

for i in range(M):
    a,b = map(int,input().split())
    if a not in bfs_dict:
        bfs_dict[a] = [b]
    else :
        bfs_dict[a].append(b)

    if b not in bfs_dict:
        bfs_dict[b] = [a]
    else :
        bfs_dict[b].append(a)

dfs_dict = bfs_dict

print(*dfs(bfs_dict,V))
print(*bfs(dfs_dict,V))
