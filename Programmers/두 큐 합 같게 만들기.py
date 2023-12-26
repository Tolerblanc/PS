def solution(queue1, queue2):
    q = queue1 + queue2
    left = 0
    right = len(queue1)
    q1sum = sum(queue1)
    q2sum = sum(queue2)
    
    cnt = 0
    while cnt < len(q) * 2:
        if q1sum == q2sum:
            return cnt
        elif q1sum > q2sum:
            q1sum -= q[left]
            q2sum += q[left]
            left = (left + 1) % len(q)
        else: #q1sum < q2sum
            q1sum += q[right]
            q2sum -= q[right]
            right = (right + 1) % len(q)
        cnt += 1
    return -1