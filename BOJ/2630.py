import sys

#sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input().rstrip())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().rstrip().split())))

white = 0
blue = 0

def summary(paper):
    result = 0
    for p in paper:
        result += sum(p)
    return result
    
def make_color_paper(paper, n):
    global blue, white
    if summary(paper) == n * n:
        blue += 1
        return
    if summary(paper) == 0:
        white += 1
        return
    if n == 2:
        blue += summary(paper)
        white += 4 - summary(paper)
        return
    paper1 = [x[:n//2] for x in paper[:n//2]] 
    paper2 = [x[n//2:] for x in paper[:n//2]]
    paper3 = [x[:n//2] for x in paper[n//2:]]
    paper4 = [x[n//2:] for x in paper[n//2:]]
    make_color_paper(paper1, n//2)
    make_color_paper(paper2, n//2)
    make_color_paper(paper3, n//2)
    make_color_paper(paper4, n//2)

make_color_paper(lst, n)
print(white)
print(blue)