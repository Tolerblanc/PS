import math

def solution(w,h):
    gcd = math.gcd(w, h)
    w_prime = w // gcd
    h_prime = h // gcd
    less = w_prime if w_prime < h_prime else h_prime
    delta = h_prime / w_prime if w_prime < h_prime else w_prime / h_prime
    cnt = 0 # 단위 격자에서 직선 밑에 있는 1x1 사각형 개수
    for i in range(1, less):
        cnt += int(delta * i)
    cnt = w_prime * h_prime - cnt * 2 # cnt : 단위 격자에서 직선이 지나가는 사각형 개수
    return w * h - (cnt * gcd)
