def solution(a, d, included):
    # 등차수열의 합을 저장할 변수
    total = 0

    for i in range(len(included)):
        if included[i]:
            # i + 1항의 값을 계산하여 등차수열의 합에 더함
            term = a + i * d
            total += term

    return total