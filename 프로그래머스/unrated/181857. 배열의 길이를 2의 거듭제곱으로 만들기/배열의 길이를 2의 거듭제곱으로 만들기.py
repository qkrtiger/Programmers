import math

def solution(arr):
    length = len(arr)
    
    # arr의 길이가 2의 거듭제곱인지 확인
    if length & (length - 1) == 0:
        return arr
    
    # 2의 거듭제곱이 될 때까지 0 추가
    next_length = 2 ** math.ceil(math.log2(length))
    arr.extend([0] * (next_length - length))
    
    return arr