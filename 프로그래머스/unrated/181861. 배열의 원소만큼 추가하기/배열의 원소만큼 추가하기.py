def solution(arr):
    X = []  # 빈 배열 X를 초기화합니다.
    for a in arr:  # arr의 각 원소에 대하여
        X.extend([a] * a)  # 원소 a를 a번 X 배열에 추가합니다.
    return X  # 최종 배열 X를 반환합니다.