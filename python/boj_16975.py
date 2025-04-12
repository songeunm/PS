# 수열과 쿼리 21
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

def propagate_segtree(lazy, tree, node, l, r):
    if lazy[node] != 0:
        tree[node] += lazy[node]
        if l != r:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

def query_segtree(lazy, tree, node, l, r, idx):
    propagate_segtree(lazy, tree, node, l, r)
    if l == r == idx:
        print(tree[node])
        return
    else:
        mid = (l + r) // 2
        if l <= idx <= mid:
            query_segtree(lazy, tree, node*2, l, mid, idx)
        else:
            query_segtree(lazy, tree, node*2+1, mid+1, r, idx)

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

if __name__ == "__main__":
    n = int(input())
    seq = list(map(int, input().split()))
    
    segtree = [0] * (4 * n)
    lazy = [0] * (4 * n)
    init_segtree(seq, segtree, 1, 0, n-1)
    
    m = int(input())
    for _ in range(m):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            # update
            c, i, j, k = cmd
            i, j = i-1, j-1
            update_segtree(lazy, segtree, 1, 0, n-1, i, j, k)
        elif cmd[0] == 2:
            # query
            idx = cmd[1] - 1
            query_segtree(lazy, segtree, 1, 0, n-1, idx)