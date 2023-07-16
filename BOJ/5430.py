import sys
from collections import deque

input = sys.stdin.readline

def parse_array(string):
    if string == '[]':
        return []
    lst = string[1:-1].split(',')
    lst = list(map(int, lst))
    return lst
    
def exec_func(func, dequeue):
    func = func.replace("RR", "")
    func = func.replace("RDRD", "P")
    for f in func:
        if f == 'R':
            dequeue.reverse()
        elif f == 'D':
            if not dequeue:
                return -1
            else:
                dequeue.popleft()
        elif f == 'P':
            if len(dequeue) < 2:
                return -1
            else:
                dequeue.pop()
                dequeue.popleft()
    return dequeue

def make_result(lst):
    s = '['
    for l in lst:
        s += str(l)
        s += ","
    s = s[:-1] + ']'
    return s

t = int(input().rstrip())
answer = []
for _ in range(t):
    func = input().rstrip()
    n = int(input().rstrip())
    q = deque(parse_array(input().rstrip()))
    q = exec_func(func, q)
    if not q:
        answer.append('[]')
    elif q == -1:
        answer.append('error')
    else:
        answer.append(make_result(list(q)))
for a in answer:
    print(a)