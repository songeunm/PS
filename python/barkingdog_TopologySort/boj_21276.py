# 계보 복원가 호석

import sys
from collections import deque
input = sys.stdin.readline

# output
# line 1: 가문의 개수 k
# line 2: 가문 시조들의 이름 사전순 나열
# line 3: 이름 사전순대로 이름, 자식의 수, 자식들 이름 사전순 나열

def TopologySort(g: dict, indegree: dict):
    # 시조 리스트
    root = []
    for name in indegree.keys():
        if indegree[name] == 0:
            root.append(name)
    # 자식 리스트
    child = {name: [] for name in g.keys()}

    q = deque()
    # 큐 초기값 삽입
    for r in root:
        q.append(r)
        # 순환 및 진입 차수 감소
        while q:
            anc = q.popleft()
            for desc in g[anc]:
                indegree[desc] -= 1
                if indegree[desc] == 0:
                    q.append(desc)
                    child[anc].append(desc)
    return root, child

if __name__ == "__main__":
    n = int(input())
    names = input().split()
    m = int(input())
    g = {name: [] for name in names}
    indegree = {name: 0 for name in names}
    for i in range(m):
        descendant, ancestor = input().split()
        g[ancestor].append(descendant)
        indegree[descendant] += 1

    root, child = TopologySort(g, indegree)
    print(len(root))
    print(* sorted(root))
    for name in sorted(child.keys()):
        print(name, len(child[name]), end=" ")
        print(*sorted(child[name]))