def solution(A, B):
    A.sort()
    B.sort()

    a = 0
    for i, b in enumerate(B):
        if A[a] < b:
            a += 1
    return a
