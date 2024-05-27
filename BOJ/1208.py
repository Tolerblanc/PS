from collections import Counter
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
left = Counter()
right = Counter()


def get_subsequence_sum(seq, counter):
    sub = []  # seq의 부분 수열 합
    for s in seq:
        for i in range(len(sub)):
            sub.append(sub[i] + s)
        sub.append(s)
    for s in sub:
        counter[s] += 1


get_subsequence_sum(nums[:n//2], left)
get_subsequence_sum(nums[n//2:], right)

answer = 0
for key in left.keys():
    answer += left[key] * right[s - key]
answer += right[s]
answer += left[s]
print(answer)
