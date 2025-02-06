# 줄 세우기

import sys
from collections import deque
input = sys.stdin.readline

def TopologySort(g, indegree):
    q = deque()
    result = []
    # 진입 차수가 0인 노드 큐에 삽입
    for node in indegree.keys():
        if indegree[node] == 0:
            q.append(node)
    while q:
        # 큐에서 팝하여 해당 노드에서 나가는 간선 제거 (연결 노드의 진입 차수 감소)
        node = q.popleft()
        result.append(node)
        for next_node in g[node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                q.append(next_node)
    if len(result) != len(g):
        return [] # cycle 존재
    return result


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = {node: [] for node in range(1, n + 1)}
    indegree = {node: 0 for node in range(1, n + 1)}
    for i in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        indegree[b] += 1
    result = TopologySort(g, indegree)
    print(* result)