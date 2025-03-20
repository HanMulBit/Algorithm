from collections import deque

def bfs(n, k):
    max_limit = 100001
    visited = [False] * max_limit
    queue = deque([(n, 0)])
    
    while queue:
        current, time = queue.popleft()

        if current == k:
            return time

        if visited[current]:
            continue
        visited[current] = True

        if current - 1 >= 0 and not visited[current - 1]:
            queue.append((current - 1, time + 1))
        if current + 1 < max_limit and not visited[current + 1]:
            queue.append((current + 1, time + 1))
        if current * 2 < max_limit and not visited[current * 2]:
            queue.append((current * 2, time + 1))

n, k = map(int, input().split())
print(bfs(n, k))