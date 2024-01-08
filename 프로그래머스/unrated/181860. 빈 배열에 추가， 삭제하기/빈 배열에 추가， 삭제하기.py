def solution(arr, flag):
    X = []  # 빈 배열 X를 초기화합니다.
    for i in range(len(flag)):  # flag 배열의 길이만큼 순회합니다.
        if flag[i]:  # flag[i]가 True일 경우
            X.extend([arr[i]] * (arr[i] * 2))  # arr[i]를 arr[i] * 2번 X 배열에 추가합니다.
        else:  # flag[i]가 False일 경우
            if len(X) >= arr[i]:  # X의 길이가 arr[i]보다 크거나 같을 때만 제거를 수행합니다.
                X = X[:-arr[i]]  # X의 마지막 arr[i]개의 원소를 제거합니다.
    return X  # 최종 배열 X를 반환합니다.