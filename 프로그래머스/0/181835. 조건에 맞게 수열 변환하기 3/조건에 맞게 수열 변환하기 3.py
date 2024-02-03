def solution(arr, k):
    # k가 홀수인 경우 arr의 모든 원소에 k를 곱합니다.
    if k % 2 == 1:
        arr = [num * k for num in arr]
    # k가 짝수인 경우 arr의 모든 원소에 k를 더합니다.
    else:
        arr = [num + k for num in arr]
    
    return arr