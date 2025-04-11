# 구간 합 구하기
# segment tree

import sys
input = sys.stdin.readline

def init_segtree(nums, tree, node, l, r):
    if l == r:
        tree[node] = nums[l]
    else:
        mid = (l + r) // 2
        tree[node] = init_segtree(nums, tree, node*2, l, mid) + init_segtree(nums, tree, node*2+1, mid+1, r)
    return tree[node]

def query_segtree(nums, tree, node, l, r, s_idx, e_idx):
    if l > e_idx or r < s_idx:
        return 0
    if l >= s_idx and r <= e_idx:
        return tree[node]
    mid = (l + r) // 2
    l_child = query_segtree(nums, tree, node*2, l, mid, s_idx, e_idx)
    r_child = query_segtree(nums, tree, node*2+1, mid+1, r, s_idx, e_idx)
    return l_child + r_child

def update_segtree(nums, tree, node, l, r, idx, diff):
    tree[node] += diff
    if l == r:
        return
    else:
        mid = (l + r) // 2
        if idx >= l and idx <= mid:
            update_segtree(nums, tree, node*2, l, mid, idx, diff)
        else:
            update_segtree(nums, tree, node*2+1, mid+1, r, idx, diff)


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    
    segtree = [0] * 4 * n
    init_segtree(nums, segtree, 1, 0, n-1)
    # print(nums)
    
    for _ in range(m+k):
        a, b, c = map(int, input().split())
        b -= 1
        if a == 1:
            # update
            update_segtree(nums, segtree, 1, 0, n-1, b, c-nums[b])
            nums[b] = c
            # print(segtree)
        elif a == 2:
            # range sum
            c -= 1
            answer = query_segtree(nums, segtree, 1, 0, n-1, b, c)
            print(answer)
            