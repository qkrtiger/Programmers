def solution(arr, k):
    result = []
    
    for num in arr:
        if num not in result:
            result.append(num)
        if len(result) == k:
            break
    
    # 완성된 배열의 길이가 k보다 작으면 나머지 값을 -1로 채움
    while len(result) < k:
        result.append(-1)
    
    return result