"""
어떤 도화지에 그림이 그려져 있을 때, 그 그림의 개수와,
그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하라    
단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자.
가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 
그림의 넓이란 그림에 포함된 1의 개수이다.
"""
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        node = queue.popleft()
        print(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

n = map(int,input().split())

for _ in range(n):
    map(int,input().split())

