def dfs_iterative(graph, start):
    """
    깊이 우선 탐색(DFS) 반복문(스택) 방식 템플릿

    :param graph: 그래프 (인접 리스트 형태)
    :param start: 탐색을 시작할 노드
    """
    stack = [start]  # 탐색을 시작할 노드를 스택에 추가
    visited = set()  # 방문한 노드를 저장할 집합

    while stack:
        node = stack.pop()  # 스택에서 노드 꺼내기

        if node not in visited:  # 아직 방문하지 않았다면
            visited.add(node)  # 방문 처리
            print(node)  # 현재 노드를 처리 (예: 출력, 저장 등)

            # 인접 노드를 스택에 추가 (역순으로 넣어야 올바른 순서로 탐색 가능)
            for neighbor in reversed(graph[node]):  
                if neighbor not in visited:
                    stack.append(neighbor)