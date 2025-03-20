from collections import deque

def bfs(graph, start):
    """
    너비 우선 탐색(BFS) 템플릿

    :param graph: 그래프 (인접 리스트 형태)
    :param start: 탐색을 시작할 노드
    """
    queue = deque([start])  # 시작 노드를 큐에 추가
    visited = set([start])  # 방문한 노드를 저장하는 집합

    while queue:  # 큐가 빌 때까지 반복
        node = queue.popleft()  # 큐에서 노드를 꺼냄
        print(node)  # 현재 노드를 처리 (예: 출력, 저장 등)

        for neighbor in graph[node]:  # 현재 노드의 인접 노드 탐색
            if neighbor not in visited:  # 아직 방문하지 않았다면
                visited.add(neighbor)  # 방문 처리
                queue.append(neighbor)  # 큐에 추가하여 탐색 확장 