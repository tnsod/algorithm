# Lazy Propagation in Bottom-up Segment Tree
# Range Update & Range Sum Query Implementation

import sys
# fastInput
def input():return sys.stdin.readline().rstrip()

# init segment tree
def init(N, size, tree : list, arr : tuple) -> None:
    for i in range(N):
        tree[i + size] = arr[i]
    for i in range(size - 1, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

# propagate lazy values to children
def push(node, width, tree : list, lazy : list) -> None:
    if lazy[node]:
        lazy[node * 2] += lazy[node]
        lazy[node * 2 + 1] += lazy[node]

        child_width = width // 2
        tree[node * 2] += lazy[node] * child_width
        tree[node * 2 + 1] += lazy[node] * child_width

        lazy[node] = 0

# update current node by merging children values
def pull(node, tree : list) -> None:
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

# range update : add val to range [l, r]
def update(l, r, val, size, height, tree : list, lazy : list) -> None:
    l += size
    r += size

    for i in range(height, 0, -1):
        width = 1 << i
        # If 'l' is not the start of a block at height 'i', push lazy from parent
        if (l >> i) << i != l:
            push(l >> i, width, tree, lazy)
        # If 'r' is not the end of a block at height 'i', push lazy from parent
        if ((r + 1) >> i) << i != r + 1:
            push(r >> i, width, tree, lazy)
    
    L, R = l, r
    width = 1
    while L <= R:
        if L % 2 == 1:
            tree[L] += val * width
            if L < size: lazy[L] += val
            L += 1
        if R % 2 == 0:
            tree[R] += val * width
            if R < size: lazy[R] += val
            R -= 1
        L //= 2
        R //= 2
        width *= 2
    
    for i in range(height + 1):
        if (l >> i) << i != l:
            pull(l >> i, tree)
        if ((r + 1) >> i) << i != r + 1:
            pull(r >> i, tree)

# range sum query
def query(l, r, size, height, tree : list, lazy : list) -> int:
    l += size
    r += size

    for i in range(height, 0, -1):
        width = 1 << i
        if (l >> i) << i != l:
            push(l >> i, width, tree, lazy)
        if ((r + 1) >> i) << i != r + 1:
            push(r >> i, width, tree, lazy)
    
    res = 0
    while l <= r:
        if l % 2 == 1:
            res += tree[l]
            l += 1
        if r % 2 == 0:
            res += tree[r]
            r -= 1
        l //= 2
        r //= 2
    return res

def main():
    N, Q = map(int, input().split())
    arr = tuple(map(int, input().split()))
    
    size = 1
    height = 0
    while size < N:
        size <<= 1
        height += 1
    
    tree = [0] * (2 * size)
    lazy = [0] * (2 * size)
    init(N, size, tree, arr)

    for _ in range(Q):
        # q input example:
        # -------------------------------------------------
        # Note: [l, r] is 1-based indexing
        # 1 1 4 3  -> Update: add 3 to range [1, 4]
        # 2 1 4    -> Query:  print sum of range [1, 4]
        q = tuple(map(int, input().split()))
        if q[0] == 1:
            l, r, value = q[1:]
            # Convert 1-based input to 0-based implementation
            l -= 1
            r -= 1
            update(l, r, value, size, height, tree, lazy)
        else:
            l, r = q[1:]
            l -= 1
            r -= 1
            print(query(l, r, size, height, tree, lazy))

if __name__ == '__main__':
    main()
