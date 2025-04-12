# 구간 합 구하기 2
# SegmentTree, LazyPropagation

import sys
input = sys.stdin.readline

def init_segtree(nums, tree, node, l, r):
    if l == r:
        tree[node] = nums[l]
    else:
        mid = (l + r) // 2
        l_child = init_segtree(nums, tree, node*2, l, mid)
        r_child = init_segtree(nums, tree, node*2+1, mid+1, r)
        tree[node] = l_child + r_child
    return tree[node]

#### LazyPropagation
def propagate_segtree(lazy, tree, node, l, r):
    if lazy[node] != 0:
        tree[node] += (r - l + 1) * lazy[node]
        if l != r:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

def query_segtree(lazy, tree, node, l, r, target_l, target_r):
    propagate_segtree(lazy, tree, node, l, r)
    
    if r < target_l or l > target_r:
        return 0
    elif target_l <= l and r <= target_r:
        return tree[node]
    else:
        mid = (l + r) // 2
        l_child = query_segtree(lazy, tree, node*2, l, mid, target_l, target_r)
        r_child = query_segtree(lazy, tree, node*2+1, mid+1, r, target_l, target_r)
        return l_child + r_child

def update_segtree(lazy, tree, node, l, r, target_l, target_r, add_val):
    propagate_segtree(lazy, tree, node, l, r)
    
    if r < target_l or l > target_r:
        return
    elif target_l <= l and r <= target_r:
        lazy[node] += add_val
        return
    else:
        mid = (l + r) // 2
        update_segtree(lazy, tree, node*2, l, mid, target_l, target_r, add_val)
        update_segtree(lazy, tree, node*2+1, mid+1, r, target_l, target_r, add_val)
        if max(l, target_l) <= min(r, target_r):
            tree[node] += (min(r, target_r) - max(l, target_l) + 1) * add_val

"""
##### non_LazyPropagation
def query_segtree(nums, tree, node, l, r, target_l, target_r):
    if r < target_l or l > target_r:
        return 0
    elif target_l <= l and r <= target_r:
        return tree[node]
    else:
        mid = (l + r) // 2
        l_child = query_segtree(nums, tree, node*2, l, mid, target_l, target_r)
        r_child = query_segtree(nums, tree, node*2+1, mid+1, r, target_l, target_r)
        return l_child + r_child

def update_segtree(nums, tree, node, l, r, target_l, target_r, added_val):
    if r < target_l or l > target_r:
        return
    elif target_l <= l and r <= target_r and l == r:
        tree[node] += added_val
        return
    else:
        mid = (l + r) // 2
        update_segtree(nums, tree, node*2, l, mid, target_l, target_r, added_val)
        update_segtree(nums, tree, node*2+1, mid+1, r, target_l, target_r, added_val)
        tree[node] = tree[node*2] + tree[node*2+1]
"""


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    
    segtree = [0] * (4 * n)
    lazy = [0] * (4 * n)
    init_segtree(nums, segtree, 1, 0, n-1)
    # print(segtree)
    
    for _ in range(m+k):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            a, b, c, d = cmd
            # update
            b, c = b-1, c-1
            update_segtree(lazy, segtree, 1, 0, n-1, b, c, d)
            # print(f"lazy: {lazy}")
            # print(f"tree: {segtree}")
        elif cmd[0] == 2:
            a, b, c = cmd
            # query
            b, c = b-1, c-1
            answer = query_segtree(lazy, segtree, 1, 0, n-1, b, c)
            # print(f"lazy: {lazy}")
            # print(f"tree: {segtree}")
            print(answer)
