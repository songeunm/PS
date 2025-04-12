# 수열과 쿼리 16
# SegmentTree

import sys
input = sys.stdin.readline

def init_segtree(nums, tree, node, l, r):
    if l == r:
        tree[node] = (nums[l], l)
    else:
        mid = (l + r) // 2
        l_child, l_idx = init_segtree(nums, tree, node*2, l, mid)
        r_child, r_idx = init_segtree(nums, tree, node*2+1, mid+1, r)
        if l_child <= r_child:
            tree[node] = (l_child, l_idx)
        else:
            tree[node] = (r_child, r_idx)
    return tree[node]

def query_segtree(nums, tree, node, l, r, target_l, target_r):
    if l > target_r or r < target_l:
        return float('inf'), 0
    elif l >= target_l and target_r >= r:
        return tree[node]
    else:
        mid = (l + r) // 2
        l_child, l_idx = query_segtree(nums, tree, node*2, l, mid, target_l, target_r)
        r_child, r_idx = query_segtree(nums, tree, node*2+1, mid+1, r, target_l, target_r)
        if l_child <= r_child:
            return l_child, l_idx
        else:
            return r_child, r_idx

def update_segtree(nums, tree, node, l, r, idx, new_val):
    if l == r == idx:
        tree[node] = (new_val, idx)
    elif l <= idx and idx <= r:
        mid = (l + r) // 2
        l_child, l_idx = update_segtree(nums, tree, node*2, l, mid, idx, new_val)
        r_child, r_idx = update_segtree(nums, tree, node*2+1, mid+1, r, idx, new_val)
        if l_child <= r_child:
            tree[node] = l_child, l_idx
        else:
            tree[node] = r_child, r_idx
    return tree[node]


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    
    segtree = [0] * 4 * n
    init_segtree(nums, segtree, 1, 0, n-1)
    # print(segtree)
    
    m = int(input())
    for _ in range(m):
        cmd, i, j = map(int, input().split())
        i -= 1
        if cmd == 1:
            # update
            update_segtree(nums, segtree, 1, 0, n-1, i, j)
            nums[i] = j
        elif cmd == 2:
            # query: range minimum
            j -= 1
            min_val, min_idx = query_segtree(nums, segtree, 1, 0, n-1, i, j)
            print(min_idx + 1)