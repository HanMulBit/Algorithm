# dfs와 bfs
from collections import deque

def dfs(graph,v,visit):
    visit[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visit[i]:
            dfs(graph,i,visit)


def bfs(graph,s,visit):
    queue = deque([s])
    visit[s] = True

    while queue:
        v = queue.popleft()
        print(v,end=' ')

        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True


n, m, v = map(int,input().split())
graph = [[]for _ in range(n+1)]

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
    graph[i].sort()

visit_dfs = [False] * (n+1)
visit_bfs = [False] * (n+1)

dfs(graph, v, visit_dfs)
print()

bfs(graph, v, visit_bfs)