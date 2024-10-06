import sys
import math
input = sys.stdin.readline

coor = []
for _ in range(3):
    coor.append(tuple(map(int, input().split())))


def delta(coor1, coor2):
    x1, y1 = coor1
    x2, y2 = coor2
    return (y2 - y1) / (x2 - x1) if x1 != x2 else math.inf


chicken = delta(coor[0], coor[1]) == delta(
    coor[1], coor[2]) == delta(coor[2], coor[1])
print('WINNER WINNER CHICKEN DINNER!' if not chicken else 'WHERE IS MY CHICKEN?')
