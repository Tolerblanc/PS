import sys
input = sys.stdin.readline

try:
    while True:
        n, k = map(int, input().split())
        answer = n

        while n >= k:
            answer += n // k
            n = n // k + n % k
        print(answer)
except:
    exit()
