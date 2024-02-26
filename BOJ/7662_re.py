import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    maxHeap = []
    minHeap = []
    checker = defaultdict(int)
    for _ in range(int(input())):
        oper, num = input().split()
        if oper == 'I':
            heapq.heappush(maxHeap, -int(num))
            heapq.heappush(minHeap, int(num))
            checker[num] += 1
        elif oper == 'D':
            try:
                if num == '1':
                    temp = str(-heapq.heappop(maxHeap))
                    while temp not in checker:
                        temp = str(-heapq.heappop(maxHeap))
                else:
                    temp = str(heapq.heappop(minHeap))
                    while temp not in checker:
                        temp = str(heapq.heappop(minHeap))
                checker[temp] -= 1
                if checker[temp] == 0:
                    del checker[temp]
            except IndexError:
                maxHeap = []
                minHeap = []
                checker = defaultdict(int)
    if len(checker.keys()) == 0:
        print('EMPTY')
    elif len(checker.keys()) == 1:
        lst = list(checker.keys())
        print(f'{lst[0]} {lst[0]}')
    else:
        maxValue = str(-heapq.heappop(maxHeap))
        while maxValue not in checker:
            maxValue = str(-heapq.heappop(maxHeap))
        minValue = str(heapq.heappop(minHeap))
        while minValue not in checker:
            minValue = str(heapq.heappop(minHeap))
        print(f'{maxValue} {minValue}')