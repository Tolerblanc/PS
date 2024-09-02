import sys
input = sys.stdin.readline

string = input().rstrip()
seq = set()
for i in range(len(string)):
    for j in range(i, len(string)):
        seq.add(string[i:j+1])
print(len(seq))
