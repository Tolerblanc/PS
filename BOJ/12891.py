import sys
input = sys.stdin.readline

s, p = map(int, input().split())
string = input().rstrip()
constraints = list(map(int, input().split()))
constraints = {
    'A': constraints[0],
    'C': constraints[1],
    'G': constraints[2],
    'T': constraints[3],
}
counter = {
    'A': 0,
    'C': 0,
    'G': 0,
    'T': 0,
}


def check():
    if counter['A'] >= constraints['A'] and \
        counter['C'] >= constraints['C'] and \
        counter['G'] >= constraints['G'] and \
        counter['T'] >= constraints['T']:
        return True
    return False


answer = 0
for i in range(p):
    counter[string[i]] += 1

if check():
    answer += 1

for left in range(1, s - p + 1):
    counter[string[left-1]] -= 1
    counter[string[left+p-1]] += 1
    if check():
        answer += 1
print(answer)
