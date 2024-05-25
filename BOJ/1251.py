import sys
input = sys.stdin.readline

word = input().rstrip()
result = []
for i in range(len(word) - 2):
    for j in range(i + 1, len(word) - 1):
        result.append(''.join([word[i::-1], word[j:i:-1], word[:j:-1]]))
result.sort()
print(result[0])
