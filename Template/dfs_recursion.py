def dfs(graph, node, visited):
    """
    깊이 우선 탐색(DFS) 재귀 방식 템플릿

    :param graph: 그래프 (인접 리스트 형태)
    :param node: 현재 탐색할 노드
    :param visited: 방문한 노드를 저장하는 집합(set)
    """
    if node not in visited:  # 아직 방문하지 않았다면
        visited.add(node)  # 현재 노드를 방문 처리
        print(node)  # 현재 노드를 처리 (예: 출력, 저장 등)

        for neighbor in graph[node]:  # 현재 노드의 인접 노드를 순회
            dfs(graph, neighbor, visited)  # 재귀적으로 DFS 호출