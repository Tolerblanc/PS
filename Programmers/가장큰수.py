def solution(numbers):
    lst = [str(n) for n in numbers]
    lst.sort(key = lambda x : (x * 4)[:4],reverse = True)
    return '0' if lst[0] == '0' else ''.join(lst)