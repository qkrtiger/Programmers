def hanoi(n, start, target, auxiliary, result):
    if n == 1:
        result.append([start, target])
    else:
        hanoi(n-1, start, auxiliary, target, result)
        result.append([start, target])
        hanoi(n-1, auxiliary, target, start, result)

def solution(n):
    result = []
    hanoi(n, 1, 3, 2, result)
    return result