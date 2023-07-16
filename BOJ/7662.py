import sys, heapq

sys.stdin = open('input.txt')
input = sys.stdin.readline

answer = []

tc = int(input().rstrip())
for _ in range(tc):
    maxHeap = []
    minHeap = []
    check = {}
    count = 0
    n = int(input().rstrip())
    for _ in range(n):
        oper, num = input().rstrip().split()
        if oper == 'I': #insert
            heapq.heappush(maxHeap, -int(num))
            heapq.heappush(minHeap, int(num))
            check[num] = check.get(num, 0) + 1
            count += 1
        elif oper == 'D': #delete
            try:
                if num == '1': #del max
                    temp = str(-heapq.heappop(maxHeap))
                    while temp not in check:
                        temp = str(-heapq.heappop(maxHeap))
                if num == '-1': #del min
                    temp = str(heapq.heappop(minHeap))
                    while temp not in check:
                        temp = str(heapq.heappop(minHeap)) 
                count -= 1
                check[temp] = check.get(temp, 0) - 1
                if check[temp] == 0:
                    del check[temp]
            except IndexError:
                count = 0
                maxHeap = []
                minHeap = []
                check = {}
                continue
    if count == 0:
        answer.append('EMPTY')
    elif count == 1:
        temp = list(check.keys())
        answer.append(str(temp[0]) + ' ' + str(temp[0]))
    else:
        result = ''
        temp = str(-heapq.heappop(maxHeap))
        while temp not in check:
            temp = str(-heapq.heappop(maxHeap))
        result += temp
        temp = str(heapq.heappop(minHeap))
        while temp not in check:
            temp = str(heapq.heappop(minHeap))
        result += ' '
        result += temp
        answer.append(result)
for a in answer:
    print(a)