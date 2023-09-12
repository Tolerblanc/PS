import sys
from bisect import bisect_right
input = sys.stdin.readline


class MergeSortTree:
    def __init__(self, n):
        self.n = n
        self.tree = [[] for _ in range(4*n + 1)]

    def _update(self, node, left, right, idx, num):
        if left > idx or right < idx:
            return
        self.tree[node].append(num)
        if (left == right):
            return
        mid = (left + right) // 2
        self._update(node * 2, left, mid, idx, num)
        self._update(node * 2 + 1, mid + 1, right, idx, num)

    def _query(self, node, left, right, node_left, node_right, num):  # node_left, node_right => 쿼리 구간
        if left > node_right or right < node_left:
            return 0
        if node_left <= left and right <= node_right:
            # 현재 노드 길이 - upper_bound idx(num)
            return len(self.tree[node]) - bisect_right(self.tree[node], num)
        mid = (left + right) // 2
        return (self._query(node * 2, left, mid, node_left, node_right, num) + self._query(node * 2 + 1, mid + 1, right, node_left, node_right, num))

    def update(self, idx, num):
        return self._update(1, 1, self.n, idx, num)

    def query(self, left, right, k):
        return self._query(1, 1, self.n, left, right, k)

    def sort(self):
        for i in range(1, self.n * 4 + 1):
            self.tree[i].sort()


n = int(input())
mst = MergeSortTree(n)
nums = list(map(int, input().split()))
for idx, num in enumerate(nums):
    mst.update(idx + 1, num)
mst.sort()
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(mst.query(a, b, c))
