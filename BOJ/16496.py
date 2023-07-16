import sys
from functools import cmp_to_key
#sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input().rstrip())
nums = input().rstrip().split()

def compare(str1, str2):
    n1 = str1 + str2
    n2 = str2 + str1
    return int(n1) - int(n2)

nums = sorted(nums, key = cmp_to_key(compare), reverse = True)
print(int(''.join(nums)))