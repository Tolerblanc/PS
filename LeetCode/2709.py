from collections import defaultdict
from collections import deque


class Solution:
    def getPrimeFactorEdges(self, primeFactorList: dict[set], num: int) -> None:
        factor = set()
        origin = num
        while num % 2 == 0:
            factor.add(2)
            num //= 2

        for i in range(3, int(origin ** 0.5) + 2, 2):
            while num % i == 0:
                factor.add(i)
                num //= i

        if num >= 2:
            factor.add(num)

        for f in factor:
            primeFactorList[f] |= factor - {f}

    def isAllConnected(self, primeFactorList: dict[set]) -> bool:
        visited = set()
        start = list(primeFactorList.keys())[0]
        q = deque([start])
        visited.add(start)
        while q:
            prev = q.popleft()
            for curr in primeFactorList[prev]:
                if curr not in visited:
                    visited.add(curr)
                    q.append(curr)

        return visited & primeFactorList.keys() == primeFactorList.keys()

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if 1 in set(nums):
            return False

        primeFactorList = defaultdict(set)

        for num in nums:
            self.getPrimeFactorEdges(primeFactorList, num)

        return self.isAllConnected(primeFactorList)
