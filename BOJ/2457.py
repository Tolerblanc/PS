import sys
input = sys.stdin.readline

n = int(input())
flowers = []
for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    flowers.append((sm, sd, em, ed))
flowers.sort()

prev = [0, 0, 3, 1]
cnt = 0
for sm, sd, em, ed in flowers:
    psm, psd, pem, ped = prev
    if pem >= 12 or pem < sm or (pem == sm and ped < sd):
        break
    if em < pem or (em == pem and ed < ped):
        continue
    if psm < sm or (psm == sm and psd < sd):
        cnt += 1
        prev[0] = pem
        prev[1] = ped
    if pem < em or (pem == em and ped < ed):
        prev[2] = em
        prev[3] = ed

print(cnt if prev[2] >= 12 else 0)
