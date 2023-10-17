def solution(arr, queries):
    results = []

    for query in queries:
        s, e, k = query
        result = -1  # 초기값을 -1로 설정

        for i in range(s, e + 1):
            if arr[i] > k:
                if result == -1:
                    result = arr[i]
                else:
                    result = min(result, arr[i])

        results.append(result)

    return results