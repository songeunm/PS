# K번째로 작은 쌍의 합

import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    n_nums = sorted(list(map(int, input().split())))
    m_nums = sorted(list(map(int, input().split())))
    
    visited_set = set()
    pq = []
    heapq.heappush(pq, (n_nums[0]+m_nums[0], 0, 0))
    visited_set.add((0, 0))
    cnt = 0
    while cnt < k-1:
        val, i, j = heapq.heappop(pq)
        cnt += 1

        if i+1 < n:
            if (i+1, j) not in visited_set:
                heapq.heappush(pq, (n_nums[i+1] + m_nums[j], i+1, j))
                visited_set.add((i+1, j))

        if j+1 < m:
            if (i, j+1) not in visited_set:
                heapq.heappush(pq, (n_nums[i] + m_nums[j+1], i, j+1))
                visited_set.add((i, j+1))
    
    answer, i, j = heapq.heappop(pq)
        
    print(answer)