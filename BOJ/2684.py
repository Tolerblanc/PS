import sys
input = sys.stdin.readline

seq = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH']
for _ in range(int(input())):
    case = input().strip()
    result = [0] * 8
    for i in range(38):
        result[seq.index(case[i:i+3])] += 1
    print(*result)
